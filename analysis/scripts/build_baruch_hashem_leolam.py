#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build Baruch Hashem LeOlam - Psalms 89:53, 135:21, 72:18-19 (31 words)"""

import json

# Extract from persukei_dezimra_clean.md line 38
baruch_text = """בָּרוּךְ ה' לְעולָם. אָמֵן וְאָמֵן: בָּרוּךְ ה' מִצִּיּון שׁכֵן יְרוּשָׁלָיִם. הַלְלוּיָהּ: בָּרוּךְ ה' אֱלהִים אֱלהֵי יִשרָאֵל. עשה נִפְלָאות לְבַדּו: וּבָרוּךְ שֵׁם כְּבודו לְעולָם. וְיִמָּלֵא כְבודו אֶת כָּל הָאָרֶץ. אָמֵן וְאָמֵן:"""

words = baruch_text.split()
print(f"Total words in Baruch Hashem LeOlam: {len(words)}")

result = {
    "metadata": {
        "name": "Baruch Hashem LeOlam",
        "name_english": "Blessed is Hashem Forever",
        "category": "Pesukei D'Zimra",
        "position": "Concluding blessings",
        "biblical_source": "Psalms 89:53, 135:21, 72:18-19",
        "word_count": len(words)
    },
    "words": {},
    "sentences": []
}

for i, word in enumerate(words, 1):
    result['words'][f'w{i}'] = {'text': word, 'translation': '', 'shoresh': {}}

mappings = {
    1: {"trans": "Blessed", "root": "ב-ר-כ"},
    2: {"trans": "is Hashem", "root": "ה-ו-ה"},
    3: {"trans": "forever", "root": "ע-ל-ם"},
    4: {"trans": "Amen", "root": "א-מ-נ"},
    5: {"trans": "and Amen", "root": "א-מ-נ"},
    6: {"trans": "Blessed", "root": "ב-ר-כ"},
    7: {"trans": "is Hashem", "root": "ה-ו-ה"},
    8: {"trans": "from Zion", "root": "צ-י-ן"},
    9: {"trans": "Who dwells", "root": "ש-כ-נ"},
    10: {"trans": "in Jerusalem", "root": "י-ר-ש"},
    11: {"trans": "Hallelujah", "root": "ה-ל-ל"},
    12: {"trans": "Blessed", "root": "ב-ר-כ"},
    13: {"trans": "is Hashem", "root": "ה-ו-ה"},
    14: {"trans": "God", "root": "א-ל-ה"},
    15: {"trans": "the God of", "root": "א-ל-ה"},
    16: {"trans": "Israel", "root": "י-ש-ר"},
    17: {"trans": "Who does", "root": "ע-ש-ה"},
    18: {"trans": "wonders", "root": "פ-ל-א"},
    19: {"trans": "alone", "root": "ב-ד-ד"},
    20: {"trans": "And blessed", "root": "ב-ר-כ"},
    21: {"trans": "is the name of", "root": "ש-מ-ם"},
    22: {"trans": "His glory", "root": "כ-ב-ד"},
    23: {"trans": "forever", "root": "ע-ל-ם"},
    24: {"trans": "And may be filled", "root": "מ-ל-א"},
    25: {"trans": "His glory", "root": "כ-ב-ד"},
    26: {"trans": "[direct object]", "root": "א-ת-ת"},
    27: {"trans": "all", "root": "כ-ל-ל"},
    28: {"trans": "the earth", "root": "א-ר-ץ"},
    29: {"trans": "Amen", "root": "א-מ-נ"},
    30: {"trans": "and Amen", "root": "א-מ-נ"}
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

with open('data/baruch_hashem_leolam_embedded.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

total = len(words)
completed = sum(1 for w in result['words'].values() if w['translation'])
print(f"Baruch Hashem LeOlam: {completed}/{total} words ({100*completed/total:.1f}%)")
