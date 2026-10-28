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
