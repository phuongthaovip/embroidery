#!/usr/bin/env python3
"""Chuẩn hoá ảnh + handle + tên file + alt trước khi list lên Shopify (EmbroThread).

Quy tắc: 00-context/shopify-listing-standard.md, mục 3 và 3b.

Đầu vào: 1 file JSON, mỗi phần tử là 1 sản phẩm:
  [{"code": "VPE26111823",
    "title": "Snowman in Gift Box Christmas Machine Embroidery Design",
    "images": [{"src": "raw/VPE26111823/a.png", "role": "main"},
               {"src": "raw/VPE26111823/b.jpg", "role": "included", "count": 9},
               {"src": "raw/VPE26111823/c.jpg", "role": "on-sweatshirt"}]}]

role: main | included | hoop-sizes | detail | on-<đồ vật> (on-sweatshirt, on-tote-bag…)

Chạy:  python3 tools/shopify_prep.py input.json out_dir
Kết quả: out_dir/<handle>*.webp + out_dir/manifest.json (handle, file, alt từng ảnh).
Chỉ dùng cwebp (có sẵn) + Pillow.
"""
import json
import re
import subprocess
import sys
import tempfile
import unicodedata
from pathlib import Path

from PIL import Image

WIDTH = 1000
QUALITY = 80
HANDLE_MAX = 60
STOP_WORDS = {"a", "an", "the", "and", "with", "of", "for", "in", "on", "to"}


def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    text = text.lower().replace("'", "").replace("’", "")
    return re.sub(r"[^a-z0-9]+", "-", text).strip("-")


def make_handle(title: str) -> str:
    """Handle ngắn ≤ 60 ký tự, keyword chính ở đầu, luôn kết thúc bằng đuôi loại sản phẩm."""
    t = re.sub(r",?\s*\d+\s+designs?\s*$", "", title, flags=re.I)  # bỏ ", 20 Designs"
    words = slugify(t).split("-")
    # Tách đuôi loại sản phẩm để luôn giữ lại
    endings = [
        ["machine", "embroidery", "design", "bundle"],
        ["embroidery", "design", "bundle"],
        ["embroidery", "design", "set"],
        ["embroidery", "bundle"],
        ["embroidery", "alphabet", "font"],
        ["machine", "embroidery", "design"],
        ["embroidery", "design"],
    ]
    tail = []
    for e in endings:
        if words[-len(e):] == e:
            tail, words = e, words[: -len(e)]
            break
    # "... design bundle" → gọn thành "embroidery-bundle"
    if tail and tail[-1] in ("bundle", "set"):
        tail = ["embroidery", "bundle"]
    elif tail[-1:] == ["font"]:
        tail = ["embroidery", "font"]
    else:
        tail = tail or ["embroidery", "design"]

    def build(ws, tl):
        return "-".join(ws + tl)

    # Bước rút gọn dần: bỏ stop word → bỏ "machine" → cắt bớt từ cuối phần mô tả
    if len(build(words, tail)) > HANDLE_MAX:
        words = [w for w in words if w not in STOP_WORDS]
    if len(build(words, tail)) > HANDLE_MAX and tail[0] == "machine":
        tail = tail[1:]
    while len(build(words, tail)) > HANDLE_MAX and len(words) > 2:
        words = words[:-1]
    return build(words, tail)


def alt_text(title: str, role: str, count=None) -> str:
    core = re.sub(r",?\s*\d+\s+designs?\s*$", "", title, flags=re.I)
    subject = re.sub(r"\s*(machine\s+)?embroidery\s+(design\s*)?(bundle|set|alphabet font|design)?$",
                     "", core, flags=re.I).strip()
    if role == "main":
        alt = title
    elif role == "included":
        alt = f"All {count} designs included in the {core}" if count else f"Designs included in the {core}"
    elif role == "hoop-sizes":
        alt = f"{subject} embroidery design hoop sizes and file formats"
    elif role == "detail":
        alt = f"Close-up stitch detail of the {subject} embroidery design"
    elif role.startswith("on-"):
        item = role[3:].replace("-", " ")
        alt = f"{subject} embroidery design stitched on a {item}"
    else:
        alt = title
    return alt[:125]


def to_webp(src: Path, dst: Path) -> None:
    with Image.open(src) as im:
        im = im.convert("RGBA")
        bg = Image.new("RGB", im.size, (255, 255, 255))
        bg.paste(im, mask=im.split()[3])
        if bg.width > WIDTH:
            bg = bg.resize((WIDTH, round(bg.height * WIDTH / bg.width)), Image.LANCZOS)
        with tempfile.NamedTemporaryFile(suffix=".png") as tmp:
            bg.save(tmp.name)
            subprocess.run(["cwebp", "-quiet", "-q", str(QUALITY), "-metadata", "none",
                            tmp.name, "-o", str(dst)], check=True)


def main(inp: str, out: str) -> None:
    items = json.loads(Path(inp).read_text())
    out_dir = Path(out)
    out_dir.mkdir(parents=True, exist_ok=True)
    seen, manifest = {}, []
    for it in items:
        handle = make_handle(it["title"])
        if handle in seen:  # trùng handle → thêm mã card
            handle = f"{handle}-{it['code'].lower()}"
        seen[handle] = it["code"]
        role_count, imgs = {}, []
        for img in it["images"]:
            role = img.get("role", "main")
            role_count[role] = role_count.get(role, 0) + 1
            suffix = "" if role == "main" else f"-{role}"
            if role_count[role] > 1:
                suffix += f"-{role_count[role]}"
            fname = f"{handle}{suffix}.webp"
            to_webp(Path(img["src"]), out_dir / fname)
            imgs.append({"file": fname, "role": role,
                         "alt": alt_text(it["title"], role, img.get("count")),
                         "kb": round((out_dir / fname).stat().st_size / 1024)})
        manifest.append({"code": it["code"], "title": it["title"], "handle": handle, "images": imgs})
        print(f"{it['code']:14} {handle}  ({len(imgs)} ảnh)")
    (out_dir / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
