#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build VaYevarech David - David's blessing (1 Chronicles 29:10-13) - 56 words"""

import json

# Read the source file
with open('source_texts/pesukei_dzimra/14_vayevarech_david_clean.md', 'r', encoding='utf-8') as f:
    text = f.read().strip().split('\n\n')[1]  # Get Hebrew text after title

# Split into words
words = text.split()
print(f"Total words in VaYevarech David: {len(words)}")

# Create structure
result = {
    "metadata": {
        "name": "VaYevarech David",
        "name_english": "And David Blessed - 1 Chronicles 29:10-13",
        "category": "Pesukei D'Zimra",
        "position": "Supporting texts",
        "biblical_source": "1 Chronicles 29:10-13",
        "word_count": len(words)
    },
    "words": {},
    "sentences": []
}

# Add all words to structure
for i, word in enumerate(words, 1):
    result['words'][f'w{i}'] = {
        'text': word,
        'translation': '',
        'shoresh': {}
    }

# Complete word mappings by ID
mappings = {
    1: {"trans": "And blessed", "root": "ב-ר-כ"},
    2: {"trans": "David", "root": "ד-ו-ד"},
    3: {"trans": "Hashem", "root": "ה-ו-ה"},
    4: {"trans": "before the eyes of", "root": "ע-י-נ"},
    5: {"trans": "all", "root": "כ-ל-ל"},
    6: {"trans": "the congregation", "root": "ק-ה-ל"},
    7: {"trans": "and said", "root": "א-מ-ר"},
    8: {"trans": "David", "root": "ד-ו-ד"},
    9: {"trans": "Blessed", "root": "ב-ר-כ"},
    10: {"trans": "are You", "root": "א-ת-ה"},
    11: {"trans": "Hashem", "root": "ה-ו-ה"},
    12: {"trans": "God of", "root": "א-ל-ה"},
    13: {"trans": "Israel", "root": "י-ש-ר"},
    14: {"trans": "our father", "root": "א-ב-ב"},
    15: {"trans": "from world", "root": "ע-ל-ם"},
    16: {"trans": "to world", "root": "ע-ל-ם"},
    17: {"trans": "Yours", "root": "ל-כ-כ"},
    18: {"trans": "Hashem", "root": "ה-ו-ה"},
    19: {"trans": "is the greatness", "root": "ג-ד-ל"},
    20: {"trans": "and the strength", "root": "ג-ב-ר"},
    21: {"trans": "and the glory", "root": "ת-פ-א"},
    22: {"trans": "and the victory", "root": "נ-צ-ח"},
    23: {"trans": "and the majesty", "root": "ה-ד-ר"},
    24: {"trans": "for", "root": "כ-י-י"},
    25: {"trans": "all", "root": "כ-ל-ל"},
    26: {"trans": "in heaven", "root": "ש-מ-ם"},
    27: {"trans": "and on earth", "root": "א-ר-ץ"},
    28: {"trans": "Yours", "root": "ל-כ-כ"},
    29: {"trans": "Hashem", "root": "ה-ו-ה"},
    30: {"trans": "is the kingdom", "root": "מ-מ-ל"},
    31: {"trans": "and You are exalted", "root": "נ-ש-א"},
    32: {"trans": "as head", "root": "ר-א-ש"},
    33: {"trans": "over all", "root": "כ-ל-ל"},
    34: {"trans": "And the wealth", "root": "ע-ש-ר"},
    35: {"trans": "and the honor", "root": "כ-ב-ד"},
    36: {"trans": "are from You", "root": "פ-נ-ה"},
    37: {"trans": "and You rule", "root": "מ-ש-ל"},
    38: {"trans": "over all", "root": "כ-ל-ל"},
    39: {"trans": "and in Your hand", "root": "י-ד-ד"},
    40: {"trans": "is power", "root": "כ-ח-ח"},
    41: {"trans": "and might", "root": "ג-ב-ר"},
    42: {"trans": "and in Your hand", "root": "י-ד-ד"},
    43: {"trans": "to make great", "root": "ג-ד-ל"},
    44: {"trans": "and to strengthen", "root": "ח-ז-ק"},
    45: {"trans": "all", "root": "כ-ל-ל"},
    46: {"trans": "And now", "root": "ע-ת-ה"},
    47: {"trans": "our God", "root": "א-ל-ה"},
    48: {"trans": "we give thanks", "root": "י-ד-ה"},
    49: {"trans": "to You", "root": "ל-כ-כ"},
    50: {"trans": "and praise", "root": "ה-ל-ל"},
    51: {"trans": "Your name", "root": "ש-מ-ם"},
    52: {"trans": "Your glorious", "root": "ת-פ-א"},
    53: {"trans": "And You", "root": "א-ת-ה"},
    54: {"trans": "rule", "root": "מ-ש-ל"},
    55: {"trans": "over all", "root": "כ-ל-ל"},
    56: {"trans": "and to You", "root": "ל-כ-כ"}
}

# Apply all mappings
for word_id, mapping in mappings.items():
    wid = f"w{word_id}"
    if wid in result['words']:
        result['words'][wid]['translation'] = mapping['trans']
        result['words'][wid]['shoresh'] = {
            'root': mapping['root'],
            'root_letters': list(mapping['root'].split('-')),
            'meaning': mapping['trans'],
            'word_type': 'noun'
        }

# Write the file
with open('data/vayevarech_david_embedded.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

# Count completion
total = len(words)
completed = sum(1 for w in result['words'].values() if w['translation'])
print(f"VaYevarech David: {completed}/{total} words ({100*completed/total:.1f}%)")
