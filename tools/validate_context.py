#!/usr/bin/env python3
from pathlib import Path
import json, re, sys, glob
try:
    import yaml
except ImportError:
    print('PyYAML is required: pip install pyyaml', file=sys.stderr)
    raise

root = Path(__file__).resolve().parents[1] / 'context'
manifest_path = root / 'product-system/context-manifest.yaml'
errors=[]
class UniqueKeyLoader(yaml.SafeLoader):
    pass
def unique_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in result:
            raise ValueError(f'duplicate YAML key: {key}')
        result[key] = loader.construct_object(value_node, deep=deep)
    return result
UniqueKeyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)
with manifest_path.open(encoding='utf-8') as f:
    manifest=yaml.safe_load(f)

paths=[]
def collect(obj):
    if isinstance(obj, str):
        if obj.startswith(('product-system/','sources/','.gigacode/','setup/')):
            paths.append(obj)
    elif isinstance(obj, list):
        for x in obj: collect(x)
    elif isinstance(obj, dict):
        for x in obj.values(): collect(x)
collect(manifest.get('documents',{}))
collect(manifest.get('loading',{}))
collect(manifest.get('prototype',{}))

# Validate direct and glob manifest paths.
for rel in sorted(set(paths)):
    if '*' in rel:
        if not glob.glob(str(root/rel), recursive=True):
            errors.append(f'glob has no matches: {rel}')
    elif not (root/rel).exists():
        errors.append(f'missing: {rel}')

# Parse structured files.
for y in root.rglob('*.yaml'):
    try:
        yaml.load(y.read_text(encoding='utf-8'), Loader=UniqueKeyLoader)
    except Exception as e: errors.append(f'yaml: {y.relative_to(root)}: {e}')
for j in root.rglob('*.json'):
    try:
        json.loads(j.read_text(encoding='utf-8'))
    except Exception as e: errors.append(f'json: {j.relative_to(root)}: {e}')

# Business registry consistency.
bc = root/'product-system/02_domain/registry'
try:
    services = yaml.safe_load((bc/'service_registry.yaml').read_text(encoding='utf-8'))
    roles = yaml.safe_load((bc/'role_registry.yaml').read_text(encoding='utf-8'))
    caps = yaml.safe_load((bc/'capability_registry.yaml').read_text(encoding='utf-8'))
    source_registry = yaml.safe_load((bc/'source_registry.yaml').read_text(encoding='utf-8'))
    service_ids=set(services.get('services',{}))
    cap_ids=[]
    for cap in caps.get('capabilities',[]):
        cap_ids.append(cap.get('id'))
        if cap.get('service') not in service_ids:
            errors.append(f"capability {cap.get('id')} references unknown service: {cap.get('service')}")
    if len(cap_ids)!=len(set(cap_ids)):
        errors.append('duplicate capability IDs')
    for rid, role in roles.get('roles',{}).items():
        for sid in role.get('services',[]):
            if sid not in service_ids:
                errors.append(f'role {rid} references unknown service: {sid}')
    # Validate source registry file/index paths; globs must match.
    for src in source_registry.get('sources',[]):
        refs=[]
        if src.get('path'): refs.append(src['path'])
        if src.get('index'): refs.append(src['index'])
        refs.extend(src.get('paths',[]) or [])
        for rel in refs:
            if '*' in rel:
                if not glob.glob(str(root/rel), recursive=True):
                    errors.append(f"source {src.get('id')} glob has no matches: {rel}")
            elif not (root/rel).exists():
                errors.append(f"source {src.get('id')} missing path: {rel}")
except Exception as e:
    errors.append(f'business registry validation failed: {e}')

# Verify the executable visual router, not only top-level manifest loading paths.
ui=root/'product-system/04_ui'
visual_paths=[]
def visual_path(base, rel):
    target=(base/rel.split('#',1)[0]).resolve()
    visual_paths.append(str(target))
    if not target.is_relative_to(root.resolve()):
        errors.append(f'visual path escapes context: {rel}')
    elif not target.exists():
        errors.append(f'missing visual path: {base.relative_to(root)}/{rel}')
    elif '#' in rel and target.suffix=='.html':
        anchor=rel.split('#',1)[1]
        if not re.search(r'\bid=[\"\x27]'+re.escape(anchor)+r'[\"\x27]',target.read_text(encoding='utf-8')):
            errors.append(f'missing HTML anchor: {rel}')
try:
    registry=yaml.safe_load((ui/'patterns/pattern-registry.yaml').read_text(encoding='utf-8'))
    pattern_ids=[entry['id'] for entry in registry['patterns']]
    if len(pattern_ids)!=len(set(pattern_ids)): errors.append('duplicate pattern IDs')
    for entry in registry['patterns']:
        for key in ['path','runtime_path','canonical_shell_spec','organism']:
            if entry.get(key): visual_path(ui/'patterns',entry[key])
    for entry in registry['runtime_overlay']['runtime_patterns'].values():
        for key in ['path','shared_shell_spec','norm_reference','historical_composition_reference']:
            if entry.get(key): visual_path(ui/'patterns',entry[key])
        for name in entry.get('authoring_patterns',[]):
            if name not in pattern_ids: errors.append(f'unknown authoring pattern: {name}')
    organisms=yaml.safe_load((ui/'organisms/organism-registry.yaml').read_text(encoding='utf-8'))
    for entry in organisms['organisms']:visual_path(ui/'organisms',entry['runtime_path'])
    refs=yaml.safe_load((ui/'references/reference-registry.yaml').read_text(encoding='utf-8'))['references']
    composition=json.loads((ui/'foundation/composition-index.json').read_text(encoding='utf-8'))
    for rel in composition['load']['core']+[composition['load']['qa'],composition['load']['implementation_guide']]:visual_path(ui/'foundation',rel)
    for entry in composition['patterns']:
        visual_path(ui/'foundation',entry['file'])
        for reference in entry['references']:
            if reference not in refs:errors.append(f"unknown composition reference in {entry['id']}: {reference}")
    starter=root/manifest['prototype']['starter']['path']
    # Runtime GigaCode files live in agent/.gigacode, separate from context provider.
    # Keep a legacy fallback for standalone/older distributions.
    agent_root=root.parent/'agent/.gigacode'
    if not agent_root.exists():
        agent_root=root.parent
    fallback=agent_root/'skills/03-build-visual-html-prototype/assets/norm-html-starter'
    required=['index.html','styles.css','prototype.js','norm-components.css','norm-components.js']
    for name in required:
        visual_path(starter,name)
        if fallback.exists() and (not (fallback/name).exists() or (starter/name).read_bytes()!=(fallback/name).read_bytes()):
            errors.append(f'starter fallback drift: {name}')
    component_js=(starter/'norm-components.js').read_text(encoding='utf-8')
    if 'const brand=' not in component_js: errors.append('starter brand primitive missing')
    if '<img class=\"brand-mark' in component_js: errors.append('starter must not depend on removed image logos')
    html=(starter/'index.html').read_text(encoding='utf-8')
    for name in required[1:5]:
        if f'"{name}"' not in html:errors.append(f'starter asset not linked: {name}')
    for first,last in [('styles.css','norm-components.css'),('norm-components.js','prototype.js')]:
        if html.find(f'"{first}"')>html.find(f'"{last}"'):errors.append(f'wrong asset order: {first} / {last}')
except Exception as e:
    errors.append(f'visual routing validation failed: {e}')

# The source code and image packages must stay excluded; full frontend normative files must remain.
for suffix in ('.tgz','.zip','.png','.jpg','.jpeg','.gif','.webp','.svg','.ico','.pdf','.docx'):
    for f in root.rglob('*'+suffix):
        errors.append(f'forbidden bundled image or archive: {f.relative_to(root)}')
front_norms=['product-system/05_engineering/frontend-standards-subagent.md','product-system/05_engineering/component-structure-data-barrels-ui-kit.md']
for p in front_norms:
    if not (root/p).exists(): errors.append(f'frontend normative missing: {p}')
for stage in ['for_frontend_planning','for_frontend_implementation','for_frontend_review']:
    for p in front_norms:
        if p not in manifest.get('loading',{}).get(stage,[]):
            errors.append(f'engineering stage {stage} does not load {p}')
for stage in ['for_product_intent_and_brief','for_ux_solution','for_visual_html_prototype','for_ux_sync','for_sdd_specification']:
    for p in front_norms:
        if p in manifest.get('loading',{}).get(stage,[]):
            errors.append(f'engineering source leaked into {stage}: {p}')

# Skill/agent YAML headers are parsed by strict loaders before any stage can run.
# This check is optional for a standalone context-only archive.
headers_checked=0
agent_root=root.parent/'agent/.gigacode'
if not agent_root.exists():
    agent_root=root.parent
for directory in ['skills','agents']:
    for p in (agent_root/directory).rglob('*.md'):
        text=p.read_text(encoding='utf-8')
        if not text.startswith('---\n'): continue
        try:
            header=text.split('---',2)[1]
            yaml.load(header,Loader=UniqueKeyLoader)
            headers_checked+=1
        except Exception as e:errors.append(f'invalid frontmatter: {p.relative_to(agent_root)}: {e}')
for name,profile in manifest.get('skill_profiles',{}).items():
    if profile not in manifest.get('loading',{}):errors.append(f'unknown loading profile for {name}: {profile}')

# Required v4 compact business layer must be wired into early profiles.
manifest_text=manifest_path.read_text(encoding='utf-8')
for required in [
    'product-system/02_domain/registry/service_registry.yaml',
    'product-system/02_domain/registry/role_registry.yaml',
    'product-system/02_domain/registry/capability_registry.yaml',
    'product-system/02_domain/registry/product_decisions.md',
]:
    if required not in manifest_text:
        errors.append(f'v4 business source not routed: {required}')

# Hygiene: removed historical authoring/report layers must stay absent.
for forbidden in ['analysis/pattern-reports','product-system/04_ui/audit']:
    if (root/forbidden).exists(): errors.append(f'forbidden runtime report layer present: {forbidden}')
for p in root.rglob('*'):
    if p.is_file() and p.name in {'.DS_Store'} or (p.is_file() and p.name.startswith('._')):
        errors.append(f'metadata file present: {p.relative_to(root)}')
    if p.is_file() and p.suffix.lower() in {'.md','.yaml','.yml','.json','.py'}:
        text=p.read_text(encoding='utf-8', errors='replace')
        legacy_token = 'lova' + 'ble'
        if re.search(legacy_token, text, re.I): errors.append(f'forbidden legacy instruction reference: {p.relative_to(root)}')
        if p.resolve() != Path(__file__).resolve():
            for stale in ['norm-product-context-v3-mvp','product_to_ui_master_prompt.md','known_capabilities.md','roles.md']:
                if stale in text:
                    errors.append(f'stale v3/business reference {stale}: {p.relative_to(root)}')

result={
    'context_id': manifest.get('context_id'),
    'context_version': manifest.get('context_version'),
    'package_version': manifest.get('package_version'),
    'files_checked': sum(1 for p in root.rglob('*') if p.is_file()),
    'manifest_paths_checked': len(set(paths)),
    'visual_paths_checked': len(set(visual_paths)),
    'skill_agent_headers_checked': headers_checked,
    'errors': errors,
    'status': 'passed' if not errors else 'failed'
}
if '--write-report' in sys.argv:
    (root/'CONTEXT_VALIDATION.json').write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print(json.dumps(result, ensure_ascii=False, indent=2))
sys.exit(1 if errors else 0)
