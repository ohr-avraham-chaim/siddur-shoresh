#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Analyze what remains to be built from persukei_dezimra_clean.md"""

import json
import os

# What we have built
built_texts = {
    'psalm_30': 'Line 3: Mizmor Shir (Psalm 30)',
    'baruch_sheamar': 'Line 15: Baruch She\'amar',
    'hodu': 'Line 17-18: Hodu LaHashem',
    'verse_compilation_1': 'Line 19-20: Verse Compilation 1',
    'psalm_100': 'Line 22: Mizmor LeTodah (Psalm 100)',
    'ashrei': 'Line 26: Ashrei/Psalm 145',
    'psalm_146': 'Line 28: Psalm 146',
    'psalm_147': 'Line 30: Psalm 147',
    'psalm_148': 'Line 32: Psalm 148',
    'psalm_149': 'Line 34: Psalm 149',
    'psalm_150': 'Line 36: Psalm 150',
    'vayevarech_david': 'Line 40: VaYevarech David',
    'yishtabach': 'Line 48: Yishtabach'
}

# What's in the file but NOT built yet
missing_texts = {
    'kaddish': {
        'line': 5,
        'text': 'Kaddish (lines 5-13)',
        'estimated_words': 80
    },
    'verse_compilation_2': {
        'line': 24,
        'text': 'Verse Compilation 2 (lines 24-25)',
        'estimated_words': 150
    },
    'baruch_hashem_leolam': {
        'line': 38,
        'text': 'Baruch Hashem LeOlam (line 38)',
        'estimated_words': 45
    },
    'ata_hu_hashem': {
        'line': 42,
        'text': 'Ata Hu Hashem/Nehemiah 9 (lines 42-43)',
        'estimated_words': 185
    },
    'vayoshia': {
        'line': 44,
        'text': 'VaYoshia (line 44)',
        'estimated_words': 33
    },
    'shirat_hayam': {
        'line': 46,
        'text': 'Shirat HaYam/Az Yashir (line 46)',
        'estimated_words': 237
    }
}

print("=" * 80)
print("PESUKEI D'ZIMRA COMPLETION ANALYSIS")
print("=" * 80)
print()

print("BUILT TEXTS (13 total):")
print("-" * 80)
for name, desc in built_texts.items():
    filepath = f'data/{name}_embedded.json'
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if 'metadata' in data and 'word_count' in data['metadata']:
            word_count = data['metadata']['word_count']
        else:
            word_count = len(data.get('words', {}))
        print(f"✓ {desc:50} {word_count:4} words")
    else:
        print(f"⚠ {desc:50} NOT FOUND")

print()
print("=" * 80)
print("MISSING TEXTS FROM PERSUKEI_DEZIMRA_CLEAN.MD:")
print("=" * 80)

total_missing_words = 0
for name, info in missing_texts.items():
    print(f"✗ {info['text']:50} ~{info['estimated_words']:4} words")
    total_missing_words += info['estimated_words']

print()
print("=" * 80)
print(f"TOTAL MISSING: {total_missing_words} words estimated")
print("=" * 80)
print()

# Calculate current completion
built_count = 0
for name in built_texts.keys():
    filepath = f'data/{name}_embedded.json'
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if 'metadata' in data and 'word_count' in data['metadata']:
            word_count = data['metadata']['word_count']
        else:
            word_count = len(data.get('words', {}))
        built_count += word_count

total_pesukei_words = built_count + total_missing_words
completion_pct = (built_count / total_pesukei_words) * 100

print("COMPLETION STATUS:")
print(f"Built: {built_count} words")
print(f"Remaining: {total_missing_words} words")
print(f"Total Pesukei D'Zimra: {total_pesukei_words} words")
print(f"Completion: {completion_pct:.1f}%")
print()
print("=" * 80)
