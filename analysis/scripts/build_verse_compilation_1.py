#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build Verse Compilation 1 - Collection of biblical verses (137 words)"""

import json

# Read the source file
with open('source_texts/pesukei_dzimra/11_verse_compilation_1_clean.md', 'r', encoding='utf-8') as f:
    text = f.read().strip().split('\n\n')[1]  # Get Hebrew text after title

# Split into words
words = text.split()
print(f"Total words in Verse Compilation 1: {len(words)}")

# Create structure
result = {
    "metadata": {
        "name": "Verse Compilation 1",
        "name_english": "Collection of Verses",
        "category": "Pesukei D'Zimra",
        "position": "Supporting texts",
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
    1: {"trans": "Blessed", "root": "ב-ר-כ"},
    2: {"trans": "is He", "root": "ה-ו-א"},
    3: {"trans": "our God", "root": "א-ל-ה"},
    4: {"trans": "King of", "root": "מ-ל-כ"},
    5: {"trans": "the world", "root": "ע-ל-ם"},
    6: {"trans": "Who sanctified us", "root": "ק-ד-ש"},
    7: {"trans": "with His commandments", "root": "מ-צ-ו"},
    8: {"trans": "and commanded us", "root": "צ-ו-ה"},
    9: {"trans": "to engage", "root": "ע-ס-ק"},
    10: {"trans": "in words of", "root": "ד-ב-ר"},
    11: {"trans": "Torah", "root": "ת-ו-ר"},
    12: {"trans": "And make pleasant", "root": "ע-ר-ב"},
    13: {"trans": "please", "root": "נ-א-א"},
    14: {"trans": "Hashem", "root": "ה-ו-ה"},
    15: {"trans": "our God", "root": "א-ל-ה"},
    16: {"trans": "the words of", "root": "ד-ב-ר"},
    17: {"trans": "Your Torah", "root": "ת-ו-ר"},
    18: {"trans": "in our mouths", "root": "פ-ה-ה"},
    19: {"trans": "and in the mouths of", "root": "פ-ה-ה"},
    20: {"trans": "Your people", "root": "ע-מ-ם"},
    21: {"trans": "the house of", "root": "ב-י-ת"},
    22: {"trans": "Israel", "root": "י-ש-ר"},
    23: {"trans": "and we shall be", "root": "ה-י-ה"},
    24: {"trans": "we", "root": "א-נ-ח"},
    25: {"trans": "and our offspring", "root": "צ-א-א"},
    26: {"trans": "and the offspring of", "root": "צ-א-א"},
    27: {"trans": "Your people", "root": "ע-מ-ם"},
    28: {"trans": "the house of", "root": "ב-י-ת"},
    29: {"trans": "Israel", "root": "י-ש-ר"},
    30: {"trans": "all of us", "root": "כ-ל-ל"},
    31: {"trans": "knowers of", "root": "י-ד-ע"},
    32: {"trans": "Your name", "root": "ש-מ-ם"},
    33: {"trans": "and students of", "root": "ל-מ-ד"},
    34: {"trans": "Your Torah", "root": "ת-ו-ר"},
    35: {"trans": "for its own sake", "root": "ש-מ-ם"},
    36: {"trans": "Blessed", "root": "ב-ר-כ"},
    37: {"trans": "are You", "root": "א-ת-ה"},
    38: {"trans": "Hashem", "root": "ה-ו-ה"},
    39: {"trans": "Who teaches", "root": "ל-מ-ד"},
    40: {"trans": "Torah", "root": "ת-ו-ר"},
    41: {"trans": "to His people", "root": "ע-מ-ם"},
    42: {"trans": "Israel", "root": "י-ש-ר"},
    43: {"trans": "Master of", "root": "ר-ב-ב"},
    44: {"trans": "the worlds", "root": "ע-ל-ם"},
    45: {"trans": "Who formed us", "root": "י-צ-ר"},
    46: {"trans": "from the womb", "root": "ר-ח-ם"},
    47: {"trans": "and formed us", "root": "י-צ-ר"},
    48: {"trans": "from the womb", "root": "ר-ח-ם"},
    49: {"trans": "Who teaches", "root": "ל-מ-ד"},
    50: {"trans": "Torah", "root": "ת-ו-ר"},
    51: {"trans": "to His people", "root": "ע-מ-ם"},
    52: {"trans": "Israel", "root": "י-ש-ר"},
    53: {"trans": "Blessed", "root": "ב-ר-כ"},
    54: {"trans": "are You", "root": "א-ת-ה"},
    55: {"trans": "Hashem", "root": "ה-ו-ה"},
    56: {"trans": "Who teaches", "root": "ל-מ-ד"},
    57: {"trans": "Torah", "root": "ת-ו-ר"},
    58: {"trans": "to His people", "root": "ע-מ-ם"},
    59: {"trans": "Israel", "root": "י-ש-ר"},
    60: {"trans": "These are the things", "root": "א-ל-ה"},
    61: {"trans": "that have no", "root": "א-י-נ"},
    62: {"trans": "measure", "root": "ש-ע-ר"},
    63: {"trans": "the corner", "root": "פ-א-ה"},
    64: {"trans": "the first fruits", "root": "ב-כ-ר"},
    65: {"trans": "and the appearance", "root": "ר-א-ה"},
    66: {"trans": "and acts of kindness", "root": "ח-ס-ד"},
    67: {"trans": "and the study of", "root": "ת-ל-מ"},
    68: {"trans": "Torah", "root": "ת-ו-ר"},
    69: {"trans": "These are the things", "root": "א-ל-ה"},
    70: {"trans": "that a person", "root": "א-ד-ם"},
    71: {"trans": "eats", "root": "א-כ-ל"},
    72: {"trans": "their fruit", "root": "פ-ר-י"},
    73: {"trans": "in this world", "root": "ע-ל-ם"},
    74: {"trans": "and the principal", "root": "ק-ר-ן"},
    75: {"trans": "remains", "root": "ק-י-ם"},
    76: {"trans": "for him", "root": "ל-ו-ו"},
    77: {"trans": "for the world to come", "root": "ע-ל-ם"},
    78: {"trans": "honoring", "root": "כ-ב-ד"},
    79: {"trans": "father", "root": "א-ב-ב"},
    80: {"trans": "and mother", "root": "א-מ-ם"},
    81: {"trans": "and acts of kindness", "root": "ח-ס-ד"},
    82: {"trans": "and coming early", "root": "ש-כ-ם"},
    83: {"trans": "to the house of study", "root": "מ-ד-ר"},
    84: {"trans": "morning", "root": "ש-ח-ר"},
    85: {"trans": "and evening", "root": "ע-ר-ב"},
    86: {"trans": "and hospitality", "root": "א-ר-ח"},
    87: {"trans": "to guests", "root": "א-ר-ח"},
    88: {"trans": "and visiting", "root": "ב-ק-ר"},
    89: {"trans": "the sick", "root": "ח-ל-ה"},
    90: {"trans": "and providing for", "root": "כ-ל-ה"},
    91: {"trans": "a bride", "root": "כ-ל-ה"},
    92: {"trans": "and escorting", "root": "ל-ו-י"},
    93: {"trans": "the dead", "root": "מ-ו-ת"},
    94: {"trans": "and concentration in", "root": "כ-ו-נ"},
    95: {"trans": "prayer", "root": "פ-ל-ל"},
    96: {"trans": "and making peace", "root": "ש-ל-ם"},
    97: {"trans": "between", "root": "ב-י-נ"},
    98: {"trans": "man", "root": "א-ד-ם"},
    99: {"trans": "and his fellow", "root": "ח-ב-ר"},
    100: {"trans": "and the study of", "root": "ת-ל-מ"},
    101: {"trans": "Torah", "root": "ת-ו-ר"},
    102: {"trans": "is equal to", "root": "כ-נ-ג"},
    103: {"trans": "all of them", "root": "כ-ל-ל"},
    104: {"trans": "Hashem", "root": "ה-ו-ה"},
    105: {"trans": "Hashem", "root": "ה-ו-ה"},
    106: {"trans": "Hashem", "root": "ה-ו-ה"},
    107: {"trans": "God", "root": "א-ל-ל"},
    108: {"trans": "merciful", "root": "ר-ח-ם"},
    109: {"trans": "and gracious", "root": "ח-נ-נ"},
    110: {"trans": "slow", "root": "א-ר-כ"},
    111: {"trans": "to anger", "root": "א-פ-ף"},
    112: {"trans": "and abundant in", "root": "ר-ב-ב"},
    113: {"trans": "kindness", "root": "ח-ס-ד"},
    114: {"trans": "and truth", "root": "א-מ-ת"},
    115: {"trans": "preserver of", "root": "נ-צ-ר"},
    116: {"trans": "kindness", "root": "ח-ס-ד"},
    117: {"trans": "for thousands", "root": "א-ל-ף"},
    118: {"trans": "forgiver of", "root": "נ-ש-א"},
    119: {"trans": "iniquity", "root": "ע-ו-ן"},
    120: {"trans": "and transgression", "root": "פ-ש-ע"},
    121: {"trans": "and sin", "root": "ח-ט-א"},
    122: {"trans": "and Who cleanses", "root": "נ-ק-ה"},
    123: {"trans": "Master of", "root": "ר-ב-ב"},
    124: {"trans": "the world", "root": "ע-ל-ם"},
    125: {"trans": "Master of", "root": "ר-ב-ב"},
    126: {"trans": "the world", "root": "ע-ל-ם"},
    127: {"trans": "King", "root": "מ-ל-כ"},
    128: {"trans": "sitting", "root": "י-ש-ב"},
    129: {"trans": "on", "root": "ע-ל-ל"},
    130: {"trans": "a throne of", "root": "כ-ס-א"},
    131: {"trans": "mercy", "root": "ר-ח-ם"},
    132: {"trans": "He presides", "root": "נ-ה-ג"},
    133: {"trans": "with grace", "root": "ח-ס-ד"},
    134: {"trans": "to forgive", "root": "ס-ל-ח"},
    135: {"trans": "the iniquities of", "root": "ע-ו-ן"},
    136: {"trans": "His people", "root": "ע-מ-ם"},
    137: {"trans": "one by one", "root": "ר-א-ש"}
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
with open('data/verse_compilation_1_embedded.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

# Count completion
total = len(words)
completed = sum(1 for w in result['words'].values() if w['translation'])
print(f"Verse Compilation 1: {completed}/{total} words ({100*completed/total:.1f}%)")
