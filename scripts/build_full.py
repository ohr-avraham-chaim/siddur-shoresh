#!/usr/bin/env python3
"""Siddur Shoresh — the whole Ashkenaz siddur as a link graph."""
import json, os, re, collections, html
from pathlib import Path

T = Path(os.path.expanduser("~/.claude/jobs/2920a354/tmp"))
OUT = T / "siddur-full"
NIK = re.compile(r"[֑-ׇ]")
strip = lambda s: NIK.sub("", s or "")
TRANS = {"א":"a","ב":"b","ג":"g","ד":"d","ה":"h","ו":"v","ז":"z","ח":"ch","ט":"t",
 "י":"y","כ":"k","ך":"k","ל":"l","מ":"m","ם":"m","נ":"n","ן":"n","ס":"s","ע":"o",
 "פ":"p","ף":"p","צ":"tz","ץ":"tz","ק":"q","ר":"r","ש":"sh","ת":"th"}
def rslug(r): return "-".join(TRANS.get(c,"") for c in strip(r) if c in TRANS) or "x"
esc = lambda s: html.escape(str(s or ""))

corpus = json.load(open(T/"corpus.json", encoding="utf-8"))

# ── root lookup: deterministic inventory + graded model output ───────────
forms, meaning = {}, {}
src = json.load(open(os.path.expanduser("~/Projects/torah-apps/Siddur/siddur-shoresh/data.json"), encoding="utf-8"))
for p in src["prayers"]:
    ws = p.get("words", [])
    if not ws or not all((w.get("hebrew") or "").strip() for w in ws): continue
    for w in ws:
        sh = w.get("shoresh") or {}; r = strip(sh.get("root") or "")
        if not r: continue
        meaning.setdefault(r, sh.get("meaning") or "")
        f = strip(w.get("hebrew") or "").strip(".,:;־׃ ")
        if f: forms.setdefault(f, (r, "form"))
for fn in ("model_roots.json", "roots_full.json"):
    if (T/fn).exists():
        for f, v in json.load(open(T/fn, encoding="utf-8")).items():
            if v.get("root"): forms.setdefault(f, (strip(v["root"]), "model-"+v["basis"]))

def lookup(tok):
    f = strip(tok).strip(".,:;־׃!?()[]׳״'\"־ ")
    return forms.get(f, (None, None))

# ── attach ───────────────────────────────────────────────────────────────
roots = {}
basis_tally = collections.Counter()
for c in corpus:
    c["sec"] = " > ".join(c["path"][:-1]) or c["path"][0]
    for w in c["words"]:
        r, b = lookup(w["hebrew"])
        w["root"], w["basis"] = r, b
        basis_tally[b or "unresolved"] += 1
        if not r: continue
        e = roots.setdefault(r, {"root": r, "count": 0, "by_sec": collections.Counter(),
                                 "by_prayer": collections.Counter(), "forms": {}})
        e["count"] += 1; e["by_sec"][c["sec"]] += 1; e["by_prayer"][c["id"]] += 1
        h = w["hebrew"]
        if h not in e["forms"] and len(e["forms"]) < 40: e["forms"][h] = c["id"]

TOTAL = sum(r["count"] for r in roots.values())
ranked = sorted(roots.values(), key=lambda r: -r["count"])
for i, r in enumerate(ranked, 1): r["rank"] = i
byid = {c["id"]: c for c in corpus}
SECS = list(dict.fromkeys(c["sec"] for c in corpus))

neigh = collections.defaultdict(collections.Counter)
for c in corpus:
    rs = {w["root"] for w in c["words"] if w["root"]}
    for a in rs:
        for b in rs:
            if a != b: neigh[a][b] += 1

CSS = open(T/"site.css", encoding="utf-8").read() if (T/"site.css").exists() else ""
HEAD = ('<title>{t}</title><link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
        'family=Frank+Ruhl+Libre:wght@400;500;700&family=IBM+Plex+Sans:wght@400;500;600&'
        'family=IBM+Plex+Mono:wght@400;500&display=swap"><style>{c}</style>')
def page(t, body): return HEAD.format(t=esc(t), c=CSS) + f'<div class="sheet">{body}</div>'

FOOT = ('<footer>The whole of Siddur Ashkenaz, walked from Sefaria — Weekday, Shabbat, '
        'Festivals, Berachot, Kaddish. Hebrew: Metsudah 1981 and Tanach, CC-BY. '
        'Every word records how its root was found; words with none render grey. '
        'Nothing is guessed.</footer>')

(OUT/"root").mkdir(parents=True, exist_ok=True)
(OUT/"tefillah").mkdir(parents=True, exist_ok=True)

def crumb(depth, *parts):
    up = "../"*depth
    o = [f'<a href="{up}index.html">Siddur Shoresh</a>']
    for lab, href in parts:
        o.append("<i>/</i>"); o.append(f'<a href="{up}{href}">{esc(lab)}</a>' if href else esc(lab))
    return '<p class="crumb">'+"".join(o)+"</p>"

# ── root pages ───────────────────────────────────────────────────────────
for r in ranked:
    mx = max(r["by_sec"].values()) if r["by_sec"] else 1
    fp = "".join(
      f'<div class="fp-row"><span class="fp-name{"" if r["by_sec"].get(s) else " none"}">{esc(s)}</span>'
      f'<span class="fp-track"><span class="bar" style="width:{100.0*r["by_sec"].get(s,0)/mx:.1f}%"></span></span>'
      f'<span class="fp-n{"" if r["by_sec"].get(s) else " zero"}">{r["by_sec"].get(s) or "—"}</span></div>'
      for s in SECS if r["by_sec"].get(s)) or '<p class="sub">—</p>'
    fr = "".join(
      f'<div class="form"><span class="f-he" dir="rtl">{esc(h)}</span>'
      f'<span class="f-where"><a class="lnk" href="../tefillah/{pid}.html">{esc(byid[pid]["en"])}</a></span></div>'
      for h, pid in list(r["forms"].items())[:28])
    tp = "".join(
      f'<a class="nbi" href="../tefillah/{pid}.html"><span class="nb-m">{esc(byid[pid]["en"])[:30]}</span>'
      f'<span class="nb-n">{n}</span></a>' for pid, n in r["by_prayer"].most_common(10))
    nb = "".join(
      f'<a class="nbi" href="{rslug(b)}.html"><span class="nb-r" dir="rtl">{esc(b)}</span>'
      f'<span class="nb-n">{roots[b]["count"]}</span></a>' for b, _ in neigh[r["root"]].most_common(8))
    body = (crumb(1, ("roots", None), (r["root"], None)) +
      f'<p class="root" dir="rtl">{esc(r["root"])}</p>'
      f'<p class="gloss">{esc(meaning.get(r["root"], ""))}</p>'
      f'<p class="stats"><span><b>{r["count"]:,}</b> words</span>'
      f'<span><b>{len(r["forms"])}</b> forms</span>'
      f'<span><b>{len(r["by_prayer"])}</b> tefillos</span>'
      f'<span><b>{100.0*r["count"]/TOTAL:.2f}%</b> of the siddur</span>'
      f'<span>rank <b>#{r["rank"]}</b></span></p>'
      f'<h2>Where it lives</h2><p class="sub">Across the whole siddur, by section.</p>{fp}'
      f'<h2>Its tefillos</h2><div class="nb">{tp}</div>'
      f'<h2>The shapes it takes</h2>{fr}'
      + (f'<h2>Keeps company with</h2><div class="nb">{nb}</div>' if nb else "") + FOOT)
    (OUT/"root"/f"{rslug(r['root'])}.html").write_text(page(f'{r["root"]} · Siddur Shoresh', body), encoding="utf-8")

# ── tefillah pages ───────────────────────────────────────────────────────
for c in corpus:
    toks = []
    for w in c["words"]:
        if w["root"]:
            toks.append(f'<a href="../root/{rslug(w["root"])}.html" title="{esc(w["root"])}">{esc(w["hebrew"])}</a>')
        else:
            toks.append(f'<a class="norr">{esc(w["hebrew"])}</a>')
    rs = collections.Counter(w["root"] for w in c["words"] if w["root"])
    tr = "".join(f'<a class="nbi" href="../root/{rslug(rt)}.html"><span class="nb-r" dir="rtl">{esc(rt)}</span>'
                 f'<span class="nb-n">{n}</span></a>' for rt, n in rs.most_common(10))
    rooted = sum(1 for w in c["words"] if w["root"])
    body = (crumb(1, (c["path"][0], None), (c["en"], None)) +
      f'<p class="root" dir="rtl" style="font-size:clamp(26px,5vw,44px)">{esc(c["en"])}</p>'
      f'<p class="gloss">{esc(c["sec"])}</p>'
      f'<p class="stats"><span><b>{len(c["words"]):,}</b> words</span>'
      f'<span><b>{len(rs)}</b> roots</span>'
      f'<span><b>{100.0*rooted/len(c["words"]):.0f}%</b> rooted</span></p>'
      f'<h2>The text</h2><p class="sub">Every word links to its root. Grey words have none resolved.</p>'
      f'<p class="tefillah" dir="rtl">{" ".join(toks)}</p>'
      f'<h2>Its roots</h2><div class="nb">{tr}</div>' + FOOT)
    (OUT/"tefillah"/f"{c['id']}.html").write_text(page(f'{c["en"]} · Siddur Shoresh', body), encoding="utf-8")

# ── arrival ──────────────────────────────────────────────────────────────
run, curve = 0, []
for n in (25, 50, 100, 250, 500, 1000):
    run = sum(x["count"] for x in ranked[:n]); curve.append((n, 100.0*run/TOTAL))
cv = "".join(f'<div class="route"><i></i><b>top {n:,} roots</b><span class="n"></span>'
             f'<span class="c">{p:.0f}%</span></div>' for n, p in curve)
tops = "".join(f'<a class="nbi" href="root/{rslug(r["root"])}.html"><span class="nb-r" dir="rtl">{esc(r["root"])}</span>'
               f'<span class="nb-m">{esc(meaning.get(r["root"],""))[:22]}</span>'
               f'<span class="nb-n">{r["count"]:,}</span></a>' for r in ranked[:24])
books = collections.Counter(c["path"][0] for c in corpus)
bk = "".join(f'<div class="route"><i></i><b>{esc(k)}</b><span class="n">{v} tefillos</span>'
             f'<span class="c">{sum(len(c["words"]) for c in corpus if c["path"][0]==k):,}w</span></div>'
             for k, v in books.most_common())
rooted = sum(1 for c in corpus for w in c["words"] if w["root"])
allw = sum(len(c["words"]) for c in corpus)
body = ('<p class="crumb"><b>Siddur Shoresh</b></p>'
  '<p class="root" dir="rtl" style="font-size:clamp(34px,7vw,62px)">סִדּוּר שׁוֹרֶשׁ</p>'
  '<p class="gloss">The whole davening, by its roots.</p>'
  f'<p class="stats"><span><b>{len(corpus)}</b> tefillos</span><span><b>{allw:,}</b> words</span>'
  f'<span><b>{len(roots):,}</b> roots</span><span><b>{100.0*rooted/allw:.0f}%</b> rooted</span></p>'
  f'<h2>What is here</h2>{bk}'
  '<h2>The curve</h2><p class="sub">A small number of roots carries most of the siddur. '
  'This is why an order exists at all.</p>'+cv+
  '<h2>The roots that carry the most</h2>'+f'<div class="nb">{tops}</div>'+FOOT)
(OUT/"index.html").write_text(page("Siddur Shoresh", body), encoding="utf-8")

json.dump({"tefillos": len(corpus), "words": allw, "roots": len(roots),
           "rooted_pct": round(100.0*rooted/allw, 1),
           "basis": dict(basis_tally), "curve": curve},
          open(OUT/"site.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"  tefillos {len(corpus)}  ·  words {allw:,}  ·  roots {len(roots):,}  ·  rooted {100.0*rooted/allw:.1f}%")
print(f"  pages {1+len(corpus)+len(ranked):,}  ->  {OUT}")
for k, v in basis_tally.most_common(): print(f"    {str(k):16} {v:>7,}")
