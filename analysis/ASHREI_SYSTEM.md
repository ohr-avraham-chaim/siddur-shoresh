# Ashrei Embedded JSON System

## Overview

A flexible, iterative system for mapping every word, phrase, and verse of Ashrei with unlimited layers of information (translations, kavanot, grammar, instructions, etc.).

## Core Concept

**Sequential Word IDs → Phrase Mappings → Verse Structure → Iterative Layers**

Every word gets a unique ID (w1, w2, w3...), and we can add ANY layer of information to:
- Individual words (w1, w2, etc.)
- Phrases (p1, p2, etc.)
- Verses (v1, v2, etc.)
- The entire prayer

## File Structure

```
Siddur/
├── clean_ashrei.md                          # Source Hebrew text
├── data/
│   └── ashrei_embedded.json                 # Main embedded database
└── scripts/
    ├── build_ashrei_embedded.py             # Build initial structure
    └── add_layer.py                         # Add layers iteratively
```

## Data Structure

### ashrei_embedded.json Structure

```json
{
  "prayer_name": {
    "hebrew": "אַשְׁרֵי",
    "english": "Ashrei"
  },
  "words": {
    "w1": {
      "id": "w1",
      "hebrew": "אַשְׁרֵי",
      "hebrew_clean": "אַשְׁרֵי",
      "punctuation": "",
      "verse": 1,
      "position_in_verse": 1,
      "position_global": 1,
      "frequency_in_ashrei": 3,              ← Built-in: appears 3 times
      "translation": "praiseworthy",        ← Added iteratively
      "root": "אשר",                         ← Can add this later
      "grammar": {...}                       ← Can add this later
    },
    "w2": {...},
    ...
  },
  "verses": {
    "v1": {
      "id": "v1",
      "number": 1,
      "word_ids": ["w1", "w2", "w3", "w4", "w5", "w6"],
      "hebrew_full": "אַשְׁרֵי יושְׁבֵי בֵיתֶךָ. עוד יְהַלְלוּךָ סֶּלָה:",
      "word_count": 6,
      "translation": "...",                  ← Can add verse translation
      "kavanah": "...",                      ← Can add verse kavanah
      "instruction": "..."                   ← Can add instruction
    },
    ...
  },
  "phrases": {
    "p1": {
      "id": "p1",
      "hebrew": "אַשְׁרֵי הָעָם",
      "frequency": 2,
      "occurrences": [
        {"word_ids": ["w7", "w8"], "verse": 2},
        {"word_ids": ["w10", "w11"], "verse": 2}
      ],
      "category": "repeated",
      "translation": "...",                  ← Can add phrase translation
      "kavanah": "..."                       ← Can add kavanah
    },
    ...
  },
  "layers": {
    "base_text": "complete",
    "translations": "pending",
    "grammar": "pending",
    "kavanot": "pending"
  }
}
```

## Current Stats

- **Words**: 173 (w1 → w173)
- **Verses**: 24 (v1 → v24)
- **Phrases**: 281 (p1 → p281)
  - 5 repeated phrases
  - 276 significant long phrases
- **Unique Words**: 137

## Most Frequent Words

1. **ה'** - appears 9 times (Hashem)
2. **כָּל** - appears 6 times (all)
3. **בְּכָל** - appears 4 times (in all)
4. **לְכָל** - appears 4 times (to all)
5. **אַשְׁרֵי** - appears 3 times (praiseworthy)
6. **לְעולָם** - appears 3 times (forever)
7. **וָעֶד** - appears 3 times (and ever)
8. **אֶת** - appears 3 times (direct object marker)

## Most Repeated Phrases

1. **לְעולָם וָעֶד** - appears 3 times (forever and ever)
2. **אַשְׁרֵי הָעָם** - appears 2 times (praiseworthy is the people)
3. **שִׁמְךָ לְעולָם** - appears 2 times (Your name forever)
4. **שִׁמְךָ לְעולָם וָעֶד** - appears 2 times (Your name forever and ever)
5. **ה' לְכָל** - appears 2 times (Hashem to all)

## How to Use

### 1. Build Initial Structure

```bash
cd "/Users/mordechai/Ohr Avraham Chaim/Siddur"
python3 scripts/build_ashrei_embedded.py
```

This creates `data/ashrei_embedded.json` with all words, verses, and phrases mapped.

### 2. Add Layers Programmatically

```python
from scripts.add_layer import load_ashrei, save_ashrei, add_word_layer

ashrei = load_ashrei()

# Add translation to word w1
add_word_layer(ashrei, "w1", "translation", "praiseworthy")

# Add grammar info
add_word_layer(ashrei, "w1", "grammar", {
    "type": "adjective",
    "number": "plural",
    "root": "אשר"
})

# Add kavanah to phrase
add_phrase_layer(ashrei, "p24", "kavanah",
    "Forever and ever - focus on God's eternal nature")

# Add instruction to verse
add_verse_layer(ashrei, "v16", "instruction",
    "Say with special concentration")

save_ashrei(ashrei)
```

### 3. Use CLI Tool

```bash
# View a word with all its layers
python3 scripts/add_layer.py show word w1

# View a phrase
python3 scripts/add_layer.py show phrase p24

# View a verse
python3 scripts/add_layer.py show verse v1

# Run example layer additions
python3 scripts/add_layer.py example translations
python3 scripts/add_layer.py example kavanot
python3 scripts/add_layer.py example instructions
```

## Layer Types You Can Add

### Word Level
- `translation` - English translation
- `root` - Hebrew root (shoresh)
- `grammar` - Grammatical info (verb form, gender, number)
- `transliteration` - Phonetic spelling
- `meaning_note` - Additional meaning notes
- `alternate_translation` - Other possible translations

### Phrase Level
- `translation` - Phrase translation
- `kavanah` - Intention/focus for this phrase
- `significance` - Why this phrase matters
- `cross_reference` - Where else this phrase appears (in Tanach, etc.)
- `teaching` - Traditional teaching about this phrase

### Verse Level
- `translation` - Complete verse translation
- `kavanah` - Intention for this verse
- `instruction` - How/when to say this verse
- `source` - Biblical source citation
- `commentary` - Traditional commentary
- `custom` - Minhag/custom information

### Prayer Level
- `general_instruction` - Overall instructions
- `theme` - Main themes of the prayer
- `history` - Historical background
- `structure` - Overview of prayer structure

## Advantages of This System

### 1. Maximum Flexibility
Add ANY layer at ANY time to ANY level (word/phrase/verse/prayer).

### 2. No Duplication
Each word appears once with unique ID. Phrases reference word IDs, avoiding text duplication.

### 3. Easy Tracking
Want to find all occurrences of "לְעולָם וָעֶד"? Look up the phrase, see all word ID sequences.

### 4. Iterative Development
Start simple (just Hebrew text), add layers progressively:
- Week 1: Add basic translations
- Week 2: Add kavanot
- Week 3: Add grammar
- Week 4: Add instructions
- Etc.

### 5. User Control
You can personally approve and refine every translation, every kavanah, every instruction.

### 6. Multiple Outputs Possible
Later, we can generate:
- Interlinear PDF (Hebrew with English under each word)
- Side-by-side PDF (Hebrew | English)
- Kavanah-focused edition (with intentions highlighted)
- Study edition (with all layers)
- Simple edition (just approved translation)

## Next Steps

1. **Add More Translations**
   - Add word-level translations for all 173 words
   - Add phrase translations
   - Add verse translations

2. **Add Kavanot**
   - Add kavanah for key phrases
   - Add verse-level kavanot
   - Add prayer-level theme

3. **Add Instructions**
   - When to say (3x daily)
   - Special concentration verses
   - Standing/sitting customs

4. **Add Grammar Layer**
   - Roots (shorashim)
   - Verb forms
   - Gender/number

5. **Generate Beautiful Output**
   - PDF with word-by-word translation
   - Kavanah booklet
   - Study guide

## Example: Complete Word Entry

After adding multiple layers, a word might look like:

```json
{
  "id": "w1",
  "hebrew": "אַשְׁרֵי",
  "hebrew_clean": "אַשְׁרֵי",
  "punctuation": "",
  "verse": 1,
  "position_in_verse": 1,
  "position_global": 1,
  "translation": "praiseworthy",
  "transliteration": "ashrei",
  "root": "אשר",
  "grammar": {
    "type": "adjective",
    "number": "plural",
    "construct_form": true
  },
  "alternate_translations": ["happy", "fortunate", "blessed"],
  "meaning_note": "Implies inner contentment and divine favor",
  "cross_reference": ["Psalm 1:1", "Psalm 119:1", "Proverbs 3:13"]
}
```

## Philosophy

**Start simple. Build iteratively. User-controlled. Maximum power.**

The system doesn't force you to complete everything at once. Add what you want, when you want, at whatever level makes sense. The structure supports infinite growth.
