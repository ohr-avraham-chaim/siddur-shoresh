#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build Verse Compilation 2 - Collection of verses (lines 24-25)"""

import json

# Read lines 24-25 from persukei_dezimra_clean.md
with open('persukei_dezimra_clean.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    verse_text = (lines[23] + lines[24]).strip()  # Lines 24-25 (0-indexed)

words = verse_text.split()
print(f"Total words in Verse Compilation 2: {len(words)}")

result = {
    "metadata": {
        "name": "Verse Compilation 2",
        "name_english": "Collection of Verses - Various Psalms",
        "category": "Pesukei D'Zimra",
        "position": "Supporting texts",
        "word_count": len(words)
    },
    "words": {},
    "sentences": []
}

for i, word in enumerate(words, 1):
    result['words'][f'w{i}'] = {'text': word, 'translation': '', 'shoresh': {}}

# Map all 142 words
mappings = {}
for i in range(1, len(words) + 1):
    word_text = words[i-1]
    # Common mappings based on the verse compilation text
    if word_text in ['ה\'', 'ה\'.', 'ה\':', 'לה\'']:
        mappings[i] = {"trans": "Hashem", "root": "ה-ו-ה"}
    elif word_text in ['לְעולָם', 'לְעולָם.', 'לְעולָם:', 'עולָם', 'עולָם.']:
        mappings[i] = {"trans": "forever", "root": "ע-ל-ם"}
    elif word_text in ['כְּבוד', 'כְבודו', 'כְבודו:']:
        mappings[i] = {"trans": "glory", "root": "כ-ב-ד"}
    elif word_text in ['שֵׁם', 'שִׁמְךָ']:
        mappings[i] = {"trans": "name", "root": "ש-מ-ם"}
    elif word_text in ['הָאָרֶץ', 'הָאָרֶץ.']:
        mappings[i] = {"trans": "the earth", "root": "א-ר-ץ"}
    elif word_text in ['בַּשָּׁמַיִם', 'הַשָּׁמַיִם']:
        mappings[i] = {"trans": "heaven/the heavens", "root": "ש-מ-ם"}
    elif word_text in ['מֶלֶךְ', 'מֶלֶךְ.']:
        mappings[i] = {"trans": "King", "root": "מ-ל-כ"}
    elif word_text in ['מָלָךְ', 'מָלָךְ:', 'מָלָךְ.']:
        mappings[i] = {"trans": "reigns", "root": "מ-ל-כ"}
    elif word_text in ['יִמְלךְ', 'יִמְלךְ:']:
        mappings[i] = {"trans": "will reign", "root": "מ-ל-כ"}
    elif word_text in ['יְהִי', 'יְהִי.']:
        mappings[i] = {"trans": "May be", "root": "ה-י-ה"}
    elif word_text in ['כָּל', 'כָּל.', 'בַּכּל']:
        mappings[i] = {"trans": "all", "root": "כ-ל-ל"}
    elif word_text in ['עַל', 'עַל.']:
        mappings[i] = {"trans": "upon", "root": "ע-ל-ל"}
    elif word_text in ['וָעֶד', 'וָעֶד:', 'וָעֶד.']:
        mappings[i] = {"trans": "and ever", "root": "ע-ד-ד"}

# Add specific mappings for unique words
specific = {
    2: {"trans": "glory of", "root": "כ-ב-ד"},
    5: {"trans": "May rejoice", "root": "ש-מ-ח"},
    7: {"trans": "in His works", "root": "מ-ע-ש"},
    9: {"trans": "the name of", "root": "ש-מ-ם"},
    11: {"trans": "blessed", "root": "ב-ר-כ"},
    12: {"trans": "from now", "root": "ע-ת-ה"},
    13: {"trans": "and until", "root": "ע-ד-ד"},
    15: {"trans": "From the rising of", "root": "מ-ז-ר"},
    16: {"trans": "the sun", "root": "ש-מ-ש"},
    17: {"trans": "until", "root": "ע-ד-ד"},
    18: {"trans": "its setting", "root": "ב-ו-א"},
    19: {"trans": "praised", "root": "ה-ל-ל"},
    20: {"trans": "the name of", "root": "ש-מ-ם"},
    22: {"trans": "High", "root": "ר-ו-ם"},
    25: {"trans": "the nations", "root": "ג-ו-י"},
    32: {"trans": "Your name", "root": "ש-מ-ם"},
    35: {"trans": "Your remembrance", "root": "ז-כ-ר"},
    36: {"trans": "for generation", "root": "ד-ו-ר"},
    37: {"trans": "and generation", "root": "ד-ו-ר"},
    40: {"trans": "prepared", "root": "כ-ו-נ"},
    41: {"trans": "His throne", "root": "כ-ס-א"},
    42: {"trans": "And His kingdom", "root": "מ-ל-כ"},
    44: {"trans": "rules", "root": "מ-ש-ל"},
    45: {"trans": "Let rejoice", "root": "ש-מ-ח"},
    47: {"trans": "and let exult", "root": "ג-י-ל"},
    49: {"trans": "And let them say", "root": "א-מ-ר"},
    50: {"trans": "among the nations", "root": "ג-ו-י"},
    57: {"trans": "Perished", "root": "א-ב-ד"},
    58: {"trans": "nations", "root": "ג-ו-י"},
    59: {"trans": "from His land", "root": "א-ר-ץ"},
    61: {"trans": "frustrated", "root": "פ-ר-ר"},
    62: {"trans": "the counsel of", "root": "ע-צ-ה"},
    63: {"trans": "nations", "root": "ג-ו-י"},
    64: {"trans": "nullified", "root": "נ-ו-א"},
    65: {"trans": "the plans of", "root": "מ-ח-ש"},
    66: {"trans": "peoples", "root": "ע-מ-ם"},
    67: {"trans": "Many", "root": "ר-ב-ב"},
    68: {"trans": "plans", "root": "מ-ח-ש"},
    69: {"trans": "in the heart of", "root": "ל-ב-ב"},
    70: {"trans": "a man", "root": "א-י-ש"},
    71: {"trans": "But the counsel of", "root": "ע-צ-ה"},
    73: {"trans": "it", "root": "ה-י-א"},
    74: {"trans": "will stand", "root": "ק-ו-ם"},
    75: {"trans": "The counsel of", "root": "ע-צ-ה"},
    78: {"trans": "will stand", "root": "ע-מ-ד"},
    79: {"trans": "the plans of", "root": "מ-ח-ש"},
    80: {"trans": "His heart", "root": "ל-ב-ב"},
    81: {"trans": "for generation", "root": "ד-ו-ר"},
    82: {"trans": "and generation", "root": "ד-ו-ר"},
    83: {"trans": "For", "root": "כ-י-י"},
    84: {"trans": "He", "root": "ה-ו-א"},
    85: {"trans": "spoke", "root": "א-מ-ר"},
    86: {"trans": "and it was", "root": "ה-י-ה"},
    87: {"trans": "He", "root": "ה-ו-א"},
    88: {"trans": "commanded", "root": "צ-ו-ה"},
    89: {"trans": "and it stood", "root": "ע-מ-ד"},
    90: {"trans": "For", "root": "כ-י-י"},
    91: {"trans": "chose", "root": "ב-ח-ר"},
    93: {"trans": "Zion", "root": "צ-י-ן"},
    94: {"trans": "He desired it", "root": "א-ו-ה"},
    95: {"trans": "for a dwelling", "root": "מ-ו-ש"},
    96: {"trans": "for Him", "root": "ל-ו-ו"},
    97: {"trans": "For", "root": "כ-י-י"},
    98: {"trans": "Jacob", "root": "י-ע-ק"},
    99: {"trans": "chose", "root": "ב-ח-ר"},
    100: {"trans": "for Himself", "root": "ל-ו-ו"},
    101: {"trans": "God", "root": "י-ה-ה"},
    102: {"trans": "Israel", "root": "י-ש-ר"},
    103: {"trans": "as His treasure", "root": "ס-ג-ל"},
    104: {"trans": "For", "root": "כ-י-י"},
    105: {"trans": "not", "root": "ל-א-א"},
    106: {"trans": "will forsake", "root": "נ-ט-ש"},
    108: {"trans": "His people", "root": "ע-מ-ם"},
    109: {"trans": "And His inheritance", "root": "נ-ח-ל"},
    110: {"trans": "not", "root": "ל-א-א"},
    111: {"trans": "will He abandon", "root": "ע-ז-ב"},
    112: {"trans": "And He", "root": "ה-ו-א"},
    113: {"trans": "the Merciful", "root": "ר-ח-ם"},
    114: {"trans": "atones for", "root": "כ-פ-ר"},
    115: {"trans": "iniquity", "root": "ע-ו-ן"},
    116: {"trans": "and does not", "root": "ל-א-א"},
    117: {"trans": "destroy", "root": "ש-ח-ת"},
    118: {"trans": "And He increases", "root": "ר-ב-ה"},
    119: {"trans": "to turn back", "root": "ש-ו-ב"},
    120: {"trans": "His anger", "root": "א-פ-ף"},
    121: {"trans": "And does not", "root": "ל-א-א"},
    122: {"trans": "stir up", "root": "ע-ו-ר"},
    124: {"trans": "His wrath", "root": "ח-מ-ה"},
    126: {"trans": "save", "root": "י-ש-ע"},
    127: {"trans": "The King", "root": "מ-ל-כ"},
    128: {"trans": "will answer us", "root": "ע-נ-ה"},
    129: {"trans": "on the day of", "root": "י-ו-ם"},
    130: {"trans": "our calling", "root": "ק-ר-א"}
}

mappings.update(specific)

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

with open('data/verse_compilation_2_embedded.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

total = len(words)
completed = sum(1 for w in result['words'].values() if w['translation'])
print(f"Verse Compilation 2: {completed}/{total} words ({100*completed/total:.1f}%)")
print(f"Remaining: {total - completed} words")
