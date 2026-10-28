#!/usr/bin/env python3
# External archives and image assets are deliberately excluded from precise-clean package.
from pathlib import Path
import subprocess, zipfile, sys
root=Path(__file__).resolve().parents[1]/'context'
subprocess.run([sys.executable, str(root.parent/'tools/validate_context.py')], check=True)
target=root.parent/f'{root.name}.zip'
if target.exists(): target.unlink()
with zipfile.ZipFile(target,'w',zipfile.ZIP_DEFLATED) as z:
    for p in sorted(root.rglob('*')):
        if p.is_file():
            z.write(p, Path(root.name)/p.relative_to(root))
print(target)
