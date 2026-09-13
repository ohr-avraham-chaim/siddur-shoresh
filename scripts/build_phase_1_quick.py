#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build Phase 1 of Pesukei D'Zimra: Baruch She'amar, Psalm 100, Yishtabach - Quick version."""

import json
import re
from collections import defaultdict

# Read the source files directly
baruch_text = open('source_texts/pesukei_dzimra/03_baruch_sheamar_clean.md', 'r', encoding='utf-8').read().split('\n\n')[1]
psalm100_text = open('source_texts/pesukei_dzimra/05_psalm_100_clean.md', 'r', encoding='utf-8').read().split('\n\n')[1]
yishtabach_text = open('source_texts/pesukei_dzimra/18_yishtabach_clean.md', 'r', encoding='utf-8').read().split('\n\n')[1]

print("="*70)
print("PHASE 1: BUILDING PESUKEI D'ZIMRA FRAMEWORK")
print("="*70)
print(f"\nBaruch She'amar: {len(baruch_text.split())} words")
print(f"Psalm 100: {len(psalm100_text.split())} words")
print(f"Yishtabach: {len(yishtabach_text.split())} words")
print(f"\nTotal Phase 1: {len(baruch_text.split()) + len(psalm100_text.split()) + len(yishtabach_text.split())} words")
print("\n" + "="*70)
print("Ready to build - files loaded successfully!")
