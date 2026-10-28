#!/usr/bin/env python3
from pathlib import Path
import json,sys,re
try: import yaml
except ImportError: sys.exit('Install PyYAML: python -m pip install pyyaml')
root=Path(__file__).resolve().parents[1]
manifest=yaml.safe_load((root/'product-system/context-manifest.yaml').read_text(encoding='utf8'))
errors=[]
if manifest.get('context_id')!='sample_product':errors.append('unexpected sample context id')
for category in ('documents','loading'):
 def walk(v):
  if isinstance(v,str) and v.startswith('product-system/') and '*' not in v and not (root/v).is_file():errors.append('missing: '+v)
  elif isinstance(v,list):
   for a in v:walk(a)
  elif isinstance(v,dict):
   for a in v.values():walk(a)
 walk(manifest.get(category,{}))
agent=root.parent/'agent/.gigacode'
for skill in (agent/'skills').iterdir():
 if not skill.is_dir():continue
 f=skill/'SKILL.md'
 if not f.exists():errors.append('missing SKILL.md: '+skill.name);continue
 body=f.read_text(encoding='utf8')
 try: name=yaml.safe_load(body.split('---',2)[1]).get('name')
 except Exception as e:errors.append('invalid skill YAML: '+skill.name+': '+str(e));continue
 if name!=skill.name:errors.append('skill name != dir: '+str(name))
for p in root.rglob('*.yaml'):
 try:yaml.safe_load(p.read_text(encoding='utf8'))
 except Exception as e:errors.append('invalid YAML '+str(p)+': '+str(e))
for p in root.rglob('*.json'):
 try:json.loads(p.read_text(encoding='utf8'))
 except Exception as e:errors.append('invalid JSON '+str(p)+': '+str(e))
for e in ['context/sources/product-openspec','context/sources/analytical-specs','context/sources/ui-kit']:
 if (root.parent/e).exists():errors.append('bundled external source '+e)
result={'status':'passed' if not errors else 'failed','errors':errors,'skills':len(list((agent/'skills').glob('*/SKILL.md'))),'agents':len(list((agent/'agents').glob('*.md')))}
print(json.dumps(result,ensure_ascii=False,indent=2))
sys.exit(0 if not errors else 1)
