#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build VaYoshia - Exodus 14:30-31 (34 words)"""

import json

# Extract from persukei_dezimra_clean.md line 44
vayoshia_text = """וַיּושַׁע ה' בַּיּום הַהוּא אֶת יִשרָאֵל מִיַּד מִצְרָיִם. וַיַּרְא יִשרָאֵל אֶת מִצְרַיִם מֵת. עַל שפַת הַיָּם: וַיַּרְא יִשרָאֵל אֶת הַיָּד הַגְּדלָה אֲשֶׁר עָשה ה' בְּמִצְרַיִם. וַיִּירְאוּ הָעָם אֶת ה'. וַיַּאֲמִינוּ בה' וּבְמשֶׁה עַבְדּו:"""

words = vayoshia_text.split()
print(f"Total words in VaYoshia: {len(words)}")

result = {
    "metadata": {
        "name": "VaYoshia",
        "name_english": "And Hashem Saved - Exodus 14:30-31",
        "category": "Pesukei D'Zimra",
        "position": "Introduction to Song at Sea",
        "biblical_source": "Exodus 14:30-31",
        "word_count": len(words)
    },
    "words": {},
    "sentences": []
}

for i, word in enumerate(words, 1):
    result['words'][f'w{i}'] = {'text': word, 'translation': '', 'shoresh': {}}

mappings = {
    1: {"trans": "And saved", "root": "י-ש-ע"},
    2: {"trans": "Hashem", "root": "ה-ו-ה"},
    3: {"trans": "on day", "root": "י-ו-ם"},
    4: {"trans": "that", "root": "ה-ו-א"},
    5: {"trans": "[direct object]", "root": "א-ת-ת"},
    6: {"trans": "Israel", "root": "י-ש-ר"},
    7: {"trans": "from the hand of", "root": "י-ד-ד"},
    8: {"trans": "Egypt", "root": "מ-צ-ר"},
    9: {"trans": "And saw", "root": "ר-א-ה"},
    10: {"trans": "Israel", "root": "י-ש-ר"},
    11: {"trans": "[direct object]", "root": "א-ת-ת"},
    12: {"trans": "Egypt", "root": "מ-צ-ר"},
    13: {"trans": "dead", "root": "מ-ו-ת"},
    14: {"trans": "on", "root": "ע-ל-ל"},
    15: {"trans": "the shore of", "root": "ש-פ-ה"},
    16: {"trans": "the sea", "root": "י-מ-ם"},
    17: {"trans": "And saw", "root": "ר-א-ה"},
    18: {"trans": "Israel", "root": "י-ש-ר"},
    19: {"trans": "[direct object]", "root": "א-ת-ת"},
    20: {"trans": "the hand", "root": "י-ד-ד"},
    21: {"trans": "great", "root": "ג-ד-ל"},
    22: {"trans": "which", "root": "א-ש-ר"},
    23: {"trans": "did", "root": "ע-ש-ה"},
    24: {"trans": "Hashem", "root": "ה-ו-ה"},
    25: {"trans": "against Egypt", "root": "מ-צ-ר"},
    26: {"trans": "And feared", "root": "י-ר-א"},
    27: {"trans": "the people", "root": "ע-מ-ם"},
    28: {"trans": "[direct object]", "root": "א-ת-ת"},
    29: {"trans": "Hashem", "root": "ה-ו-ה"},
    30: {"trans": "And believed", "root": "א-מ-נ"},
    31: {"trans": "in Hashem", "root": "ה-ו-ה"},
    32: {"trans": "and in Moses", "root": "מ-ש-ה"},
    33: {"trans": "His servant", "root": "ע-ב-ד"}
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

with open('data/vayoshia_embedded.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

total = len(words)
completed = sum(1 for w in result['words'].values() if w['translation'])
print(f"VaYoshia: {completed}/{total} words ({100*completed/total:.1f}%)")
