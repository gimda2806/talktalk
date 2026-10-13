#!/usr/bin/env python3
"""숏드라마 영상에 달항아리 워터마크를 얹는다.

사용 예:
  python3 zeta/tools/add_video_watermark.py 완성본.mp4
  python3 zeta/tools/add_video_watermark.py 클립폴더/ --dark
  python3 zeta/tools/add_video_watermark.py 완성본.mp4 --pos bottom-right --opacity 0.4

기본값: 오른쪽 위, 영상 가로의 7%, 투명도 35%, 가장자리 여백 가로의 3.5%.
결과는 원본 옆에 `이름_wm.mp4`로 저장한다(원본은 건드리지 않음). 소리는 그대로 복사한다.
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

ASSETS = Path(__file__).resolve().parent.parent / "assets"
MARKS = {
    False: ASSETS / "watermark-moonjar.png",
    True: ASSETS / "watermark-moonjar-dark-outline.png",
}
VIDEO_EXT = {".mp4", ".mov", ".m4v", ".webm", ".mkv"}


def video_width(path):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "v:0",
         "-show_entries", "stream=width", "-of", "json", str(path)],
        check=True, capture_output=True, text=True).stdout
    return json.loads(out)["streams"][0]["width"]


def overlay_xy(pos, m):
    x = "W-w-%d" % m if pos.endswith("right") else "%d" % m
    y = "%d" % m if pos.startswith("top") else "H-h-%d" % m
    return x, y


def add_mark(src, args):
    w = video_width(src)
    mark_w = max(16, round(w * args.size) // 2 * 2)
    m = round(w * args.margin)
    x, y = overlay_xy(args.pos, m)
    dst = src.with_name(src.stem + "_wm" + src.suffix)
    filt = (f"[1:v]format=rgba,scale={mark_w}:-1,colorchannelmixer=aa={args.opacity}[wm];"
            f"[0:v][wm]overlay={x}:{y}:format=auto")
    subprocess.run(
        ["ffmpeg", "-y", "-loglevel", "error", "-i", str(src), "-i", str(MARKS[args.dark]),
         "-filter_complex", filt, "-c:v", "libx264", "-crf", "18", "-preset", "medium",
         "-pix_fmt", "yuv420p", "-c:a", "copy", "-movflags", "+faststart", str(dst)],
        check=True)
    print(f"{src.name} → {dst.name}")


def main():
    p = argparse.ArgumentParser(description="숏드라마 영상에 달항아리 워터마크 얹기")
    p.add_argument("inputs", nargs="+", help="영상 파일 또는 폴더")
    p.add_argument("--pos", default="top-right",
                   choices=["top-right", "top-left", "bottom-right", "bottom-left"])
    p.add_argument("--size", type=float, default=0.07, help="영상 가로 대비 워터마크 가로 (기본 0.07)")
    p.add_argument("--opacity", type=float, default=0.35, help="불투명도 0~1 (기본 0.35)")
    p.add_argument("--margin", type=float, default=0.035, help="가장자리 여백, 영상 가로 대비 (기본 0.035)")
    p.add_argument("--dark", action="store_true", help="밝은 화면용 진한 테두리 버전")
    args = p.parse_args()

    files = []
    for s in args.inputs:
        path = Path(s)
        if path.is_dir():
            files += sorted(f for f in path.iterdir()
                            if f.suffix.lower() in VIDEO_EXT and not f.stem.endswith("_wm"))
        elif path.is_file():
            files.append(path)
        else:
            sys.exit(f"없는 경로: {s}")
    if not files:
        sys.exit("영상 파일을 찾지 못했다.")
    for f in files:
        add_mark(f, args)


if __name__ == "__main__":
    main()
