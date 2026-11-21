"""Replace <code>-N.webp attachments on EmbroT cards (any list) with the files in raw/<code>/out/.
Usage: trello_replace.py CODE [CODE ...]"""
import json, os, re, sys, uuid, urllib.request
BOARD = "uu51yxaq"; RAW = os.path.expanduser("~/Downloads/Ecom-Project/embroidery/raw")
env = dict(l.strip().split("=", 1) for l in open(os.path.expanduser("~/.config/embroidery/trello.env")) if "=" in l)
AUTH = {"Authorization": f'OAuth oauth_consumer_key="{env["TRELLO_KEY"]}", oauth_token="{env["TRELLO_TOKEN"]}"'}
def call(m, u, d=None, h=None):
    return json.loads(urllib.request.urlopen(urllib.request.Request(u, data=d, method=m, headers={**AUTH, **(h or {})}), timeout=120).read() or b"null")
cards = call("GET", f"https://api.trello.com/1/boards/{BOARD}/cards?fields=name&attachments=true&attachment_fields=name")
by = {re.search(r"EMBN\d+", c["name"], re.I).group(0).upper(): c for c in cards if re.search(r"EMBN\d+", c["name"], re.I)}
for code in [a.upper() for a in sys.argv[1:]]:
    c = by[code]; files = sorted(f for f in os.listdir(f"{RAW}/{code}/out") if f.endswith(".webp")); gone = 0
    for a in c["attachments"]:
        if a["name"] in files: call("DELETE", f"https://api.trello.com/1/cards/{c['id']}/attachments/{a['id']}"); gone += 1
    for f in files:
        b = uuid.uuid4().hex
        body = (f"--{b}\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\n{f}\r\n--{b}\r\nContent-Disposition: form-data; name=\"file\"; filename=\"{f}\"\r\nContent-Type: image/webp\r\n\r\n").encode() + open(f"{RAW}/{code}/out/{f}", "rb").read() + f"\r\n--{b}--\r\n".encode()
        call("POST", f"https://api.trello.com/1/cards/{c['id']}/attachments", body, {"Content-Type": f"multipart/form-data; boundary={b}"})
    print(code, f"replaced {gone} -> {len(files)}")
