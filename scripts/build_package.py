"""Build an allowlisted package; never copy repository evidence into runtime."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import zipfile

root = Path(__file__).resolve().parents[1]
name = 'z-jack-work-assignments'
dest = root / 'dist' / name
resources = (root / 'package-resources.txt').read_text().splitlines()
files = [root / 'SKILL.md']
for entry in resources:
    if entry not in ('agents', 'references'):
        raise ValueError(f'Unexpected runtime resource: {entry}')
    files.extend(p for p in (root / entry).rglob('*') if p.is_file())
expected = {p.relative_to(root).as_posix() for p in files}
if dest.exists():
    extra = {p.relative_to(dest).as_posix() for p in dest.rglob('*') if p.is_file()} - expected
    if extra:
        raise RuntimeError(f'Unexpected output files; inspect before rebuilding: {extra}')
hashes = {}
for source in sorted(files):
    if source.is_symlink() or not source.resolve().is_relative_to(root):
        raise ValueError('Runtime source must stay inside repository')
    relative = source.relative_to(root)
    target = dest / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, target)
    hashes[relative.as_posix()] = hashlib.sha256(target.read_bytes()).hexdigest()
archive = root / 'dist' / f'{name}.zip'
with zipfile.ZipFile(archive, 'w', compression=zipfile.ZIP_DEFLATED) as out:
    for relative in sorted(hashes):
        info = zipfile.ZipInfo(f'{name}/{relative}', date_time=(2026, 10, 18, 0, 0, 0))
        info.compress_type = zipfile.ZIP_DEFLATED
        info.external_attr = 0o100644 << 16
        out.writestr(info, (dest / relative).read_bytes())
commit = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=root, text=True).strip()
receipt = {'source_commit': commit, 'files': hashes, 'zip_sha256': hashlib.sha256(archive.read_bytes()).hexdigest()}
(root / 'dist' / 'release-receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')
print(json.dumps(receipt, indent=2))
