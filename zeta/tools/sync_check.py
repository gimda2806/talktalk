"""새 프로필 이미지 동기화 점검: 로컬 폴더의 프로필 이미지가 저장소(zeta/generated/)에 이미 있는지 크기로 비교한다(같은 작품·같은 종류의 저장소 파일과 크기가 같으면 같은 이미지).

사용법 (저장소 루트에서):
  python3 zeta/tools/sync_check.py

보는 곳 (둘 다 본다)
- ~/Documents/ChatGPT/이미지 프로필 제작/generated/번호_이름/
- ~/Library/CloudStorage/GoogleDrive-…/내 드라이브/이미지 프로필 제작/번호_이름/   (구글 드라이브 데스크톱 폴더)

대상 파일: `…-main.png` · `…-user-m.png` · `…-user-f.png` (기본 이름이 없을 때 쓰는 `-v2` 같은 재생성본 포함).
이름 앞의 번호는 있어도 없어도 되고, 한글 이름(`148_조남훈-main.png`)이든 영문 이름이든 상관없다.
제외: 3면도·사복 시트·스틸·콘티·카메오·`-prev` 이전본.

판정
- NEW: 저장소 그 폴더에 그 종류(주인공·남·여)의 파일이 아직 없고, 
- CHG: 그 종류가 저장소에 있는데 내용이 다르고, 로컬 파일이 저장소 등록본(마지막 커밋)보다 더 최근에 저장됨
- DRIVE-DIFF: 드라이브 데스크톱 폴더의 파일이 저장소 등록본과 다름. 드라이브 폴더 파일의 수정 시각은 올린 시각이라 최신 여부를 알 수 없으므로 자동 교체하지 않고 눈으로 확인한다.
- 저장소 등록본과 크기가 같으면 세지 않고, 로컬 작업 폴더 파일이 저장소 등록본보다 오래됐으면 세지 않는다.
둘 다 없으면 "새 이미지 없음"을 찍는다.
"""
import hashlib
import os
import re
import subprocess
import time
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
R = ROOT / "zeta/generated"
SOURCES = [
    Path.home() / "Documents/ChatGPT/이미지 프로필 제작/generated",
    Path.home() / "Library/CloudStorage/GoogleDrive-hyukgu86@gmail.com/내 드라이브/이미지 프로필 제작",
]
SKIP = re.compile(r"character-sheet|-prev\.png|닿기직전|reference|shortdrama|kiss|콘티|입맞춤|cameo")


def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def main():
    repo, ct, rsize = {}, {}, {}
    for d0 in os.listdir(R):
        dp = R / d0
        d = unicodedata.normalize("NFC", d0)
        if re.match(r"\d{3}_", d) and dp.is_dir():
            for f in os.listdir(dp):
                m = re.search(r"-(main|user-m|user-f)\.png$", f)
                if m:
                    repo[(d, m.group(1))] = f
                    rsize[(d, m.group(1))] = os.path.getsize(dp / f)
    for (d, k), f in repo.items():
        out = subprocess.run(["git", "log", "-1", "--format=%ct", "--", f"zeta/generated/{unicodedata.normalize('NFD', d)}/{f}"], capture_output=True, text=True, cwd=ROOT).stdout.strip()
        ct[(d, k)] = int(out or 0)
    new, chg, drv, stale, seen = [], [], [], 0, set()
    for src in SOURCES:
        if not src.is_dir():
            continue
        for d0 in sorted(os.listdir(src)):
            d = unicodedata.normalize("NFC", d0)
            if not re.match(r"\d{3}_", d) or not (src / d0).is_dir():
                continue
            for f0 in sorted(os.listdir(src / d0)):
                f = unicodedata.normalize("NFC", f0)
                if not f.endswith(".png") or SKIP.search(f) or re.match(r"\d{3}_C\d\d", f):
                    continue
                m = re.search(r"-(main|user-m|user-f)(-v\d+)?\.png$", f)
                if not m:
                    continue
                lp = src / d0 / f0
                key = (d, m.group(1))
                size = os.path.getsize(lp)
                # 같은 작품·같은 종류의 저장소 파일과 크기가 같으면 같은 이미지로 본다
                # (드라이브 데스크톱 폴더의 파일을 내려받아 해시하지 않으려는 것 — 크기가 다르면 내용도 다르다)
                if key in rsize and rsize[key] == size:
                    continue
                if (d, size) in seen:
                    continue
                seen.add((d, size))
                mt = os.path.getmtime(lp)
                row = (d, f, time.strftime("%m-%d %H:%M", time.localtime(mt)), str(src))
                if key not in repo:
                    new.append(row)
                elif "CloudStorage" in str(src):
                    # 드라이브 데스크톱 폴더 파일의 수정 시각은 올린 시각이라 최신 여부를 알 수 없다 → 눈으로 확인
                    drv.append(row)
                elif mt < ct[key]:
                    stale += 1
                else:
                    chg.append(row)
    print("NEW", [r[:3] for r in new])
    print("CHG", [r[:3] for r in chg])
    print("DRIVE-DIFF(확인 필요)", [r[:3] for r in drv])
    print("stale(저장소가 더 최신)", stale)
    if not new and not chg and not drv:
        print("새 이미지 없음")


if __name__ == "__main__":
    main()
