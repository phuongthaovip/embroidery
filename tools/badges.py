"""Add EmbroThread navy format badges (2 rows) to the bottom of a main mockup.
Usage: badges.py in.webp out.webp
Row 1 = file formats really in the design zip. Row 2 = machine brands they open on."""
from PIL import Image, ImageDraw, ImageFont
import sys
NAVY, CREAM = (46, 66, 89), (251, 247, 239)
ROW1 = ["PES", "DST", "EXP", "JEF", "VP3", "HUS", "XXX"]
ROW2 = ["Brother", "Babylock", "Janome", "Husqvarna", "Pfaff", "Singer", "Bernina", "Tajima"]
F = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
def row(d, W, y, labels, size, h, gap, padx):
    f = ImageFont.truetype(F, size)
    ws = [d.textlength(t, font=f) + 2*padx for t in labels]
    x = (W - sum(ws) - gap*(len(ws)-1)) / 2
    for t, w in zip(labels, ws):
        d.rounded_rectangle([x, y, x+w, y+h], radius=h/2, fill=NAVY)
        d.text((x+w/2, y+h/2), t, font=f, fill=CREAM, anchor="mm"); x += w + gap
im = Image.open(sys.argv[1]).convert("RGB"); W, H = im.size; s = W/1000
d = ImageDraw.Draw(im)
row(d, W, H - 128*s, ROW1, int(26*s), 46*s, 12*s, 20*s)
row(d, W, H - 68*s, ROW2, int(17*s), 32*s, 8*s, 12*s)
im.save(sys.argv[2], quality=82)
