#!/usr/bin/env python3
"""플롯 md와 숏드라마 콘티 md 파일을 로컬 작업 폴더의 작품별 폴더로 복사한다.

사용 예 (저장소 폴더에서, 먼저 git pull로 최신 main을 받는다):
  python zeta/tools/copy_conti_to_local.py
  python zeta/tools/copy_conti_to_local.py "H:\\항아리\\generated"
  python zeta/tools/copy_conti_to_local.py --dry-run

- 대상: 플롯 zeta/zeta_{번호}_{이름}.md, 콘티 zeta/shortdrama/{번호}_{이름}_숏드라마*.md (기본·강·첫만남·연인발전·연애초기 버전 모두)
- 넣는 곳: {대상 폴더}/{번호}_{이름}/ — 같은 번호로 시작하는 폴더가 이미 있으면 그 폴더, 없으면 새로 만든다.
- 복사만 한다(저장소의 파일은 그대로 둔다). 같은 이름의 파일이 있으면 내용이 다를 때만 덮어쓴다.
"""
import filecmp
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
SRC = ROOT / "zeta" / "shortdrama"
DEFAULT_DEST = Path(r"H:\항아리\generated")


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    dry = "--dry-run" in sys.argv
    dest = Path(args[0]) if args else DEFAULT_DEST
    if not dest.exists():
        sys.exit(f"대상 폴더가 없습니다: {dest}")

    existing = {}
    for d in dest.iterdir():
        m = re.match(r"(\d{3})_", d.name)
        if d.is_dir() and m:
            existing.setdefault(m.group(1), d)

    copied = skipped = 0
    files = [(f, re.match(r"zeta_(\d{3})_(.+)\.md$", f.name)) for f in sorted((ROOT / "zeta").glob("zeta_[0-9][0-9][0-9]_*.md"))]
    files += [(f, re.match(r"(\d{3})_(.+?)_숏드라마", f.name)) for f in sorted(SRC.glob("[0-9][0-9][0-9]_*_숏드라마*.md"))]
    for f, m in files:
        if not m:
            continue
        num, name = m.groups()
        folder = existing.get(num) or dest / f"{num}_{name}"
        target = folder / f.name
        if target.exists() and filecmp.cmp(f, target, shallow=False):
            skipped += 1
            continue
        print(f"{'(미리보기) ' if dry else ''}{f.name} → {folder.name}/")
        if not dry:
            folder.mkdir(exist_ok=True)
            existing.setdefault(num, folder)
            shutil.copy2(f, target)
        copied += 1
    print(f"복사 {copied}개, 이미 같아서 건너뜀 {skipped}개 → {dest}")


if __name__ == "__main__":
    main()
