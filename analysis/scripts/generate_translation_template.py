#!/usr/bin/env python3
"""
Generate a complete translation template from the actual Ashrei JSON.
Shows all unique words that need translation.
"""

import json
from pathlib import Path

def load_ashrei():
    path = Path('/Users/mordechai/Ohr Avraham Chaim/Siddur/data/ashrei_embedded.json')
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def generate_template():
    ashrei = load_ashrei()

    # Collect all unique words with their first occurrence
    unique_words = {}

    for word_id, word_data in ashrei["words"].items():
        hebrew = word_data["hebrew_clean"]
        if hebrew not in unique_words:
            unique_words[hebrew] = {
                "first_id": word_id,
                "verse": word_data["verse"],
                "frequency": word_data["frequency_in_ashrei"],
                "translation": word_data.get("translation", "")
            }

    # Sort by first occurrence (word ID)
    sorted_words = sorted(unique_words.items(), key=lambda x: int(x[1]["first_id"][1:]))

    print("=" * 80)
    print("ASHREI TRANSLATION TEMPLATE")
    print("=" * 80)
    print(f"\nTotal unique words: {len(sorted_words)}")
    print(f"Already translated: {sum(1 for _, d in sorted_words if d['translation'])}")
    print(f"Need translation: {sum(1 for _, d in sorted_words if not d['translation'])}")

    print("\n" + "=" * 80)
    print("WORDS NEEDING TRANSLATION")
    print("=" * 80)

    for hebrew, data in sorted_words:
        if not data['translation']:
            print(f'  "{hebrew}": "",  # {data["first_id"]}, verse {data["verse"]}, appears {data["frequency"]}x')

    print("\n" + "=" * 80)
    print("ALL WORDS (for copy-paste into script)")
    print("=" * 80)
    print("translation_map = {")

    for hebrew, data in sorted_words:
        trans = data['translation'] if data['translation'] else "TODO"
        print(f'    "{hebrew}": "{trans}",  # {data["first_id"]}, v{data["verse"]}, {data["frequency"]}x')

    print("}")

if __name__ == '__main__':
    generate_template()
