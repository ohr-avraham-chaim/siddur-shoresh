#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Final Comprehensive Pesukei D'Zimra Completion Report"""

import json
import os

print("=" * 80)
print("PESUKEI D'ZIMRA CLEAN.MD - FINAL COMPLETION REPORT")
print("=" * 80)
print()

# All texts in persukei_dezimra_clean.md in order
pesukei_texts = [
    ('psalm_30', 'Line 3: Mizmor Shir (Psalm 30)'),
    ('kaddish', 'Lines 5-13: Kaddish'),
    ('baruch_sheamar', 'Line 15: Baruch She\'amar'),
    ('hodu', 'Lines 17-18: Hodu LaHashem'),
    ('verse_compilation_1', 'Lines 19-20: Verse Compilation 1'),
    ('psalm_100', 'Line 22: Mizmor LeTodah (Psalm 100)'),
    ('verse_compilation_2', 'Lines 24-25: Verse Compilation 2'),
    ('ashrei', 'Line 26: Ashrei (Psalm 145)'),
    ('psalm_146', 'Line 28: Psalm 146'),
    ('psalm_147', 'Line 30: Psalm 147'),
    ('psalm_148', 'Line 32: Psalm 148'),
    ('psalm_149', 'Line 34: Psalm 149'),
    ('psalm_150', 'Line 36: Psalm 150'),
    ('baruch_hashem_leolam', 'Line 38: Baruch Hashem LeOlam'),
    ('vayevarech_david', 'Line 40: VaYevarech David'),
    ('ata_hu_hashem', 'Lines 42-43: Ata Hu Hashem (Nehemiah 9:6-11)'),
    ('vayoshia', 'Line 44: VaYoshia (Exodus 14:30-31)'),
    ('shirat_hayam', 'Line 46: Shirat HaYam (Exodus 15:1-19)'),
    ('yishtabach', 'Line 48: Yishtabach')
]

total_words = 0
found_count = 0
missing = []

print("ALL TEXTS FROM PERSUKEI_DEZIMRA_CLEAN.MD:")
print("-" * 80)

for name, desc in pesukei_texts:
    filepath = f'data/{name}_embedded.json'
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if 'metadata' in data and 'word_count' in data['metadata']:
            word_count = data['metadata']['word_count']
        else:
            word_count = len(data.get('words', {}))

        completed = sum(1 for w in data.get('words', {}).values() if w.get('translation'))
        pct = 100 * completed / word_count if word_count else 0

        if pct == 100:
            print(f"✓ {desc:55} {word_count:4} words")
            total_words += word_count
            found_count += 1
        else:
            print(f"⚠ {desc:55} {word_count:4} words ({pct:.1f}%)")
            total_words += word_count
            missing.append((name, desc, word_count - completed))
    else:
        print(f"✗ {desc:55} NOT FOUND")
        missing.append((name, desc, 0))

print()
print("=" * 80)
print(f"PESUKEI D'ZIMRA CLEAN.MD COMPLETION:")
print("-" * 80)
print(f"Texts completed: {found_count}/{len(pesukei_texts)}")
print(f"Total words: {total_words}")
print(f"Completion: {100*found_count/len(pesukei_texts):.1f}%")

if missing:
    print()
    print("MISSING/INCOMPLETE:")
    for name, desc, words in missing:
        print(f"  - {desc}: {words} words remaining")
else:
    print()
    print("🎉 ALL TEXTS FROM PERSUKEI_DEZIMRA_CLEAN.MD ARE COMPLETE! 🎉")

print()
print("=" * 80)
print("OVERALL SIDDUR PROJECT STATUS:")
print("-" * 80)

# Count all JSON files
all_files = [f for f in os.listdir('data') if f.endswith('_embedded.json')]
project_total = 0
project_completed = 0

for filename in sorted(all_files):
    filepath = os.path.join('data', filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if 'metadata' in data and 'word_count' in data['metadata']:
        word_count = data['metadata']['word_count']
    else:
        word_count = len(data.get('words', {}))

    completed = sum(1 for w in data.get('words', {}).values() if w.get('translation'))

    project_total += word_count
    project_completed += completed

print(f"Total JSON files: {len(all_files)}")
print(f"Total words across all files: {project_total}")
print(f"Completed words: {project_completed}")
print(f"Overall completion: {100*project_completed/project_total:.1f}%")
print()
print("=" * 80)
