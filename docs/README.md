# Siddur Prayer Analysis System

**A comprehensive Hebrew prayer analysis system with word-by-word translation and root mapping**

Built by: mordechaipotash@gmail.com
In Memory of Avraham Chaim ben David

---

## 📖 Project Overview

This project provides deep linguistic analysis of Jewish prayers, mapping every word to its Hebrew root (shoresh), providing translations, and tracking patterns across texts. The goal is to transform rote prayer recitation into deep understanding through systematic vocabulary building and pattern recognition.

### Current Status: ✅ Phase 1 Complete

- **12 Complete Texts** - Fully analyzed and documented
- **858 Total Words** - With complete translation and root analysis
- **248 Unique Hebrew Roots** - Identified and cross-referenced
- **100% Completion** - All metrics complete across all texts

---

## 🎯 Core Features

### 1. Word-Level Analysis
Every word includes:
- **Hebrew text** (with vowels/nikud)
- **English translation**
- **Hebrew root** (shoresh) - typically 3 letters
- **Root meaning** and semantic family
- **Word type** (verb, noun, adjective, etc.)
- **Frequency counts** (within-text and cross-text)

### 2. Root Mapping System (Shoresh)
Hebrew roots are the building blocks of vocabulary. Understanding one root unlocks many words:

**Example - Root ב-ר-כ (blessing):**
- בָּרוּךְ (blessed)
- בְּרָכָה (a blessing)
- אֲבָרְכָה (I will bless)
- יְבָרֶכְךָ (may He bless you)

All from 3 letters: **ב-ר-כ**

### 3. Cross-Text Frequency Tracking
See how often each root appears across all prayers:
- **ה-ו-י** (Hashem) - 41 occurrences (most common)
- **כ-ל-ל** (all, every) - 41 occurrences
- **א-ת-ת** (you/direct object) - 39 occurrences
- **א-ל-ה** (God, deity) - 27 occurrences
- **מ-ל-כ** (kingship) - 21 occurrences

### 4. Embedded JSON Format
Each prayer is stored as structured JSON with nested data:
```json
{
  "prayer_name": "Ashrei",
  "total_words": 173,
  "total_verses": 24,
  "words": {
    "w1": {
      "hebrew": "אַשְׁרֵי",
      "translation": "Praiseworthy",
      "shoresh": {
        "root": "א-ש-ר",
        "meaning": "happiness, fortune",
        "word_type": "adjective/interjection"
      },
      "frequency_in_prayer": 3,
      "frequency_across_all": 14
    }
  },
  "root_index": { ... }
}
```

---

## 📚 Completed Texts

### Core Prayers (593 words)

1. **Ashrei** - 173 words (Psalm 145)
   - Focus: Praise and God's works
   - Key root: **ה-ל-ל** (praise) - 6x, unique to Ashrei

2. **Aleinu** - 173 words (Declaration of sovereignty)
   - Focus: Kingship and future redemption
   - Key root: **מ-ל-כ** (kingship) - 11x

3. **Shema** - 247 words (Core declaration of faith)
   - Focus: Hear/Love God, teach children, daily mitzvot
   - Key root: **ש-מ-ע** (hear/listen) - 5x, unique to Shema

### Morning Blessings (107 words)

4. **Netilat Yadayim** - 13 words (Handwashing blessing)
5. **Asher Yatzar** - 46 words (Blessing for body's functioning)
6. **Elohai Neshama** - 48 words (Blessing for the soul)

### Torah Blessings (67 words)

7. **Birkat HaTorah 1** - La'asok B'Divrei Torah (13 words)
8. **Birkat HaTorah 2** - V'Ha'arev Na (34 words)
9. **Birkat HaTorah 3** - Asher Bachar Banu (20 words)

### Torah Study Texts (91 words)

10. **Birkat Kohanim** - Priestly Blessing (33 words)
11. **Eilu Devarim 1** - Things Without Measure (12 words)
12. **Eilu Devarim 2** - Fruits in This World (46 words)

---

## 🔍 Key Insights

### The Blessing Formula

**Standard opening** appears in 8 texts:
```hebrew
בָּרוּךְ אַתָּה ה' אֱלהֵינוּ מֶלֶךְ הָעולָם
```
*"Blessed are You, Hashem our God, King of the universe"*

**7 Core Roots** account for 16% of all words:
1. **ב-ר-כ** (blessed) → 18x
2. **א-ת-ת** (You) → 39x
3. **ה-ו-י** (Hashem) → 41x
4. **א-ל-ה** (our God) → 27x
5. **מ-ל-כ** (King) → 21x
6. **ע-ל-מ** (universe/world) → 16x
7. **א-ש-ר** (Who) → 14x

### Learning Efficiency

- **Top 50 roots** → understand ~60% of all words
- **Top 100 roots** → understand ~80% of all words
- **All 248 roots** → 100% understanding

---

## 🛠️ Technical Stack

### Language & Tools
- **Python 3.9+** - Data processing and analysis
- **JSON** - Structured data storage
- **Markdown** - Documentation and clean text files

### Data Structure
Each prayer has three representations:
1. **Clean markdown** (`clean_ashrei.md`) - Pure Hebrew text
2. **Embedded JSON** (`ashrei_embedded.json`) - Full linguistic data
3. **Source JSON** (from Sefaria API) - Original data

### Key Scripts

**Core Builders:**
- `build_ashrei_embedded.py` - Build Ashrei with full analysis
- `build_aleinu_embedded.py` - Build Aleinu with full analysis
- `build_shema_complete.py` - Build Shema with full analysis
- `build_birkot_hashachar.py` - Build morning blessings
- `build_birkot_hatorah.py` - Build Torah blessings
- `build_morning_texts.py` - Build morning study texts

**Analysis Tools:**
- `add_shoresh.py` - Add root (shoresh) layer to any text
- `complete_all_shoresh.py` - Complete all root mappings
- `update_cross_prayer_frequencies.py` - Update frequency counts
- `analyze_remaining.py` - Analyze completion status

---

## 📁 Project Structure

```
Siddur/
├── README.md                           # This file
├── SIDDUR_PROJECT_ANALYSIS.md         # Vision and design proposals
├── SHORESH_SYSTEM.md                  # Root mapping system documentation
├── COMPLETE_SIDDUR_SUMMARY.md         # Full system summary
│
├── data/                               # Embedded JSON files (12 texts)
│   ├── ashrei_embedded.json
│   ├── aleinu_embedded.json
│   ├── shema_embedded.json
│   ├── netilat_yadayim_embedded.json
│   ├── asher_yatzar_embedded.json
│   ├── elohai_neshama_embedded.json
│   ├── birkat_hatorah_1_laasok_embedded.json
│   ├── birkat_hatorah_2_vhaarev_embedded.json
│   ├── birkat_hatorah_3_asher_bachar_embedded.json
│   ├── birkat_kohanim_embedded.json
│   ├── eilu_devarim_1_embedded.json
│   └── eilu_devarim_2_embedded.json
│
├── scripts/                            # Python analysis scripts (35+)
│   ├── build_*.py                      # Text builders
│   ├── complete_*.py                   # Completion scripts
│   ├── add_*.py                        # Layer addition scripts
│   └── analyze_*.py                    # Analysis scripts
│
├── source_texts/                       # Original Sefaria JSON sources
│
├── *.md                                # Clean Hebrew text files
│   ├── clean_ashrei.md
│   ├── alenu_clean.md
│   ├── shema_clean.md
│   ├── netilat_yadayim_clean.md
│   ├── asher_yatzar_clean.md
│   └── birkot_hatorah_clean.md
│
└── Siddur Ashkenaz - *.json           # Sefaria API downloads (6 translations)
```

---

## 🚀 Usage Examples

### Reading a Prayer's Data

```python
import json

# Load Ashrei with full analysis
with open('data/ashrei_embedded.json', 'r', encoding='utf-8') as f:
    ashrei = json.load(f)

# Get first word
first_word = ashrei['words']['w1']
print(f"Hebrew: {first_word['hebrew']}")
print(f"Translation: {first_word['translation']}")
print(f"Root: {first_word['shoresh']['root']}")
print(f"Root Meaning: {first_word['shoresh']['meaning']}")
```

### Finding All Words from a Root

```python
# Find all words from root ב-ר-כ (blessing)
target_root = "ב-ר-כ"

for word_id, word_data in ashrei['words'].items():
    if word_data['shoresh']['root'] == target_root:
        print(f"{word_data['hebrew']} - {word_data['translation']}")
```

### Cross-Text Root Frequency

Each word includes `frequency_across_all` showing total occurrences across all 12 texts.

---

## 🎓 Educational Applications

### Vocabulary Building Strategy

**Level 1: Blessing Formula**
- Master standard blessing opening (7 roots = 16% of all words)
- Recognize across all 8 blessings

**Level 2: Common Verbs**
Master the 10 most frequent verbs:
- **ה-י-ה** (be/exist)
- **ע-ש-ה** (do/make)
- **נ-ת-נ** (give)
- **א-מ-ר** (say/speak)
- **ד-ב-ר** (speak/word)
- **ב-ר-כ** (bless)
- **ל-מ-ד** (learn/teach)
- **י-ד-ע** (know)
- **ש-מ-ר** (guard/keep)
- **ב-ו-א** (come/enter)

**Level 3: Thematic Vocabulary**
- **Creation**: ב-ר-א, י-צ-ר
- **Torah**: י-ר-ה, ל-מ-ד, ע-ס-ק
- **Holiness**: ק-ד-ש, ב-ר-כ
- **Body/Soul**: נ-ש-מ, נ-ק-ב, ח-ל-ל, ר-פ-א

### Pattern Recognition

**Same Root, Different Forms**

Take root **ב-ר-כ** (blessing):
1. **בָּרוּךְ** - blessed (adjective)
2. **תְבָרְכוּ** - you shall bless (verb, plural)
3. **יְבָרֶכְךָ** - may He bless you (verb, singular)
4. **בְּרָכָה** - a blessing (noun)

All from **ב-ר-כ**!

---

## 📊 Statistics

### Coverage
- **12 texts** fully analyzed
- **858 words** with complete data
- **248 unique roots** identified
- **100% completion** across all metrics

### Most Common Roots (Top 10)
1. **ה-ו-י** (Hashem) - 41x
2. **כ-ל-ל** (all, every) - 41x
3. **א-ת-ת** (you/object) - 39x
4. **א-ל-ה** (God) - 27x
5. **מ-ל-כ** (kingship) - 21x
6. **ע-ל-ל** (upon) - 20x
7. **ב-ר-כ** (blessing) - 18x
8. **ע-ל-מ** (world) - 16x
9. **א-ש-ר** (who/that) - 14x
10. **ד-ב-ר** (word/speak) - 14x

### Text Complexity
**Simplest** (highest uniqueness):
- Eilu Devarim 1: 100% unique roots

**Most Complex** (highest repetition):
- Shema: 40% unique (60% repetition for reinforcement)

---

## 🔮 Future Possibilities

### Additional Prayers
- **Pesukei D'Zimra** (Verses of Praise)
- **Amidah** (Standing Prayer - 19/7 blessings)
- **Kaddish** (multiple versions)
- **Hallel** (6 Psalms)
- **Kabbalat Shabbat**
- **Havdalah**

### Enhanced Layers
- **Grammar Layer**: Binyanim, gender, number, tense, person
- **Kavanah Layer**: Meditative focus, mystical interpretations
- **Cross-Reference Layer**: Biblical sources, Talmudic discussions
- **Audio Layer**: Pronunciation, traditional melodies
- **Visual Layer**: Word clouds, frequency charts, root family trees

### Output Formats
- **PDF Generation**: LaTeX beautiful formatting with interlinear translation
- **Web Interface**: Interactive word lookup and root exploration
- **API**: RESTful API for programmatic access
- **Mobile App**: Prayer study companion

---

## 🎯 Why This System Matters

### Traditional Approach
- Memorize prayers by rote
- Recite without understanding
- Miss deeper patterns and connections

### This System's Approach
- **Understand every word** - complete translations
- **See root patterns** - recognize word families
- **Track frequencies** - learn most important words first
- **Cross-reference** - see connections across prayers
- **Progressive learning** - build vocabulary systematically

### From Rote to Understanding

**Before**: Recite "בָּרוּךְ אַתָּה ה'"

**After**: Understand:
- **בָּרוּךְ** (blessed) from **ב-ר-כ** - appears 18x across system
- **אַתָּה** (You) from **א-ת-ת** - appears 39x across system
- **ה'** (Hashem) from **ה-ו-י** - appears 41x (most common!)

Same 3 words, infinite depth.

---

## 📖 Documentation

### Key Documentation Files
- `SIDDUR_PROJECT_ANALYSIS.md` - Vision, design proposals, and roadmap
- `SHORESH_SYSTEM.md` - Complete root mapping system documentation
- `SHORESH_EXAMPLES.md` - Examples of root usage
- `COMPLETE_SIDDUR_SUMMARY.md` - Full system summary with statistics
- `ASHREI_SYSTEM.md` - Ashrei-specific analysis
- `SHEMA_COMPLETE_SUMMARY.md` - Shema-specific analysis
- `BRACHOT_SUMMARY.md` - Morning blessings analysis
- `PESUKEI_DZIMRA_PLAN.md` - Plan for Verses of Praise expansion

---

## 🤝 Contributing

This is a personal learning project, but contributions are welcome:

1. **Additional Prayers**: Build analysis for new texts
2. **Root Corrections**: Fix or improve root identifications
3. **Translation Refinements**: Suggest better translations
4. **Documentation**: Improve explanations and examples
5. **Tools**: Build visualization or analysis tools

---

## 📜 License

This project is dedicated to the public domain for Torah study and education.

**In Memory of Avraham Chaim ben David**

---

## 🙏 Acknowledgments

- **Sefaria.org** - Source texts and translations
- **Metsudah Linear Siddur** (Avrohom Davis, 1981) - Primary translation source
- **Hebrew Language Academy** - Root identification standards
- **The Jewish community** - Centuries of prayer tradition

---

## 📧 Contact

**Author**: mordechaipotash@gmail.com

For questions, suggestions, or collaboration opportunities.

---

**The journey from one word to complete understanding begins here.**

**מִלָּה אַחַת → הֲבָנָה שְׁלֵמָה**

*One word → Complete understanding*
