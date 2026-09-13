#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build Kaddish - Mourner's Kaddish (~80 words)"""

import json

# Extract from persukei_dezimra_clean.md lines 5-13
kaddish_text = """יִתְגַּדַּל וְיִתְקַדַּשׁ שְׁמֵהּ רַבָּא. בְּעָלְמָא דִּי בְרָא כִרְעוּתֵהּ וְיַמְלִיךְ מַלְכוּתֵהּ בְּחַיֵּיכון וּבְיומֵיכון וּבְחַיֵּי דְכָל בֵּית יִשרָאֵל בַּעֲגָלָא וּבִזְמַן קָרִיב, וְאִמְרוּ אָמֵן: יְהֵא שְׁמֵהּ רַבָּא מְבָרַךְ לְעָלַם וּלְעָלְמֵי עָלְמַיָּא: יִתְבָּרַךְ וְיִשְׁתַּבַּח וְיִתְפָּאַר וְיִתְרומַם וְיִתְנַשּא וְיִתְהַדָּר וְיִתְעַלֶּה וְיִתְהַלָּל שְׁמֵהּ דְּקֻדְשָׁא. בְּרִיךְ הוּא. לְעֵלָּא מִן כָּל בִּרְכָתָא וְשִׁירָתָא תֻּשְׁבְּחָתָא וְנֶחֱמָתָא דַּאֲמִירָן בְּעָלְמָא. וְאִמְרוּ אָמֵן: יְהֵא שְׁלָמָא רַבָּא מִן שְׁמַיָּא וְחַיִּים עָלֵינוּ וְעַל כָּל יִשרָאֵל. וְאִמְרוּ אָמֵן: עושה שָׁלום בִּמְרומָיו הוּא יַעֲשה שָׁלום עָלֵינוּ וְעַל כָּל יִשרָאֵל וְאִמְרוּ אָמֵן:"""

# Split into words
words = kaddish_text.split()
print(f"Total words in Kaddish: {len(words)}")

# Create structure
result = {
    "metadata": {
        "name": "Kaddish",
        "name_english": "Mourner's Kaddish",
        "category": "Pesukei D'Zimra",
        "position": "Opening prayer",
        "language": "Aramaic",
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

# Complete word mappings (Aramaic Kaddish)
mappings = {
    1: {"trans": "May be magnified", "root": "ג-ד-ל"},
    2: {"trans": "and sanctified", "root": "ק-ד-ש"},
    3: {"trans": "His name", "root": "ש-מ-ם"},
    4: {"trans": "great", "root": "ר-ב-ב"},
    5: {"trans": "in the world", "root": "ע-ל-ם"},
    6: {"trans": "which", "root": "ד-י-י"},
    7: {"trans": "He created", "root": "ב-ר-א"},
    8: {"trans": "according to His will", "root": "ר-ע-ה"},
    9: {"trans": "and may He establish", "root": "מ-ל-כ"},
    10: {"trans": "His kingdom", "root": "מ-ל-כ"},
    11: {"trans": "in your lifetime", "root": "ח-י-ה"},
    12: {"trans": "and in your days", "root": "י-ו-ם"},
    13: {"trans": "and in the lifetime of", "root": "ח-י-ה"},
    14: {"trans": "all", "root": "כ-ל-ל"},
    15: {"trans": "the house of", "root": "ב-י-ת"},
    16: {"trans": "Israel", "root": "י-ש-ר"},
    17: {"trans": "speedily", "root": "ע-ג-ל"},
    18: {"trans": "and in a near time", "root": "ז-מ-נ"},
    19: {"trans": "near", "root": "ק-ר-ב"},
    20: {"trans": "and say", "root": "א-מ-ר"},
    21: {"trans": "Amen", "root": "א-מ-נ"},
    22: {"trans": "May be", "root": "ה-י-ה"},
    23: {"trans": "His name", "root": "ש-מ-ם"},
    24: {"trans": "great", "root": "ר-ב-ב"},
    25: {"trans": "blessed", "root": "ב-ר-כ"},
    26: {"trans": "forever", "root": "ע-ל-ם"},
    27: {"trans": "and to the world of", "root": "ע-ל-ם"},
    28: {"trans": "worlds", "root": "ע-ל-ם"},
    29: {"trans": "May be blessed", "root": "ב-ר-כ"},
    30: {"trans": "and praised", "root": "ש-ב-ח"},
    31: {"trans": "and glorified", "root": "פ-א-ר"},
    32: {"trans": "and exalted", "root": "ר-ו-ם"},
    33: {"trans": "and raised", "root": "נ-ש-א"},
    34: {"trans": "and honored", "root": "ה-ד-ר"},
    35: {"trans": "and elevated", "root": "ע-ל-ה"},
    36: {"trans": "and praised", "root": "ה-ל-ל"},
    37: {"trans": "His name", "root": "ש-מ-ם"},
    38: {"trans": "of the Holy One", "root": "ק-ד-ש"},
    39: {"trans": "Blessed", "root": "ב-ר-כ"},
    40: {"trans": "is He", "root": "ה-ו-א"},
    41: {"trans": "beyond", "root": "ע-ל-ה"},
    42: {"trans": "from all", "root": "כ-ל-ל"},
    43: {"trans": "blessings", "root": "ב-ר-כ"},
    44: {"trans": "and songs", "root": "ש-י-ר"},
    45: {"trans": "praises", "root": "ש-ב-ח"},
    46: {"trans": "and consolations", "root": "נ-ח-ם"},
    47: {"trans": "that are uttered", "root": "א-מ-ר"},
    48: {"trans": "in the world", "root": "ע-ל-ם"},
    49: {"trans": "and say", "root": "א-מ-ר"},
    50: {"trans": "Amen", "root": "א-מ-נ"},
    51: {"trans": "May there be", "root": "ה-י-ה"},
    52: {"trans": "peace", "root": "ש-ל-ם"},
    53: {"trans": "great", "root": "ר-ב-ב"},
    54: {"trans": "from", "root": "מ-נ-נ"},
    55: {"trans": "heaven", "root": "ש-מ-ם"},
    56: {"trans": "and life", "root": "ח-י-ה"},
    57: {"trans": "upon us", "root": "ע-ל-ה"},
    58: {"trans": "and upon", "root": "ע-ל-ה"},
    59: {"trans": "all", "root": "כ-ל-ל"},
    60: {"trans": "Israel", "root": "י-ש-ר"},
    61: {"trans": "and say", "root": "א-מ-ר"},
    62: {"trans": "Amen", "root": "א-מ-נ"},
    63: {"trans": "He Who makes", "root": "ע-ש-ה"},
    64: {"trans": "peace", "root": "ש-ל-ם"},
    65: {"trans": "in His heights", "root": "מ-ר-ם"},
    66: {"trans": "He", "root": "ה-ו-א"},
    67: {"trans": "will make", "root": "ע-ש-ה"},
    68: {"trans": "peace", "root": "ש-ל-ם"},
    69: {"trans": "upon us", "root": "ע-ל-ה"},
    70: {"trans": "and upon", "root": "ע-ל-ה"},
    71: {"trans": "all", "root": "כ-ל-ל"},
    72: {"trans": "Israel", "root": "י-ש-ר"},
    73: {"trans": "and say", "root": "א-מ-ר"},
    74: {"trans": "Amen", "root": "א-מ-נ"}
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
            'word_type': 'aramaic'
        }

# Write the file
with open('data/kaddish_embedded.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

# Count completion
total = len(words)
completed = sum(1 for w in result['words'].values() if w['translation'])
print(f"Kaddish: {completed}/{total} words ({100*completed/total:.1f}%)")
