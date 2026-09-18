#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate Phase 3 Completion Report"""

import json
import os

print("=" * 80)
print("PHASE 3 COMPLETION REPORT: SUPPORTING TEXTS")
print("=" * 80)
print()

# Phase 3 files
phase_3_files = [
    ('data/psalm_30_embedded.json', 'Psalm 30 (Mizmor Shir)'),
    ('data/hodu_embedded.json', 'Hodu LaHashem (1 Chronicles 16:8-36)'),
    ('data/verse_compilation_1_embedded.json', 'Verse Compilation 1'),
    ('data/vayevarech_david_embedded.json', 'VaYevarech David (1 Chronicles 29:10-13)')
]

total_words = 0
total_completed = 0

for filepath, name in phase_3_files:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        word_count = data['metadata']['word_count']
        completed = sum(1 for w in data['words'].values() if w['translation'])
        pct = 100 * completed / word_count if word_count else 0

        status = "✓ COMPLETE" if pct == 100 else f"⚠ {pct:.1f}%"
        print(f"{status:15} {name}")
        print(f"              {completed}/{word_count} words")
        print()

        total_words += word_count
        total_completed += completed

print("=" * 80)
print(f"PHASE 3 TOTAL: {total_completed}/{total_words} words ({100*total_completed/total_words:.1f}%)")
print("=" * 80)
print()

# Overall project status
print("=" * 80)
print("OVERALL PROJECT STATUS")
print("=" * 80)
print()

# Count all JSON files in data/
all_files = [f for f in os.listdir('data') if f.endswith('_embedded.json')]
project_total = 0
project_completed = 0

for filename in sorted(all_files):
    filepath = os.path.join('data', filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Handle files with or without metadata
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
print(f"Completion: {100*project_completed/project_total:.1f}%")
print()
print("=" * 80)
