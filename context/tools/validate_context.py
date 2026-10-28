#!/usr/bin/env python3
from pathlib import Path
import json,sys
try: import yaml
except ImportError: sys.exit('Install PyYAML: python -m pip install pyyaml')
root=Path(__file__).resolve().parents[1]
m=yaml.safe_load((root/'product-system/context-manifest.yaml').read_text('utf8'))
errors=[]
if m.get('context_id')!='norm':errors.append('wrong context_id')
def check(v):
 if isinstance(v,dict):
  for x in v.values():check(x)
 elif isinstance(v,list):
  for x in v:check(x)
 elif isinstance(v,str) and v.startswith('product-system/'):
  if '*' in v:
   if not list(root.glob(v)):errors.append('empty glob '+v)
  elif not (root/v).is_file():errors.append('missing '+v)
for v in (m.get('documents',{}),m.get('loading',{})):check(v)
reg=yaml.safe_load((root/'product-system/02_domain/registry/service_registry.yaml').read_text('utf8'))
for k,v in reg['services'].items():
 if not (root/v['primary_document']).exists():errors.append('missing service '+k)
 if v.get('questions_document') and not (root/v['questions_document']).exists():errors.append('missing questions '+k)
# Validate composition and selected pattern/organism routing locally.
comp=root/'product-system/04_ui/foundation/composition-index.json'
if not comp.exists(): errors.append('missing composition-index.json')
patroot=root/'product-system/04_ui/patterns'
pat=yaml.safe_load((patroot/'pattern-registry.yaml').read_text('utf8'))
for item in pat.get('patterns',[]):
 p=patroot/item['path']
 if not p.exists():errors.append('missing pattern route: '+item['path'])
for item in pat.get('runtime_overlay',{}).values():
 for key in ('path','shared_shell_spec'):
  if key in item and not (patroot/item[key]).is_file():errors.append('missing runtime route: '+item[key])
orgroot=root/'product-system/04_ui/organisms'
org=yaml.safe_load((orgroot/'organism-registry.yaml').read_text('utf8'))
for item in org.get('organisms',[]):
 if not (orgroot/item['runtime_path']).is_file():errors.append('missing organism route: '+item['runtime_path'])
# Engineering standards 05/06/07 contract. Do not leak full rules into product/prototype stages.
eng_paths=[
 'product-system/06_engineering/engineering-standards.md',
 'product-system/06_engineering/component-structure-and-handoff.md',
]
frontend_profiles=('for_frontend_planning','for_frontend_implementation','for_frontend_review')
nonengineering_profiles=('always','for_product_intent_and_brief','for_ux_solution',
                         'for_visual_html_prototype','for_ux_sync','for_sdd_specification')
loading=m.get('loading',{})
for profile in frontend_profiles:
 actual=loading.get(profile,[])
 for path in eng_paths:
  if path not in actual:errors.append('engineering rules missing from '+profile+': '+path)
for profile in nonengineering_profiles:
 for path in eng_paths:
  if path in loading.get(profile,[]):errors.append('engineering rules loaded too early in '+profile)
for path in eng_paths:
 if path not in m.get('documents',{}).get('engineering_standards',[]):
  errors.append('missing engineering document index: '+path)
 if not (root/path).is_file():errors.append('missing canonical engineering standard: '+path)
if m.get('loading',{}).get('on_demand',{}).get('engineering_standards')!='product-system/06_engineering/*.md':
 errors.append('engineering standards on_demand route missing')
for name in ('frontend-planner','frontend-implementer','frontend-reviewer'):
 f=root.parent/'agent/.gigacode/agents'/f'{name}.md'
 if not f.is_file():errors.append('missing engineering agent: '+name)
 elif '06_engineering' not in f.read_text('utf8'):
  errors.append('engineering agent does not load standard: '+name)
for f in (root.parent/'agent/.gigacode/skills/05-07-frontend-standards').rglob('*.md'):
 content=f.read_text('utf8')
 if 'NORMaliz' in content or 'Проверяй реальные пути, версии, UI Kit' in content:
  errors.append('damaged frontend rule: '+str(f))
for path in eng_paths:
 if not (root/path).is_file():continue
 text=(root/path).read_text('utf8')
 if len(text)<3500:errors.append('engineering standard unexpectedly short: '+path)
 if any(token in text.lower() for token in ('sber','сбер')):
  errors.append('corporate identifier in engineering standard: '+path)
# Optional external evidence field must remain neutral and local-only.
evidence=root.parent/'agent/.gigacode/product-evidence.yaml.example'
if not evidence.exists():errors.append('missing evidence YAML sample')
else:
 sample=yaml.safe_load(evidence.read_text('utf8'))
 for product in sample.get('products',{}).values():
  fr=product.get('frontend_rules')
  if not isinstance(fr,dict) or not all(k in fr for k in ('local_root','index_url','toolchain_root')):
   errors.append('missing frontend_rules evidence mapping')
  elif any(fr.values()):errors.append('filled frontend_rules paths in distributable example')
for f in root.rglob('*.yaml'):
 try:yaml.safe_load(f.read_text('utf8'))
 except Exception as e:errors.append('YAML '+str(f)+': '+str(e))
for f in root.rglob('*.json'):
 try:json.loads(f.read_text('utf8'))
 except Exception as e:errors.append('JSON '+str(f)+': '+str(e))
agent=root.parent/'agent/.gigacode'
for f in (agent/'skills').glob('*/SKILL.md'):
 try:
  n=yaml.safe_load(f.read_text('utf8').split('---',2)[1])['name']
  if n!=f.parent.name:errors.append('skill name mismatch: '+str(f.parent))
 except Exception as e:errors.append('invalid skill: '+str(f)+': '+str(e))
for d in (agent/'skills').iterdir():
 if d.is_dir() and not (d/'SKILL.md').exists():errors.append('missing skill file '+d.name)
for p in root.rglob('*'):
 if p.is_file() and p.suffix.lower() in {'.zip','.tgz','.tar','.gz','.pdf','.docx','.png','.jpg','.jpeg'}:errors.append('unexpected archive/binary '+str(p))
print(json.dumps({'status':'passed' if not errors else 'failed','errors':errors,'service_count':len(reg['services']),'skills':len(list((agent/'skills').glob('*/SKILL.md'))),'agents':len(list((agent/'agents').glob('*.md'))),'context_files':len(list(root.rglob('*.*')))},ensure_ascii=False,indent=2))
sys.exit(bool(errors))
