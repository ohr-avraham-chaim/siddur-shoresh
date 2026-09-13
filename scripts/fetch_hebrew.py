#!/usr/bin/env python3
"""
Fetch the Hebrew for the 18 prayers whose word records shipped empty.

The old records cannot be repaired by a positional join — the word counts
disagree with Sefaria. So we do not join. We take Sefaria's text AS the text,
split it to words, and attach a root only where one can be matched against the
inventory already derived from the intact prayers. Everything else is left
explicitly unresolved rather than guessed.

Writes data/hebrew.json   {pid: {ref, version, license, segments[], words[]}}
"""
import urllib.parse, urllib.request, json, re, os, collections
from pathlib import Path

A   = "https://www.sefaria.org/api"
OUT = Path(os.path.expanduser("~/.claude/jobs/2920a354/tmp/hebrew.json"))
SRC = Path(os.path.expanduser("~/Projects/torah-apps/Siddur/siddur-shoresh/data.json"))
SID = "Siddur Ashkenaz, Weekday, Shacharit, Pesukei Dezimra, "

REFS = {
  "psalm_30":  "Psalms 30",   "psalm_100": "Psalms 100", "psalm_146": "Psalms 146",
  "psalm_147": "Psalms 147",  "psalm_148": "Psalms 148", "psalm_149": "Psalms 149",
  "psalm_150": "Psalms 150",
  "shirat_hayam":        "Exodus 15:1-19",
  "vayoshia":            "Exodus 14:30-31",
  "vayevarech_david":    "I Chronicles 29:10-13",
  "hodu":                "I Chronicles 16:8-36",
  "ata_hu_hashem":       "Nehemiah 9:6-11",
  "baruch_hashem_leolam":"Psalms 89:53",
  "baruch_sheamar":      SID + "Barukh She'amar",
  "yishtabach":          SID + "Yishtabach",
  "verse_compilation_1": SID + "Yehi Chevod",
  "verse_compilation_2": SID + "Closing Verses",
  "kaddish":             "Siddur Ashkenaz, Kaddish, Orphan's Kaddish",
}
PRETTY = {
  "psalm_30":("Psalm 30","מִזְמוֹר שִׁיר חֲנֻכַּת הַבַּיִת"),
  "psalm_100":("Psalm 100 — Mizmor LeTodah","מִזְמוֹר לְתוֹדָה"),
  "psalm_146":("Psalm 146","הַלְלוּיָהּ"),"psalm_147":("Psalm 147","הַלְלוּיָהּ"),
  "psalm_148":("Psalm 148","הַלְלוּיָהּ"),"psalm_149":("Psalm 149","הַלְלוּיָהּ"),
  "psalm_150":("Psalm 150","הַלְלוּיָהּ"),
  "shirat_hayam":("Shirat HaYam — Az Yashir","אָז יָשִׁיר"),
  "vayoshia":("VaYosha","וַיּוֹשַׁע"),
  "vayevarech_david":("VaYevarech David","וַיְבָרֶךְ דָּוִיד"),
  "hodu":("Hodu LaHashem","הוֹדוּ לַיהוה"),
  "ata_hu_hashem":("Atah Hu Hashem","אַתָּה הוּא יהוה"),
  "baruch_hashem_leolam":("Baruch Hashem L'Olam","בָּרוּךְ יהוה לְעוֹלָם"),
  "baruch_sheamar":("Baruch She'amar","בָּרוּךְ שֶׁאָמַר"),
  "yishtabach":("Yishtabach","יִשְׁתַּבַּח"),
  "verse_compilation_1":("Yehi Chevod","יְהִי כְבוֹד"),
  "verse_compilation_2":("Closing Verses","פְּסוּקֵי סִיּוּם"),
  "kaddish":("Kaddish Yatom","קַדִּישׁ יָתוֹם"),
}
NIKUD = re.compile(r"[֑-ׇ]")
def strip(s): return NIKUD.sub("", s or "")
def vocalised(s): return bool(NIKUD.search(s or ""))

def get(url):
    return json.load(urllib.request.urlopen(url, timeout=40))

def fetch(ref):
    q = urllib.parse.quote(ref.replace(" ", "_"), safe="")
    url = f"{A}/texts/{q}?context=0"
    if ref.startswith("Siddur"):
        url += "&vhe=" + urllib.parse.quote("The Metsudah siddur, 1981", safe="")
    d = get(url)
    if not (d.get("he") or []):                       # version may not exist on this node
        d = get(f"{A}/texts/{q}?context=0")
    def flat(x):
        if isinstance(x, str): return [x]
        o = []
        for i in (x or []): o += flat(i)
        return o
    segs = [re.sub("<[^>]+>", "", h).strip() for h in flat(d.get("he"))]
    segs = [s for s in segs if s]
    # a Siddur node prefixes halachic instruction, unvocalised. Drop it.
    voc = [s for s in segs if vocalised(s)]
    if voc: segs = voc                                # drop unvocalised instruction lines
    return segs, d.get("heVersionTitle"), d.get("license")

# ── the root inventory derived from the intact prayers ───────────────────
src = json.load(open(SRC, encoding="utf-8"))
known = {}                       # stripped-root -> meaning
forms = {}                       # stripped surface form -> root
for p in src["prayers"]:
    ws = p.get("words", [])
    if not ws or not all((w.get("hebrew") or "").strip() for w in ws): continue
    for w in ws:
        sh = w.get("shoresh") or {}
        r = strip(sh.get("root") or "")
        if not r: continue
        known.setdefault(r, sh.get("meaning") or "")
        f = strip(w.get("hebrew") or "").strip(".,:;־׃ ")
        if f: forms.setdefault(f, r)

PREF = ["ובש","וכש","ולש","ומש","וה","וב","וכ","ול","ומ","וש","ה","ב","כ","ל","מ","ש","ו"]
SUF  = ["יהם","יכם","נו","הם","כם","יו","יה","ים","ות","ך","כ","ו","י","ם","ן","ה","ת"]

def match_root(word):
    """Exact surface match first (safe). Then affix-stripped match. Else None."""
    w = strip(word).strip(".,:;־׃!?()[]׳״'\" ")
    if not w: return None, None
    if w in forms: return forms[w], "form"
    for p in PREF:
        if w.startswith(p) and len(w) - len(p) >= 3:
            c = w[len(p):]
            if c in forms: return forms[c], "affix"
    for s in SUF:
        if w.endswith(s) and len(w) - len(s) >= 3:
            c = w[:-len(s)]
            if c in forms: return forms[c], "affix"
    for p in PREF:
        for s in SUF:
            if w.startswith(p) and w.endswith(s) and len(w) - len(p) - len(s) >= 3:
                c = w[len(p):-len(s)]
                if c in forms: return forms[c], "affix"
    return None, None

out, report = {}, []
for pid, ref in REFS.items():
    try:
        segs, ver, lic = fetch(ref)
    except Exception as e:
        report.append((pid, ref, "ERR", str(e)[:50])); continue
    words, matched = [], 0
    for si, seg in enumerate(segs, 1):
        for tok in seg.split():
            r, how = match_root(tok)
            if r: matched += 1
            words.append({"hebrew": tok, "verse": si, "root": r, "root_basis": how})
    out[pid] = {"ref": ref, "version": ver, "license": lic,
                "en": PRETTY.get(pid, (pid, ""))[0], "he": PRETTY.get(pid, ("", ""))[1],
                "segments": len(segs), "words": words}
    report.append((pid, ref, f"{len(words)}w", f"{matched} rooted ({100.0*matched/max(len(words),1):.0f}%)"))

json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"  {'prayer':22} {'ref':46} {'words':>7}  roots")
for pid, ref, w, m in report:
    print(f"  {pid:22} {ref[:46]:46} {w:>7}  {m}")
tw = sum(len(v["words"]) for v in out.values())
tm = sum(1 for v in out.values() for w in v["words"] if w["root"])
print(f"\n  {len(out)} prayers · {tw:,} words · {tm:,} rooted ({100.0*tm/max(tw,1):.0f}%) · {tw-tm:,} unresolved")
print(f"  -> {OUT}")
