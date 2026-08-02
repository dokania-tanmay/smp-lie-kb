#!/usr/bin/env python3
"""Pull sources into refs/.

    python tools/fetch.py arxiv 2503.12345 [--key someCiteKey2025]
    python tools/fetch.py zotero --tag lie-groups
    python tools/fetch.py zotero --collection ABCD1234
    python tools/fetch.py --self-check

arXiv gives the LaTeX source tree at refs/@<key>/; Zotero gives refs/@<key>.pdf.
Turning either into refs/@<key>.md is Claude's job, not this script's.

Zotero needs ZOTERO_API_KEY and ZOTERO_USER_ID in the environment:
    export ZOTERO_API_KEY=...        # zotero.org/settings/keys
    export ZOTERO_USER_ID=...        # the numeric id on that same page

ponytail: stdlib only (urllib/tarfile/json). No requests, no pyzotero.
"""

import argparse
import gzip
import io
import json
import os
import re
import sys
import tarfile
import urllib.parse
import urllib.request
from pathlib import Path

REFS = Path(__file__).resolve().parent.parent / "refs"
UA = "smp-lie-kb/1.0 (https://arxiv.org/help/api; mailto:krnavneet13@gmail.com)"


def get(url, headers=None):
    req = urllib.request.Request(url, headers={"User-Agent": UA, **(headers or {})})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


# --- arxiv ------------------------------------------------------------------

def arxiv_id(s):
    """Normalize anything that identifies an arXiv paper to a bare versionless id."""
    s = s.strip().rstrip("/")
    s = re.sub(r"^(https?://)?(www\.)?arxiv\.org/(abs|pdf|e-print)/", "", s)
    s = re.sub(r"^arxiv:", "", s, flags=re.I)
    s = re.sub(r"\.pdf$", "", s)
    s = re.sub(r"v\d+$", "", s)
    if not re.fullmatch(r"\d{4}\.\d{4,5}|[a-z-]+(\.[A-Z]{2})?/\d{7}", s):
        raise ValueError(f"not an arXiv id: {s!r}")
    return s


def fetch_arxiv(ident, key=None):
    aid = arxiv_id(ident)
    dest = REFS / ("@" + (key or aid.replace("/", "-")))
    blob = get(f"https://arxiv.org/e-print/{aid}")

    dest.mkdir(parents=True, exist_ok=True)
    try:
        with tarfile.open(fileobj=io.BytesIO(blob)) as tar:
            # filter='data' blocks absolute paths and symlink escapes (py3.12+)
            tar.extractall(dest, filter="data")
    except tarfile.ReadError:
        # single-file submissions come back as a bare gzipped .tex
        (dest / f"{aid.replace('/', '-')}.tex").write_bytes(gzip.decompress(blob))

    tex = sorted(p.relative_to(dest) for p in dest.rglob("*.tex"))
    print(f"{dest}  ({len(tex)} .tex: {', '.join(map(str, tex[:5]))})")
    return dest


# --- zotero -----------------------------------------------------------------

def zotero_creds():
    key, uid = os.environ.get("ZOTERO_API_KEY"), os.environ.get("ZOTERO_USER_ID")
    if not key or not uid:
        sys.exit("set ZOTERO_API_KEY and ZOTERO_USER_ID (zotero.org/settings/keys)")
    return key, uid


def zotero_get(path, api_key, user_id, **params):
    url = f"https://api.zotero.org/users/{user_id}/{path}"
    if params:
        url += "?" + urllib.parse.urlencode(params)
    headers = {"Zotero-API-Version": "3", "Zotero-API-Key": api_key}
    return get(url, headers)


def citekey(data):
    """Better BibTeX key from the Extra field, else creator+year+first title word."""
    m = re.search(r"^Citation Key:\s*(\S+)", data.get("extra", ""), re.M | re.I)
    if m:
        return m.group(1)
    creators = data.get("creators") or [{}]
    last = creators[0].get("lastName") or creators[0].get("name") or "anon"
    year = (re.search(r"\d{4}", data.get("date", "")) or re.match("", "")).group() or "nd"
    word = (re.search(r"[A-Za-z]{4,}", data.get("title", "")) or re.match("", "")).group() or "untitled"
    return f"{last.lower()}{word.capitalize()}{year}"


def fetch_zotero(tag=None, collection=None, limit=100):
    api_key, user_id = zotero_creds()
    params = {"format": "json", "limit": limit}
    if tag:
        params["tag"] = tag
    path = f"collections/{collection}/items" if collection else "items"
    items = json.loads(zotero_get(path, api_key, user_id, **params))

    REFS.mkdir(parents=True, exist_ok=True)
    saved = []
    for item in items:
        data = item["data"]
        if data["itemType"] in ("attachment", "note"):
            continue
        out = REFS / f"@{citekey(data)}.pdf"
        if out.exists():
            continue
        children = json.loads(zotero_get(f"items/{item['key']}/children", api_key, user_id, format="json"))
        pdf = next((c for c in children if c["data"].get("contentType") == "application/pdf"), None)
        if not pdf:
            print(f"  no pdf attached: {data.get('title', '?')[:60]}")
            continue
        out.write_bytes(zotero_get(f"items/{pdf['key']}/file", api_key, user_id))
        print(out)
        saved.append(out)
    print(f"{len(saved)} new pdf(s) in {REFS}")
    return saved


# --- cli --------------------------------------------------------------------

def self_check():
    for raw in ["2503.12345", "arXiv:2503.12345v2", "https://arxiv.org/abs/2503.12345",
                "https://arxiv.org/pdf/2503.12345v1.pdf"]:
        assert arxiv_id(raw) == "2503.12345", raw
    assert arxiv_id("math.DG/0211159") == "math.DG/0211159"
    for bad in ["not-an-id", "12345", ""]:
        try:
            arxiv_id(bad)
        except ValueError:
            pass
        else:
            raise AssertionError(f"accepted {bad!r}")

    assert citekey({"extra": "tex.ids: foo\nCitation Key: khanMeansRandomVariables2025"}) \
        == "khanMeansRandomVariables2025"
    assert citekey({"creators": [{"lastName": "van Goor"}], "date": "2023-05-01",
                    "title": "Equivariant Filter (EqF)"}) == "van goorEquivariant2023"
    assert citekey({}) == "anonUntitlednd"
    print("ok")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--self-check", action="store_true", help="run assertions and exit")
    sub = p.add_subparsers(dest="cmd")

    a = sub.add_parser("arxiv", help="download LaTeX source tree")
    a.add_argument("id", help="id, arXiv:id, or abs/pdf url")
    a.add_argument("--key", help="citekey for the refs/ folder name (default: the arxiv id)")

    z = sub.add_parser("zotero", help="download attached pdfs")
    z.add_argument("--tag")
    z.add_argument("--collection", help="collection key, e.g. ABCD1234")
    z.add_argument("--limit", type=int, default=100)

    args = p.parse_args()
    if args.self_check:
        return self_check()
    if args.cmd == "arxiv":
        fetch_arxiv(args.id, args.key)
    elif args.cmd == "zotero":
        fetch_zotero(args.tag, args.collection, args.limit)
    else:
        p.print_help()


if __name__ == "__main__":
    main()
