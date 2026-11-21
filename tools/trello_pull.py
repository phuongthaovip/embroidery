"""Download attachments of cards in Trello list "Đã duyệt" (board EmbroT) into raw/<code>/.
Usage: trello_pull.py [CODE ...]   (no codes = all cards). Reads ~/.config/embroidery/trello.env.
Writes raw/cards.json (code, name, attachment names, kind)."""
import json, os, re, sys, urllib.request
LIST = "6b016e21b216a76361fe462b"
RAW = os.path.expanduser("~/Downloads/Ecom-Project/embroidery/raw")
env = dict(l.strip().split("=", 1) for l in open(os.path.expanduser("~/.config/embroidery/trello.env")) if "=" in l)
K, T = env["TRELLO_KEY"], env["TRELLO_TOKEN"]
AUTH = {"Authorization": f'OAuth oauth_consumer_key="{K}", oauth_token="{T}"'}
def get(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers=AUTH), timeout=120).read()
cards = json.loads(get(f"https://api.trello.com/1/lists/{LIST}/cards?fields=name&attachments=true&attachment_fields=name,url,bytes"))
want = {c.upper() for c in sys.argv[1:]}
index = []
for c in cards:
    m = re.search(r"EMBN\d+", c["name"], re.I)
    code = m.group(0).upper() if m else c["id"]
    names = [a["name"] for a in c["attachments"]]
    pngs = [n for n in names if n.lower().endswith(".png")]
    kind = "single" if any(n.upper() == code + ".PNG" for n in pngs) else ("bundle" if len(pngs) > 1 else ("jpg" if names else "empty"))
    index.append({"code": code, "name": c["name"], "kind": kind, "attachments": names})
    if want and code not in want: continue
    d = os.path.join(RAW, code); os.makedirs(d, exist_ok=True)
    for a in c["attachments"]:
        if not re.search(r"\.(png|jpe?g)$", a["name"], re.I): continue
        p = os.path.join(d, a["name"])
        if os.path.exists(p) and os.path.getsize(p) == a.get("bytes"): continue
        open(p, "wb").write(get(a["url"]))
    print(code, kind, len(os.listdir(d)))
json.dump(index, open(os.path.join(RAW, "cards.json"), "w"), ensure_ascii=False, indent=1)
from collections import Counter; print(Counter(x["kind"] for x in index))
