# Ohr Avraham Chaim - Presentation Script

**Professional Repository Walkthrough**

---

## Opening (30 seconds)

Hi everyone! Today I'm excited to show you **Ohr Avraham Chaim** – a collection of tools I've built to make Torah learning accessible and deeply meaningful.

**Quick context**: I love learning Torah in its original Hebrew, but as someone who's dyslexic, traditional study methods have always been challenging. When ChatGPT came out, I realized I could use AI and programming to build a bridge between authentic Hebrew texts and deep comprehension.

That's what this repository is all about.

---

## Part 1: The Torah Text Publishing System (2-3 minutes)

### Overview

The first major project here is **bilingual Torah text publishing** – taking classical Hebrew texts and creating beautiful, professional PDFs with side-by-side Hebrew and English.

Let me show you how it works.

### Technology Stack

**Data Source**: Sefaria.org API
- Open-source database with Torah texts in JSON format
- Includes original Hebrew and metadata

**Translation**: Gemini Flash 2.5 Lite via OpenRouter
- Nearly free: $0.10–$0.40 per million tokens
- High-quality translation that preserves meaning
- Why not use Sefaria's English? Their translations are good, but I wanted control over consistency and style

**Typesetting**: LaTeX + XeLaTeX
- Professional book-quality layout
- Handles Hebrew (right-to-left) and English (left-to-right)
- Custom fonts: Arial Hebrew Scholar, Helvetica Neue

### The Tur & Mefarshim Project

Let me show you a concrete example. *[Navigate to `tur and mefarshim/` directory]*

This project focuses on **Shulchan Aruch** (Jewish legal code) and its classical commentaries.

Here's what the system does:

1. **Fetches** the Hebrew text from Sefaria API (JSON)
2. **Translates** using Gemini AI
3. **Organizes** the text: main text + all major commentaries
4. **Typesets** using LaTeX with custom macros
5. **Compiles** to a beautiful PDF

**Time**: About 2-5 minutes per *siman* (section) from start to finish.

### Example Output: Siman 3

*[Open PDF: `build/Siman_3.pdf`]*

This is **Siman 3** – the laws of bathroom conduct. Let me walk you through the layout:

**Page Structure:**
- **Hebrew first, then English** – always this pattern
- **Tur** (14th-century code) at the top
- **Commentaries inline** below each section:
  - Bach (1561-1640)
  - Darkhei Moshe
  - Beit Yosef
  - Perisha
- **Shulchan Aruch** (1563) follows with its commentaries:
  - Mishnah Berurah (1907) – the main modern commentary
  - Magen Avraham
  - Taz
  - Be'er HaGra
  - And more

**Why This Format Matters:**
- Everything is **organized and accessible**
- I can finally learn these texts deeply for the first time
- The side-by-side layout lets me check the Hebrew while understanding the English
- Designed for **printing and studying**, not just digital reading

**Current Status**: ~50 *simanim* completed and compiled.

---

## Part 2: The Siddur Prayer Analysis System (3-4 minutes)

### The Problem

Traditional prayer is often rote recitation without understanding. You say the words, but do you know what each word *means*? Where it comes from? How it connects to other prayers?

For someone dyslexic like me who struggles with Hebrew fluency, this gap between recitation and comprehension has always been frustrating.

### The Solution: Deep Linguistic Analysis

I built a system that analyzes every single word in the Jewish prayer book (siddur) at a granular level.

Let me show you. *[Navigate to `Siddur/` directory]*

### How It Works

**Input**: Prayer text from Sefaria (JSON)

**Processing**: Python scripts that extract and analyze:
1. **Hebrew word** with vowel points (nikud)
2. **English translation**
3. **Shoresh** (Hebrew root) – usually 3 letters
4. **Root meaning** and semantic family
5. **Word type** (verb, noun, adjective, etc.)
6. **Frequency tracking**:
   - Within this specific prayer
   - Across all prayers in the system

**Output**: Structured JSON with complete linguistic data

### Example: Netilat Yadayim (Handwashing Blessing)

*[Open: `data/netilat_yadayim_embedded.json`]*

Let me show you one word in detail – **בָּרוּךְ** (baruch – "blessed"):

```json
{
  "hebrew": "בָּרוּךְ",
  "hebrew_clean": "ברוך",
  "translation": "Blessed",
  "position_global": 1,
  "frequency_in_prayer": 1,
  "shoresh": {
    "root": "ב-ר-כ",
    "meaning": "blessing, benediction",
    "word_type": "adjective"
  },
  "frequency_across_all": 18
}
```

**What This Tells Me:**
- The word is **blessed** (translation)
- It comes from the root **ב-ר-כ** (bet-resh-kaf)
- That root means **blessing**
- This root appears **18 times** across all the prayers I've analyzed
- In this specific prayer, it appears **once**

### The Power of Root Mapping (Shoresh)

Here's where it gets really cool.

**Hebrew roots are 3-letter building blocks.** Once you understand one root, you unlock an entire family of words.

**Example: Root ב-ר-כ (blessing)**
- **בָּרוּךְ** – blessed (adjective)
- **בְּרָכָה** – a blessing (noun)
- **יְבָרֶכְךָ** – may He bless you (verb)
- **אֲבָרְכָה** – I will bless (verb, first person)

All from the same 3 letters: **ב-ר-כ**

**Learning Efficiency:**
- Master the **top 50 roots** → understand ~60% of prayer words
- Master the **top 100 roots** → understand ~80% of prayer words
- Master all **248 roots** in my system → 100% understanding

### Current Status

**12 Complete Texts:**
1. Ashrei (173 words)
2. Aleinu (173 words)
3. Shema (247 words)
4. 6 morning blessings
5. 3 Torah blessings

**Statistics:**
- **858 total words** analyzed
- **248 unique Hebrew roots** identified
- **100% completion** – every word has full data

**Most Common Roots:**
1. **ה-ו-י** (Hashem) – 41 occurrences
2. **כ-ל-ל** (all, every) – 41 occurrences
3. **א-ת-ת** (you) – 39 occurrences
4. **א-ל-ה** (God) – 27 occurrences
5. **מ-ל-כ** (kingship) – 21 occurrences

### Real-World Impact

**Before this system:**
- I would recite prayers by rote
- Struggled to understand what I was saying
- Missed patterns and connections

**After this system:**
- I understand **every single word**
- I see how words connect through roots
- I recognize patterns across different prayers
- Learning feels **systematic and achievable** instead of overwhelming

---

## Part 3: Other Projects (1 minute)

Beyond these two main projects, I've also built similar systems for:

**Derech Hashem** (The Way of God)
- Classic philosophical text by Rabbi Moshe Chaim Luzzatto
- Same translation + typesetting pipeline

**Gevurot Hashem** (The Mighty Acts of God)
- Maharal of Prague's work
- Bilingual PDF generation

**Nefesh HaChaim** (The Soul of Life)
- Rabbi Chaim of Volozhin
- Currently: Gate I complete (22 chapters, 54-page PDF)

**Plus**: Audio transcription pipeline for Torah lectures
- Download MP3s from YouTube
- Transcribe locally (30-50× faster than realtime)
- Vectorize and store for searchable learning

---

## Technical Philosophy (1 minute)

### Core Principles

**Evidence Over Assumptions**
- All translation verified, all data structured
- No guesswork, everything traceable

**Automation Where It Matters**
- Python for data wrangling
- Makefiles for build automation
- LaTeX for professional typesetting

**Open Source Foundation**
- Sefaria API for texts
- Gemini for affordable AI translation
- LaTeX for reproducible publishing

**Systematic Learning**
- Frequency tracking guides learning priorities
- Root mapping builds vocabulary systematically
- Cross-referencing reveals patterns

### Why These Tools Matter

Traditional Torah learning has a **high barrier to entry**:
- Need to know Hebrew fluently
- Need to navigate dense commentary
- Hard to see connections across texts

These tools **lower the barrier** while **raising the depth**:
- Hebrew + English side-by-side
- Every word explained and tracked
- Patterns made visible through data

**Result**: Deep, meaningful learning that's accessible to anyone willing to put in the effort.

---

## Closing (30 seconds)

This repository represents hundreds of hours of work, but every minute has been worth it.

**For the first time in my life**, I can:
- Learn Torah texts deeply in their original form
- Understand every word of my daily prayers
- See patterns and connections I never knew existed

If you're interested in Torah learning, accessible education, or the intersection of AI and ancient texts, I hope this inspires you.

**In Memory of Avraham Chaim ben David**

Thank you for watching!

---

## Q&A Preparation

### Anticipated Questions

**Q: Why not just use existing translations?**
A: Existing translations are good, but I wanted:
- Consistency across all texts
- Control over style and vocabulary
- The ability to customize for my learning needs

**Q: How accurate is Gemini translation?**
A: Very accurate for Hebrew→English. I spot-check against scholarly translations, and the quality is comparable to professional human translation. The cost savings (nearly free) make it practical to translate everything.

**Q: Can others use this?**
A: Absolutely! The code is in the repository. The main requirement is:
- Python 3.9+
- OpenRouter API key (for Gemini)
- LaTeX installation (for PDF generation)

**Q: What's next?**
A: For Siddur: Expand to full daily prayers (Amidah, Pesukei D'Zimra, Kaddish)
For Tur: Complete Orach Chayim (all 697 sections)
Future: Web interface for interactive prayer study

**Q: How long did this take?**
A: The Tur system: ~2 months of development, now automated
The Siddur system: ~3 months of iterative development
Both are ongoing projects I continue to refine

---

## Technical Deep Dive (Bonus Content)

### Tur Pipeline

```bash
# Fetch data from Sefaria API
make fetch-range SIMAN_START=1 SIMAN_END=50

# Translate with Gemini
# (happens automatically during fetch with 1.5s rate limit delay)

# Generate LaTeX
make generate-range SIMAN_START=1 SIMAN_END=50

# Compile to PDF
make compile SIMAN=3
```

**Output**: `build/Siman_3.pdf` (24 pages, professional quality)

### Siddur Pipeline

```bash
# Fetch prayer from Sefaria
python3 scripts/fetch_prayer.py "Ashrei"

# Build embedded JSON with full analysis
python3 scripts/build_ashrei_embedded.py

# Add root (shoresh) layer
python3 scripts/add_shoresh.py ashrei

# Update cross-prayer frequencies
python3 scripts/update_cross_prayer_frequencies.py
```

**Output**: `data/ashrei_embedded.json` (173 words, complete linguistic data)

### Key Technologies

**Python Libraries:**
- `requests` – Sefaria API calls
- `json` – Data manipulation
- `time` – Rate limiting

**LaTeX Packages:**
- `polyglossia` – Hebrew/English support
- `fontspec` – Custom font selection
- `geometry` – Page layout
- `fancyhdr` – Headers/footers

**AI Integration:**
- OpenRouter API
- Gemini Flash 2.5 Lite model
- Cost: ~$0.10-0.40 per million tokens

---

## Repository Statistics

**Total Files:** ~200+
**Lines of Python:** ~5,000+
**LaTeX Templates:** ~10 custom macros
**PDFs Generated:** ~50 (Tur) + 12 (other projects)
**JSON Data Files:** ~100+
**Total Words Analyzed:** 858 (Siddur)
**Unique Roots Identified:** 248

**Development Time:** ~6 months (ongoing)
**Cost to Run:** ~$5-10 total (mostly Gemini API)

---

**End of Presentation Script**
