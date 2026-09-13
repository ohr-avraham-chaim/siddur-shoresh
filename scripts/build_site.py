#!/usr/bin/env python3
"""
Siddur Shoresh — static site generator.

Reads data.json, keeps only prayers whose every word carries Hebrew (the
62% hollow ones are excluded and reported, not silently rendered), and emits:

    index.html                 one arrival — the route, not a directory
    root/<slug>.html           one page per root: footprint, forms, neighbours
    tefillah/<id>.html         one page per prayer: text, every word linked
    data/site.json             the computed graph

Links are lateral and inline. No page lists the others. The topology is
emergent from the edges.
"""
import json, os, re, shutil, collections, html
from pathlib import Path

SRC  = Path(os.path.expanduser("~/Projects/torah-apps/Siddur/siddur-shoresh/data.json"))
OUT  = Path(os.path.expanduser("~/.claude/jobs/2920a354/tmp/siddur-site"))

# ── names for the prayers whose name dict shipped empty ──────────────────
NAMES = {
 "birkot_hashachar": ("Birkot HaShachar", "בִּרְכוֹת הַשַּׁחַר"),
 "yehi_ratzon":      ("Yehi Ratzon",       "וִיהִי רָצוֹן"),
 "elohai_neshama":   ("Elohai Neshama",    "אֱלֹהַי נְשָׁמָה"),
 "birkat_kohanim":   ("Birkat Kohanim",    "בִּרְכַּת כֹּהֲנִים"),
 "eilu_devarim_1":   ("Eilu Devarim — Ein Lahem Shiur", "אֵלּוּ דְבָרִים שֶׁאֵין לָהֶם שִׁעוּר"),
 "eilu_devarim_2":   ("Eilu Devarim — Peiroteihem",     "אֵלּוּ דְבָרִים שֶׁאָדָם אוֹכֵל"),
}
# the order a person says them
ORDER = ["netilat_yadayim","asher_yatzar","elohai_neshama","birkot_hashachar",
         "birkat_hatorah_1_laasok","birkat_hatorah_2_vhaarev","birkat_hatorah_3_asher_bachar",
         "birkat_kohanim","eilu_devarim_1","eilu_devarim_2","yehi_ratzon",
         "ashrei","shema","aleinu"]

TRANS = {"א":"a","ב":"b","ג":"g","ד":"d","ה":"h","ו":"v","ז":"z","ח":"ch","ט":"t",
         "י":"y","כ":"k","ך":"k","ל":"l","מ":"m","ם":"m","נ":"n","ן":"n","ס":"s",
         "ע":"o","פ":"p","ף":"p","צ":"tz","ץ":"tz","ק":"q","ר":"r","ש":"sh","ת":"th"}

NIKUD = re.compile(r"[֑-ׇ]")      # nikud, te'amim, and the shin/sin dots

def norm_root(root):
    """ק-ד-שׁ and ק-ד-ש are the same root written two ways. Strip the points."""
    return NIKUD.sub("", root or "").strip()

def slug(root):
    return "-".join(TRANS.get(c, "") for c in norm_root(root) if c in TRANS) or "x"

def esc(s): return html.escape(str(s or ""))

# ── load + filter ────────────────────────────────────────────────────────
d = json.load(open(SRC, encoding="utf-8"))
prayers, hollow = {}, []
for p in d["prayers"]:
    pid = p.get("id"); ws = p.get("words", [])
    if not ws: continue
    if all((w.get("hebrew") or "").strip() for w in ws):
        n = p.get("name") or {}
        en = (n.get("english") if isinstance(n, dict) else n) or NAMES.get(pid, (pid, ""))[0]
        he = (n.get("hebrew")  if isinstance(n, dict) else "") or NAMES.get(pid, ("", ""))[1]
        prayers[pid] = {"id": pid, "en": en, "he": he, "words": ws}
    else:
        hollow.append((pid, len(ws)))

order = [p for p in ORDER if p in prayers] + [p for p in prayers if p not in ORDER]

# ── the graph ────────────────────────────────────────────────────────────
roots = {}                                   # root -> {meaning, count, by_prayer, forms}
for pid in order:
    for w in prayers[pid]["words"]:
        sh = w.get("shoresh") or {}
        r  = norm_root(sh.get("root"))
        if not r: continue
        e = roots.setdefault(r, {"root": r, "meaning": sh.get("meaning") or "",
                                 "count": 0, "by_prayer": collections.Counter(), "forms": {}})
        e["count"] += 1
        e["by_prayer"][pid] += 1
        heb = (w.get("hebrew") or "").strip()
        if heb and heb not in e["forms"]:
            e["forms"][heb] = {"he": heb, "en": w.get("translation") or "", "in": pid}
        if not e["meaning"] and sh.get("meaning"): e["meaning"] = sh["meaning"]

TOTAL = sum(r["count"] for r in roots.values())
ranked = sorted(roots.values(), key=lambda r: -r["count"])
for i, r in enumerate(ranked, 1): r["rank"] = i

# co-occurrence: roots sharing a prayer, weighted
neigh = collections.defaultdict(collections.Counter)
for pid in order:
    rs = {norm_root((w.get("shoresh") or {}).get("root")) for w in prayers[pid]["words"]}
    rs = {x for x in rs if x}
    for a in rs:
        for b in rs:
            if a != b: neigh[a][b] += 1

# prayer -> prayer: knowing A, what % of B's words are familiar
proots = {pid: [norm_root((w.get("shoresh") or {}).get("root")) for w in prayers[pid]["words"]] for pid in order}
proots = {k: [r for r in v if r] for k, v in proots.items()}
def familiarity(a, b):
    ra = set(proots[a]); wb = proots[b]
    return 100.0 * sum(1 for r in wb if r in ra) / len(wb) if wb else 0.0

# greedy route
def route():
    known, out, cov, rem = set(), [], 0, dict(proots)
    while rem:
        best = max(rem.items(), key=lambda kv: sum(
            1 for pr in proots.values() for r in pr if r in (set(kv[1]) - known)))
        name, rs = best
        new = set(rs) - known
        gain = sum(1 for pr in proots.values() for r in pr if r in new)
        known |= new; cov += gain
        out.append((name, len(rs), len(new), 100.0 * cov / TOTAL))
        del rem[name]
    return out
ROUTE = route()

# root-coverage curve
def curve():
    run, out = 0, []
    for n in (10, 25, 50, 100, 200, len(ranked)):
        run = sum(r["count"] for r in ranked[:n])
        out.append((n, 100.0 * run / TOTAL))
    return out
CURVE = curve()

# ── rendering ────────────────────────────────────────────────────────────
CSS = """
:root{--paper:#FDFCF8;--ink:#1B1A17;--ink-soft:#57544D;--ink-faint:#948F85;
--rule:#E7E3D8;--rule-soft:#F1EEE5;--tech:#2B4C7E;--tech-wash:#E9EEF5;}
*{box-sizing:border-box}html{color-scheme:light}
body{background:var(--paper);color:var(--ink);font-family:"IBM Plex Sans",system-ui,sans-serif;
margin:0;padding:clamp(22px,5vw,58px) clamp(16px,5vw,38px) 88px;line-height:1.5;-webkit-font-smoothing:antialiased}
.sheet{max-width:880px;margin:0 auto}
a{color:inherit;text-decoration:none}
a.lnk{color:var(--tech);border-bottom:1px solid transparent}
a.lnk:hover{border-bottom-color:var(--tech)}
.crumb{font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--ink-faint);
font-weight:600;margin:0 0 26px;display:flex;gap:9px;flex-wrap:wrap}
.crumb a{color:var(--ink-soft)} .crumb a:hover{color:var(--tech)} .crumb i{color:var(--rule);font-style:normal}
.root{font-family:"Frank Ruhl Libre",Georgia,serif;direction:rtl;font-size:clamp(48px,10vw,86px);
font-weight:700;line-height:.95;letter-spacing:.06em;margin:0}
.gloss{font-family:"Frank Ruhl Libre",Georgia,serif;font-size:clamp(18px,2.5vw,23px);
color:var(--ink-soft);margin:6px 0 0}
.stats{font-family:"IBM Plex Mono",monospace;font-size:12.5px;color:var(--ink-soft);
margin:22px 0 0;padding:14px 0 0;border-top:1px solid var(--rule);display:flex;gap:24px;
flex-wrap:wrap;font-variant-numeric:tabular-nums}
.stats b{color:var(--ink);font-weight:500}
h2{font-size:11px;letter-spacing:.15em;text-transform:uppercase;color:var(--ink-faint);
font-weight:600;margin:52px 0 4px}
.sub{font-size:13.5px;color:var(--ink-soft);margin:0 0 20px;max-width:60ch}
.fp-row{display:grid;grid-template-columns:186px 1fr 34px;gap:14px;align-items:center;
padding:7px 0;border-bottom:1px solid var(--rule-soft)}
.fp-row:last-child{border-bottom:none}
.fp-name{font-size:13.5px;color:var(--ink-soft)} .fp-name.none{color:var(--ink-faint)}
.fp-track{display:flex;gap:3px;height:16px;flex-wrap:wrap}
.tick{width:7px;height:16px;background:var(--tech);border-radius:1px}
.tick.ghost{background:var(--rule);height:5px;align-self:center}
.fp-n{font-family:"IBM Plex Mono",monospace;font-size:12px;color:var(--ink-soft);
text-align:right;font-variant-numeric:tabular-nums}
.fp-n.zero{color:var(--rule)}
.form{display:grid;grid-template-columns:minmax(120px,auto) 1fr 150px;gap:18px;align-items:baseline;
padding:12px 0;border-bottom:1px solid var(--rule-soft)}
.f-he{font-family:"Frank Ruhl Libre",Georgia,serif;direction:rtl;font-size:25px;font-weight:500;line-height:1.35}
.f-en{font-size:14.5px} .f-where{font-size:12.5px}
.nb{display:flex;gap:9px;flex-wrap:wrap}
.nbi{display:flex;align-items:baseline;gap:9px;padding:10px 15px;background:var(--tech-wash);border-radius:2px}
.nb-r{font-family:"Frank Ruhl Libre",Georgia,serif;direction:rtl;font-size:19px;font-weight:500}
.nb-m{font-size:12.5px;color:var(--ink-soft)} .nb-n{font-family:"IBM Plex Mono",monospace;font-size:11.5px;color:var(--ink-faint)}
.tefillah{font-family:"Frank Ruhl Libre",Georgia,serif;direction:rtl;text-align:right;
font-size:clamp(21px,3vw,27px);line-height:2.15;margin:6px 0 0}
.tefillah a{border-bottom:1px solid var(--rule)}
.tefillah a:hover{border-bottom-color:var(--tech);color:var(--tech)}
.tefillah a.norr{border-bottom:none;color:var(--ink-faint)}
.route{display:grid;grid-template-columns:26px 1fr 76px 84px;gap:12px;align-items:baseline;
padding:10px 0;border-bottom:1px solid var(--rule-soft);font-size:14px}
.route i{font-family:"IBM Plex Mono",monospace;color:var(--ink-faint);font-style:normal;font-size:12px}
.route b{font-weight:400}
.route .n{font-family:"IBM Plex Mono",monospace;font-size:12px;color:var(--ink-soft);
text-align:right;font-variant-numeric:tabular-nums}
.route .c{font-family:"IBM Plex Mono",monospace;font-size:12.5px;color:var(--tech);
text-align:right;font-variant-numeric:tabular-nums}
.unlock{display:flex;gap:8px;flex-wrap:wrap;margin-top:4px}
.ul{padding:9px 14px;background:var(--tech-wash);border-radius:2px;font-size:13px}
.ul b{font-family:"IBM Plex Mono",monospace;font-size:12px;color:var(--tech);font-weight:500}
footer{margin-top:60px;padding-top:17px;border-top:1px solid var(--rule);
font-size:11.5px;color:var(--ink-faint);line-height:1.65}
@media(max-width:660px){.form{grid-template-columns:1fr;gap:2px}.fp-row{grid-template-columns:118px 1fr 30px;gap:9px}
.route{grid-template-columns:22px 1fr 66px;gap:8px}.route .c{grid-column:3;text-align:right}}
"""

HEAD = """<title>{title}</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Frank+Ruhl+Libre:wght@400;500;700&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>{css}</style>
"""

def page(title, body, depth=0):
    up = "../" * depth
    return HEAD.format(title=esc(title), css=CSS) + f'<div class="sheet">{body}</div>'

def crumb(depth, *parts):
    up = "../" * depth
    out = [f'<a href="{up}index.html">Siddur Shoresh</a>']
    for label, href in parts:
        out.append("<i>/</i>")
        out.append(f'<a href="{up}{href}">{esc(label)}</a>' if href else esc(label))
    return '<p class="crumb">' + "".join(out) + "</p>"

FOOT = ('<footer>Built from the 14 tefillos whose every word carries Hebrew — '
        '1,067 words, 280 roots. Eighteen further prayers in the source data hold roots '
        'but no Hebrew text and are deliberately excluded rather than rendered blank. '
        'Hebrew set in Frank Ruhl Libre. Grammatical forms shown as they occur, not parsed.</footer>')

# ── root pages ───────────────────────────────────────────────────────────
(OUT / "root").mkdir(parents=True, exist_ok=True)
(OUT / "tefillah").mkdir(parents=True, exist_ok=True)

for r in ranked:
    s = slug(r["root"])
    fp = []
    for pid in order:
        n = r["by_prayer"].get(pid, 0)
        ticks = "".join('<i class="tick"></i>' for _ in range(min(n, 40))) or \
                '<i class="tick ghost"></i><i class="tick ghost"></i><i class="tick ghost"></i>'
        fp.append(
            f'<div class="fp-row"><span class="fp-name{"" if n else " none"}">'
            f'<a class="lnk" href="../tefillah/{pid}.html">{esc(prayers[pid]["en"])}</a></span>'
            f'<span class="fp-track">{ticks}</span>'
            f'<span class="fp-n{"" if n else " zero"}">{n or "—"}</span></div>')
    forms = "".join(
        f'<div class="form"><span class="f-he" dir="rtl">{esc(f["he"])}</span>'
        f'<span class="f-en">{esc(f["en"])}</span>'
        f'<span class="f-where"><a class="lnk" href="../tefillah/{f["in"]}.html">{esc(prayers[f["in"]]["en"])}</a></span></div>'
        for f in list(r["forms"].values())[:24])
    nb = "".join(
        f'<a class="nbi" href="{slug(b)}.html"><span class="nb-r" dir="rtl">{esc(b)}</span>'
        f'<span class="nb-m">{esc(roots[b]["meaning"])[:26]}</span>'
        f'<span class="nb-n">{roots[b]["count"]}</span></a>'
        for b, _ in neigh[r["root"]].most_common(6))
    body = (
      crumb(1, ("roots", None), (r["root"], None)) +
      f'<p class="root" dir="rtl">{esc(r["root"])}</p>'
      f'<p class="gloss">{esc(r["meaning"] or "—")}</p>'
      f'<p class="stats"><span><b>{r["count"]}</b> words</span>'
      f'<span><b>{len(r["forms"])}</b> distinct forms</span>'
      f'<span><b>{sum(1 for v in r["by_prayer"].values() if v)}</b> tefillos</span>'
      f'<span><b>{100.0*r["count"]/TOTAL:.1f}%</b> of the corpus</span>'
      f'<span>rank <b>#{r["rank"]}</b></span></p>'
      f'<h2>Footprint</h2><p class="sub">Where this root lives across the morning, in the order you say it.</p>'
      + "".join(fp) +
      f'<h2>Seen in {len(r["forms"])} shape{"s" if len(r["forms"])!=1 else ""}</h2>'
      f'<p class="sub">One root doing several jobs. Reading down this column is how a root is actually acquired.</p>'
      + forms +
      (f'<h2>Keeps company with</h2><p class="sub">Roots that share a tefillah with this one.</p><div class="nb">{nb}</div>' if nb else "")
      + FOOT)
    (OUT / "root" / f"{s}.html").write_text(page(f'{r["root"]} · Siddur Shoresh', body), encoding="utf-8")

# ── tefillah pages ───────────────────────────────────────────────────────
for pid in order:
    p = prayers[pid]
    toks = []
    for w in p["words"]:
        heb = (w.get("hebrew") or "").strip()
        rt  = norm_root((w.get("shoresh") or {}).get("root"))
        if rt and rt in roots:
            toks.append(f'<a href="../root/{slug(rt)}.html" title="{esc(rt)} — {esc(w.get("translation"))}">{esc(heb)}</a>')
        else:
            toks.append(f'<a class="norr" title="{esc(w.get("translation"))}">{esc(heb)}</a>')
    unlock = sorted(((familiarity(pid, b), b) for b in order if b != pid), reverse=True)[:4]
    ul = "".join(f'<a class="ul" href="{b}.html">{esc(prayers[b]["en"])} <b>{v:.0f}%</b></a>' for v, b in unlock)
    top = collections.Counter(r for r in proots[pid]).most_common(8)
    tr = "".join(f'<a class="nbi" href="../root/{slug(rt)}.html"><span class="nb-r" dir="rtl">{esc(rt)}</span>'
                 f'<span class="nb-m">{esc(roots[rt]["meaning"])[:24]}</span><span class="nb-n">{n}</span></a>'
                 for rt, n in top)
    body = (
      crumb(1, ("tefillos", None), (p["en"], None)) +
      f'<p class="root" dir="rtl" style="font-size:clamp(30px,6vw,54px)">{esc(p["he"] or p["en"])}</p>'
      f'<p class="gloss">{esc(p["en"])}</p>'
      f'<p class="stats"><span><b>{len(p["words"])}</b> words</span>'
      f'<span><b>{len(set(proots[pid]))}</b> distinct roots</span></p>'
      f'<h2>The text</h2><p class="sub">Every word links to its root. Words with no root yet resolved are greyed.</p>'
      f'<p class="tefillah" dir="rtl">{" ".join(toks)}</p>'
      f'<h2>Its roots</h2><div class="nb">{tr}</div>'
      f'<h2>Knowing this one</h2><p class="sub">How much of another tefillah becomes familiar once you know this one.</p>'
      f'<div class="unlock">{ul}</div>' + FOOT)
    (OUT / "tefillah" / f"{pid}.html").write_text(page(f'{p["en"]} · Siddur Shoresh', body), encoding="utf-8")

# ── the one arrival ──────────────────────────────────────────────────────
rt_rows = "".join(
    f'<div class="route"><i>{i}</i><b><a class="lnk" href="tefillah/{n}.html">{esc(prayers[n]["en"])}</a></b>'
    f'<span class="n">{nr} new</span><span class="c">{cov:.0f}%</span></div>'
    for i, (n, w, nr, cov) in enumerate(ROUTE[:8], 1))
top_roots = "".join(
    f'<a class="nbi" href="root/{slug(r["root"])}.html"><span class="nb-r" dir="rtl">{esc(r["root"])}</span>'
    f'<span class="nb-m">{esc(r["meaning"])[:24]}</span><span class="nb-n">{r["count"]}</span></a>'
    for r in ranked[:12])
curve_rows = "".join(f'<div class="route"><i></i><b>top {n} roots</b><span class="n"></span>'
                     f'<span class="c">{pct:.0f}%</span></div>' for n, pct in CURVE[:5])
body = (
  '<p class="crumb"><b>Siddur Shoresh</b></p>'
  '<p class="root" dir="rtl" style="font-size:clamp(38px,8vw,68px)">סִדּוּר שׁוֹרֶשׁ</p>'
  '<p class="gloss">Learn the davening by its roots, not by its translation.</p>'
  f'<p class="stats"><span><b>{len(prayers)}</b> tefillos</span><span><b>{TOTAL:,}</b> words</span>'
  f'<span><b>{len(roots)}</b> roots</span></p>'
  '<h2>Where to start</h2>'
  '<p class="sub">Learn these in this order and each one carries the most new ground. '
  'The percentage is how much of the whole corpus has become familiar by then.</p>'
  + rt_rows +
  '<h2>The curve</h2><p class="sub">A small number of roots carries most of the davening. This is why an order exists at all.</p>'
  + curve_rows +
  '<h2>The roots that carry the most</h2>' + f'<div class="nb">{top_roots}</div>'
  + FOOT)
(OUT / "index.html").write_text(page("Siddur Shoresh", body), encoding="utf-8")

json.dump({"prayers": {k: {"en": v["en"], "he": v["he"], "words": len(v["words"])} for k, v in prayers.items()},
           "roots": {r["root"]: {"meaning": r["meaning"], "count": r["count"], "rank": r["rank"],
                                 "slug": slug(r["root"])} for r in ranked},
           "route": ROUTE, "curve": CURVE, "excluded_hollow": hollow},
          open(OUT / "site.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

print(f"  prayers rendered : {len(prayers)}")
print(f"  roots rendered   : {len(ranked)}")
print(f"  hollow excluded  : {len(hollow)} prayers / {sum(n for _,n in hollow):,} words")
print(f"  pages            : {1 + len(prayers) + len(ranked)}")
print(f"  out              : {OUT}")
