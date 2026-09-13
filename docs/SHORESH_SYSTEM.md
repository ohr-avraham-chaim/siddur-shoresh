# Hebrew Root (Shoresh) System for Siddur Project

## What is a Shoresh?

A **shoresh** (שורש) is the root of a Hebrew word - typically 3 letters that carry the core meaning. All Hebrew words (with rare exceptions) are built from these roots using patterns, vowels, and affixes.

## Why Add Roots to Our System?

### Educational Benefits
1. **Pattern Recognition**: See how the same root appears in different forms
2. **Vocabulary Building**: Learn one root = understand many words
3. **Deeper Understanding**: Connect related concepts in prayers

### Practical Uses
1. **Cross-Reference**: Find all words from same root in siddur
2. **Etymology**: Understand word origins and relationships
3. **Grammar Learning**: Study binyanim (verb patterns) systematically

## Root Structure in Our JSON

### Individual Word Level

```json
{
  "id": "w1",
  "hebrew": "מֶלֶךְ",
  "hebrew_clean": "מֶלֶךְ",
  "translation": "king",
  "frequency_in_prayer": 3,
  "shoresh": {
    "root": "מ-ל-כ",
    "root_letters": ["מ", "ל", "כ"],
    "meaning": "kingship, ruling",
    "word_type": "noun",
    "pattern": "פֶּעֶל",
    "notes": "Basic noun form"
  }
}
```

### Root Index (Prayer-Level)

Add a new top-level section to each prayer JSON:

```json
{
  "prayer_name": {...},
  "words": {...},
  "verses": {...},
  "root_index": {
    "מ-ל-כ": {
      "meaning": "kingship, ruling",
      "frequency": 8,
      "word_forms": [
        {"word_id": "w38", "form": "מֶלֶךְ", "type": "noun"},
        {"word_id": "w61", "form": "מַלְכֵּנוּ", "type": "noun with suffix"},
        {"word_id": "w81", "form": "מַלְכוּתְךָ", "type": "noun"},
        {"word_id": "w95", "form": "מַלְכוּת", "type": "noun"},
        {"word_id": "w130", "form": "מַלְכוּתֶךָ", "type": "noun"},
        {"word_id": "w131", "form": "וְתִמְלךְ", "type": "verb"}
      ],
      "appears_in_verses": [3, 13, 15, 23],
      "related_roots": ["ש-ל-ט" (rule), "כ-ס-א" (throne)]
    },
    "ב-ר-כ": {
      "meaning": "blessing",
      "frequency": 5,
      "word_forms": [...]
    }
  }
}
```

## Common Roots in Ashrei

### Most Frequent Roots in Ashrei

1. **מ-ל-כ** (kingship) - appears 8+ times
   - מֶלֶךְ, מַלְכוּת, מַלְכוּתְךָ, etc.

2. **ב-ר-כ** (blessing) - appears 5+ times
   - אֲבָרְכָה, בָּרוּךְ, יְבָרְכוּכָה

3. **ה-ל-ל** (praise) - appears 4+ times
   - תְּהִלָּה, יְהַלְלוּךָ, אֲהַלְלָה

4. **ע-ש-ה** (doing/making) - appears 4+ times
   - מַעֲשֶׂיךָ, מַעֲשָׂיו, יַעֲשֶׂה

5. **ק-ד-שׁ** (holiness) - appears 2+ times
   - הַקָּדוֹשׁ, קָדְשׁוֹ

## Common Roots in Aleinu

1. **מ-ל-כ** (kingship) - heavily featured
   - מֶלֶךְ, מַלְכֵּי, הַמְּלָכִים, מַלְכוּת, תִּמְלֹךְ

2. **ש-ח-ה** (bowing) - appears 3 times
   - מִשְׁתַּחֲוִים, וּמִשְׁתַּחֲוִים

3. **י-ד-ע** (knowing) - appears 3 times
   - וְיָדַעְתָּ, יֵדְעוּ

4. **ק-ר-א** (calling) - appears 2+ times
   - יִקְרְאוּ, קֹרְאָיו

## Implementation Strategy

### Phase 1: Core Roots
Start with the 20 most common roots that appear in multiple prayers:
- מ-ל-כ, ב-ר-כ, ק-ד-שׁ, ה-ל-ל, ע-ש-ה, י-ד-ע, etc.

### Phase 2: Manual Entry
For Ashrei & Aleinu, manually add roots to each word (educational - learn as you go)

### Phase 3: Automated Detection
Build a script to suggest roots based on:
- Common patterns
- Prefix/suffix removal
- Known root dictionary

### Phase 4: Validation
Review automated suggestions, correct weak roots and irregular forms

## Root Categories

### Regular Roots (פעל שלם)
All 3 letters appear clearly: מ-ל-כ, ב-ר-כ, ק-ד-שׁ

### Weak Roots (פעל חסר)
One or more letters may disappear:
- **פ"נ** (first letter נ): נ-ת-ן → נוֹתֵן
- **פ"י** (first letter י): י-ד-ע → יוֹדֵעַ
- **ל"ה** (last letter ה): ע-ש-ה → עֹשֶׂה
- **ל"י** (last letter י): ב-נ-י → בּוֹנֶה

### Doubled Roots (פעל כפול)
Middle letter doubles: ס-ב-ב → סוֹבֵב

### Four-Letter Roots (רבועי)
Less common: ת-ר-ג-ם (translate)

## Example: Adding Roots to First 10 Words of Ashrei

```json
{
  "w1": {
    "hebrew": "אַשְׁרֵי",
    "translation": "Praiseworthy",
    "shoresh": {
      "root": "א-ש-ר",
      "meaning": "happiness, fortune",
      "word_type": "adjective/interjection",
      "pattern": "פַּעְלֵי",
      "notes": "Construct plural form expressing praise"
    }
  },
  "w2": {
    "hebrew": "יושְׁבֵי",
    "translation": "those who dwell",
    "shoresh": {
      "root": "י-ש-ב",
      "meaning": "sitting, dwelling",
      "word_type": "verb - participle",
      "pattern": "קוֹטְלֵי",
      "binyan": "Kal",
      "notes": "Present tense active participle, construct form"
    }
  },
  "w5": {
    "hebrew": "יְהַלְלוּךָ",
    "translation": "they will praise You",
    "shoresh": {
      "root": "ה-ל-ל",
      "meaning": "praise, glory",
      "word_type": "verb",
      "pattern": "פִּעֵל",
      "binyan": "Piel",
      "tense": "future",
      "person": "third person plural",
      "suffix": "ך - You",
      "notes": "Piel intensifies the action of praising"
    }
  }
}
```

## Benefits of Root Tracking

### For Learning
- "I see **ה-ל-ל** 4 times in Ashrei - all about praise!"
- "**מ-ל-כ** appears in both paragraphs of Aleinu - kingship is central"

### For Cross-Reference
- Find all words from root **ב-ר-כ** across entire siddur
- Track how different binyanim of same root are used

### For Translation
- Understand nuances: Why **בָּרוּךְ** vs **אֲבָרְכָה**?
- Both from **ב-ר-כ** but different patterns = different meanings

### For Kavanah
- When you see **מֶלֶךְ**, **מַלְכוּת**, **יִמְלֹךְ** - all connect to God's sovereignty
- Root awareness deepens prayer focus

## Tools We'll Need

1. **Root Dictionary**: Map of 1500+ common Hebrew roots with meanings
2. **Pattern Recognition**: Identify binyanim (Kal, Piel, Hifil, etc.)
3. **Affix Stripper**: Remove prefixes (ב,כ,ל,מ,ש,ה,ו) and suffixes
4. **Weak Root Handler**: Special logic for נ,י,ה disappearing letters
5. **Validation Interface**: Let you approve/correct suggested roots

## Next Steps

1. Create root dictionary JSON with common roots
2. Build helper script to add roots to words
3. Start with Ashrei - manually add roots to learn the system
4. Build automated root detector for remaining prayers
5. Generate root-based study materials and cross-references
