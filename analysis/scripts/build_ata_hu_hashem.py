#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build Ata Hu Hashem - Nehemiah 9:6-11 (118 words)"""

import json

# Read lines 42-43 from persukei_dezimra_clean.md
with open('persukei_dezimra_clean.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    ata_text = (lines[41] + lines[42]).strip()  # Lines 42-43 (0-indexed)

words = ata_text.split()
print(f"Total words in Ata Hu Hashem: {len(words)}")

result = {
    "metadata": {
        "name": "Ata Hu Hashem",
        "name_english": "You Are Hashem - Nehemiah 9:6-11",
        "category": "Pesukei D'Zimra",
        "position": "Historical recollection",
        "biblical_source": "Nehemiah 9:6-11",
        "word_count": len(words)
    },
    "words": {},
    "sentences": []
}

for i, word in enumerate(words, 1):
    result['words'][f'w{i}'] = {'text': word, 'translation': '', 'shoresh': {}}

# Complete mappings for Nehemiah 9:6-11
mappings = {
    1: {"trans": "You", "root": "א-ת-ה"},
    2: {"trans": "are He", "root": "ה-ו-א"},
    3: {"trans": "Hashem", "root": "ה-ו-ה"},
    4: {"trans": "alone", "root": "ב-ד-ד"},
    5: {"trans": "You", "root": "א-ת-ה"},
    6: {"trans": "made", "root": "ע-ש-ה"},
    7: {"trans": "[direct object]", "root": "א-ת-ת"},
    8: {"trans": "the heavens", "root": "ש-מ-ם"},
    9: {"trans": "the heaven of", "root": "ש-מ-ם"},
    10: {"trans": "heavens", "root": "ש-מ-ם"},
    11: {"trans": "and all", "root": "כ-ל-ל"},
    12: {"trans": "their host", "root": "צ-ב-א"},
    13: {"trans": "the earth", "root": "א-ר-ץ"},
    14: {"trans": "and all", "root": "כ-ל-ל"},
    15: {"trans": "that is", "root": "א-ש-ר"},
    16: {"trans": "upon it", "root": "ע-ל-ה"},
    17: {"trans": "the seas", "root": "י-מ-ם"},
    18: {"trans": "and all", "root": "כ-ל-ל"},
    19: {"trans": "that is in them", "root": "ב-ה-ם"},
    20: {"trans": "And You", "root": "א-ת-ה"},
    21: {"trans": "give life", "root": "ח-י-ה"},
    22: {"trans": "[direct object]", "root": "א-ת-ת"},
    23: {"trans": "all of them", "root": "כ-ל-ל"},
    24: {"trans": "And the host of", "root": "צ-ב-א"},
    25: {"trans": "heaven", "root": "ש-מ-ם"},
    26: {"trans": "to You", "root": "ל-כ-כ"},
    27: {"trans": "bow down", "root": "ש-ח-ה"},
    28: {"trans": "You", "root": "א-ת-ה"},
    29: {"trans": "are He", "root": "ה-ו-א"},
    30: {"trans": "Hashem", "root": "ה-ו-ה"},
    31: {"trans": "God", "root": "א-ל-ה"},
    32: {"trans": "Who", "root": "א-ש-ר"},
    33: {"trans": "chose", "root": "ב-ח-ר"},
    34: {"trans": "in Abram", "root": "א-ב-ר"},
    35: {"trans": "And brought him out", "root": "י-צ-א"},
    36: {"trans": "from Ur", "root": "א-ו-ר"},
    37: {"trans": "of the Chaldees", "root": "כ-ש-ד"},
    38: {"trans": "And set", "root": "ש-ו-מ"},
    39: {"trans": "his name", "root": "ש-מ-ם"},
    40: {"trans": "Abraham", "root": "א-ב-ר"},
    41: {"trans": "And found", "root": "מ-צ-א"},
    42: {"trans": "[direct object]", "root": "א-ת-ת"},
    43: {"trans": "his heart", "root": "ל-ב-ב"},
    44: {"trans": "faithful", "root": "א-מ-נ"},
    45: {"trans": "before You", "root": "פ-נ-ה"},
    46: {"trans": "And making", "root": "כ-ר-ת"},
    47: {"trans": "with him", "root": "ע-מ-ם"},
    48: {"trans": "the covenant", "root": "ב-ר-ת"},
    49: {"trans": "to give", "root": "נ-ת-נ"},
    50: {"trans": "[direct object]", "root": "א-ת-ת"},
    51: {"trans": "the land of", "root": "א-ר-ץ"},
    52: {"trans": "the Canaanites", "root": "כ-נ-ע"},
    53: {"trans": "the Hittites", "root": "ח-ת-ת"},
    54: {"trans": "the Amorites", "root": "א-מ-ר"},
    55: {"trans": "and the Perizzites", "root": "פ-ר-ז"},
    56: {"trans": "and the Jebusites", "root": "י-ב-ס"},
    57: {"trans": "and the Girgashites", "root": "ג-ר-ג"},
    58: {"trans": "to give", "root": "נ-ת-נ"},
    59: {"trans": "to his seed", "root": "ז-ר-ע"},
    60: {"trans": "And You fulfilled", "root": "ק-ו-ם"},
    61: {"trans": "[direct object]", "root": "א-ת-ת"},
    62: {"trans": "Your words", "root": "ד-ב-ר"},
    63: {"trans": "for", "root": "כ-י-י"},
    64: {"trans": "righteous", "root": "צ-ד-ק"},
    65: {"trans": "You are", "root": "א-ת-ה"},
    66: {"trans": "And You saw", "root": "ר-א-ה"},
    67: {"trans": "[direct object]", "root": "א-ת-ת"},
    68: {"trans": "the affliction of", "root": "ע-נ-י"},
    69: {"trans": "our forefathers", "root": "א-ב-ב"},
    70: {"trans": "in Egypt", "root": "מ-צ-ר"},
    71: {"trans": "And [direct object]", "root": "א-ת-ת"},
    72: {"trans": "their cry", "root": "ז-ע-ק"},
    73: {"trans": "You heard", "root": "ש-מ-ע"},
    74: {"trans": "at", "root": "ע-ל-ל"},
    75: {"trans": "the Sea of", "root": "י-מ-ם"},
    76: {"trans": "Reeds", "root": "ס-ו-ף"},
    77: {"trans": "And You gave", "root": "נ-ת-נ"},
    78: {"trans": "signs", "root": "א-ו-ת"},
    79: {"trans": "and wonders", "root": "מ-פ-ת"},
    80: {"trans": "against Pharaoh", "root": "פ-ר-ע"},
    81: {"trans": "and against all", "root": "כ-ל-ל"},
    82: {"trans": "his servants", "root": "ע-ב-ד"},
    83: {"trans": "and against all", "root": "כ-ל-ל"},
    84: {"trans": "the people of", "root": "ע-מ-ם"},
    85: {"trans": "his land", "root": "א-ר-ץ"},
    86: {"trans": "For", "root": "כ-י-י"},
    87: {"trans": "You knew", "root": "י-ד-ע"},
    88: {"trans": "that", "root": "כ-י-י"},
    89: {"trans": "they acted wickedly", "root": "ז-י-ד"},
    90: {"trans": "against them", "root": "ע-ל-ה"},
    91: {"trans": "And You made", "root": "ע-ש-ה"},
    92: {"trans": "for Yourself", "root": "ל-כ-כ"},
    93: {"trans": "a name", "root": "ש-מ-ם"},
    94: {"trans": "as it is", "root": "כ-מ-ו"},
    95: {"trans": "this day", "root": "י-ו-ם"},
    96: {"trans": "this", "root": "ז-ה-ה"},
    97: {"trans": "And the sea", "root": "י-מ-ם"},
    98: {"trans": "You split", "root": "ב-ק-ע"},
    99: {"trans": "before them", "root": "פ-נ-ה"},
    100: {"trans": "And they passed", "root": "ע-ב-ר"},
    101: {"trans": "through the midst of", "root": "ת-ו-כ"},
    102: {"trans": "the sea", "root": "י-מ-ם"},
    103: {"trans": "on dry land", "root": "י-ב-ש"},
    104: {"trans": "And [direct object]", "root": "א-ת-ת"},
    105: {"trans": "their pursuers", "root": "ר-ד-ף"},
    106: {"trans": "You threw", "root": "ש-ל-כ"},
    107: {"trans": "into the depths", "root": "צ-ל-ל"},
    108: {"trans": "like", "root": "כ-מ-ו"},
    109: {"trans": "a stone", "root": "א-ב-נ"},
    110: {"trans": "in waters", "root": "מ-י-ם"},
    111: {"trans": "mighty", "root": "ע-ז-ז"}
}

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

with open('data/ata_hu_hashem_embedded.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

total = len(words)
completed = sum(1 for w in result['words'].values() if w['translation'])
print(f"Ata Hu Hashem: {completed}/{total} words ({100*completed/total:.1f}%)")
print(f"Remaining: {total - completed} words")
