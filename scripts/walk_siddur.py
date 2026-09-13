#!/usr/bin/env python3
"""
Walk the whole of Siddur Ashkenaz and fetch every leaf.

The tree's traversal order IS the order of the davening, so we keep it —
that is what gives the site its sequence without anyone authoring one.

Writes corpus.json: [{id, path[], en, section, ref, version, license, words[]}]
Hebrew rules, each bought by a bug tonight:
  · unescape entities, normalise NBSP        (&nbsp; printed literally)
  · split on MAQAF                           (את־מצרים was one token)
  · drop unvocalised lines where vocalised   (halachic instructions)
    ones exist
"""
import urllib.parse, urllib.request, json, re, os, time, html as _html
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

A   = "https://www.sefaria.org/api"
OUT = Path(os.path.expanduser("~/.claude/jobs/2920a354/tmp/corpus.json"))
NIK = re.compile(r"[֑-ׇ]")
voc = lambda s: bool(NIK.search(s or ""))

def get(u, tries=3):
    for _ in range(tries):
        try:
            return json.load(urllib.request.urlopen(u, timeout=45))
        except Exception:
            time.sleep(1.2)
    return None

# ── enumerate the leaves, in order ───────────────────────────────────────
idx = get(f"{A}/index/Siddur_Ashkenaz")
leaves = []
def walk(n, path=()):
    if isinstance(n, dict):
        t = n.get("title") or n.get("sharedTitle")
        p = path + ((t,) if t else ())
        kids = n.get("nodes") or n.get("contents") or []
        if kids:
            for ch in kids: walk(ch, p)
        elif t:
            leaves.append(p)
    elif isinstance(n, list):
        for x in n: walk(x, path)
walk(idx.get("schema") or idx)
print(f"  leaves: {len(leaves)}")

def slugify(path):
    s = "-".join(path[1:])
    s = re.sub(r"[^A-Za-z0-9]+", "-", s).strip("-").lower()
    return s[:90] or "x"

MET = urllib.parse.quote("The Metsudah siddur, 1981", safe="")

def fetch(path):
    ref = ", ".join(path)
    q = urllib.parse.quote(ref.replace(" ", "_"), safe="")
    d = get(f"{A}/texts/{q}?context=0&vhe={MET}")
    if not d or not (d.get("he") or []):
        d = get(f"{A}/texts/{q}?context=0")
    if not d:
        return None
    def flat(x):
        if isinstance(x, str): return [x]
        o = []
        for i in (x or []): o += flat(i)
        return o
    segs = [_html.unescape(re.sub("<[^>]+>", " ", h)) for h in flat(d.get("he"))]
    segs = [re.sub(r"[ \s]+", " ", s).strip() for s in segs]
    segs = [s for s in segs if s]
    v = [s for s in segs if voc(s)]
    if v: segs = v
    words = []
    for si, seg in enumerate(segs, 1):
        for tok in re.sub("־", " ", seg).split():
            if tok: words.append({"hebrew": tok, "verse": si})
    if not words:
        return None
    return {"id": slugify(path), "path": list(path[1:]), "en": path[-1],
            "section": " > ".join(path[1:-1]),
            "ref": ref, "version": d.get("heVersionTitle"), "license": d.get("license"),
            "segments": len(segs), "words": words}

t0 = time.time()
with ThreadPoolExecutor(10) as ex:
    got = list(ex.map(fetch, leaves))

corpus, empty = [], []
seen = set()
for path, r in zip(leaves, got):
    if not r:
        empty.append(" > ".join(path[1:])); continue
    while r["id"] in seen: r["id"] += "-2"
    seen.add(r["id"])
    corpus.append(r)

json.dump(corpus, open(OUT, "w", encoding="utf-8"), ensure_ascii=False)
tw = sum(len(c["words"]) for c in corpus)
print(f"  fetched  : {len(corpus)} leaves  ·  {tw:,} words  ·  {time.time()-t0:.0f}s")
print(f"  empty    : {len(empty)}")
for e in empty[:8]: print(f"      {e}")
import collections
sec = collections.Counter(c["path"][0] for c in corpus)
print("  by book:")
for k, v in sec.most_common(): print(f"      {k:18} {v:>3} leaves  "
    f"{sum(len(c['words']) for c in corpus if c['path'][0]==k):>6,} words")
print(f"  -> {OUT}")
