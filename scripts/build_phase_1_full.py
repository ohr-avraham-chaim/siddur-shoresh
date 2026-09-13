#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build Phase 1 of Pesukei D'Zimra: Baruch She'amar, Psalm 100, Yishtabach."""

import json
import re

def parse_hebrew_text(text):
    """Parse Hebrew text into words."""
    return text.split()

# Read source files
print("Loading source files...")
with open('source_texts/pesukei_dzimra/03_baruch_sheamar_clean.md', 'r', encoding='utf-8') as f:
    baruch_text = f.read().split('\n\n')[1]
with open('source_texts/pesukei_dzimra/05_psalm_100_clean.md', 'r', encoding='utf-8') as f:
    psalm100_text = f.read().split('\n\n')[1]
with open('source_texts/pesukei_dzimra/18_yishtabach_clean.md', 'r', encoding='utf-8') as f:
    yishtabach_text = f.read().split('\n\n')[1]

print("Baruch She'amar - building now...")
# Just output the word count for now
print(f"  {len(parse_hebrew_text(baruch_text))} words parsed")
