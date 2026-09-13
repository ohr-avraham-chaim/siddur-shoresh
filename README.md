# Siddur Shoresh · סידור שורש

**You daven three times a day in a language you can't read.** A translation tells you
what the page means this morning. It doesn't teach you the language, because next
morning you need it again.

Roots do. Learn **מ-ל-כ** once and you own every *melech*, *malchus* and *yimloch* in
the siddur — and the siddur will show you where they all are.

**→ [siddur-shoresh.vercel.app](https://siddur-shoresh.vercel.app)** — no install, no account.

## What it is

Every word of the daily tefillos carries four things:

```json
{ "hebrew": "מֶלֶךְ", "translation": "king",
  "verse": 1,
  "shoresh": { "root": "מ-ל-כ", "root_letters": ["מ","ל","כ"] } }
```

And every root knows every prayer it lives in:

```json
{ "root": "מ-ל-כ", "meaning": "kingship, ruling",
  "prayers": ["Aleinu", "Ashrei", "Asher Yatzar", "Shema Yisrael", "Netilat Yadayim"] }
```

So **ה-ל-ל** (praise) shows up 6 times, and only in Ashrei. **מ-ל-כ** runs through
Aleinu eleven times. That is the shape of the davening, made visible.

## What's in it

| | |
|---|---|
| prayers | **32** |
| words | **2,821** |
| roots | **574** |

Ashrei · Aleinu · Shema · Asher Yatzar · Netilas Yadayim · Birkos HaTorah ·
Birkos HaShachar · Birkas Kohanim · Baruch She'amar · Pesukei D'Zimra · and the rest
of the daily core.

Not the whole siddur. Shemoneh Esrei and Shabbos aren't in yet.

## Running it

It's one HTML file and one JSON file. No build, no dependencies.

```bash
python3 -m http.server 8000     # then open localhost:8000
```

`scripts/` holds the builders that produced `data.json`, one per tefillah, so the
data is reproducible rather than a blob. `docs/` holds the design of the root system.

## Provenance

The Hebrew is the liturgical text. The per-word English glosses and the root analysis
are original to this project — written by hand against traditional translations, not
copied from any edition. The published editions consulted during research
(Metsudah 1981, Ha-Siddur Ha-Shalem 1949, Singer 1915, Sefaria Community, Sha'ar Zahav)
are **not** redistributed here and none of their text appears in `data.json`.

**The Hebrew is the sole authoritative text.** The English here is a learning aid. It
cannot, chas v'shalom, be relied upon for halacha, and a word-gloss is not a translation
of a tefillah.

## Licence

Code (`scripts/`, `index.html`) — **MIT**.
Torah content (`data.json`, `docs/`, `texts/`) — **CC-BY-NC-SA 4.0**.

---

*L'ilui nishmas Avraham Chaim ben David*
