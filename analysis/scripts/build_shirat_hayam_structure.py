#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build Shirat HaYam structure - Song at the Sea (Exodus 15:1-19)"""

import json

# Read line 46 from persukei_dezimra_clean.md
with open('persukei_dezimra_clean.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    shirat_text = lines[45].strip()  # Line 46 (0-indexed)

words = shirat_text.split()
print(f"Total words in Shirat HaYam: {len(words)}")

result = {
    "metadata": {
        "name": "Shirat HaYam",
        "name_english": "Song at the Sea - Exodus 15:1-19",
        "category": "Pesukei D'Zimra",
        "position": "Climax of Pesukei D'Zimra",
        "biblical_source": "Exodus 15:1-19",
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

# Write structure
with open('data/shirat_hayam_embedded.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print(f"Structure created: 0/{len(words)} words mapped")
print("Run complete_shirat_hayam.py to add mappings")
