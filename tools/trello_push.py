"""Upload raw/<code>/out/*.webp to the Trello card and move it to list "Listing Shopify".
Usage: trello_push.py CODE [CODE ...]. Skips files already attached (same name)."""
import json, os, re, sys, uuid, urllib.request
SRC, DST = "6b016e21b216a76361fe462b", "6b011a404f4e904f95c96860"
RAW = os.path.expanduser("~/Downloads/Ecom-Project/embroidery/raw")
env = dict(l.strip().split("=", 1) for l in open(os.path.expanduser("~/.config/embroidery/trello.env")) if "=" in l)
AUTH = {"Authorization": f'OAuth oauth_consumer_key="{env["TRELLO_KEY"]}", oauth_token="{env["TRELLO_TOKEN"]}"'}
def call(method, url, data=None, headers=None):
    req = urllib.request.Request(url, data=data, method=method, headers={**AUTH, **(headers or {})})
    return json.loads(urllib.request.urlopen(req, timeout=120).read() or b"null")
cards = call("GET", f"https://api.trello.com/1/lists/{SRC}/cards?fields=name&attachments=true&attachment_fields=name")
by = {}
for c in cards:
    m = re.search(r"EMBN\d+", c["name"], re.I)
    if m: by[m.group(0).upper()] = c
for code in [a.upper() for a in sys.argv[1:]]:
    c = by.get(code)
    if not c: print(code, "not in Đã duyệt"); continue
    have = {a["name"] for a in c["attachments"]}
    files = sorted(f for f in os.listdir(f"{RAW}/{code}/out") if f.endswith(".webp"))
    up = 0
    for f in files:
        if f in have: continue
        b = uuid.uuid4().hex
        body = (f"--{b}\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\n{f}\r\n"
                f"--{b}\r\nContent-Disposition: form-data; name=\"file\"; filename=\"{f}\"\r\nContent-Type: image/webp\r\n\r\n").encode() \
               + open(f"{RAW}/{code}/out/{f}", "rb").read() + f"\r\n--{b}--\r\n".encode()
        call("POST", f"https://api.trello.com/1/cards/{c['id']}/attachments", body, {"Content-Type": f"multipart/form-data; boundary={b}"}); up += 1
    call("PUT", f"https://api.trello.com/1/cards/{c['id']}?idList={DST}&pos=top")
    print(code, f"uploaded {up}/{len(files)}, moved to Listing Shopify")
