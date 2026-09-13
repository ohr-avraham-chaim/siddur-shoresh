#!/usr/bin/env python3
"""
Add layers iteratively to Ashrei embedded JSON.
Can add to: words, phrases, verses, or entire prayer.
"""

import json
import sys
from pathlib import Path

def load_ashrei():
    """Load the embedded Ashrei JSON."""
    path = Path('/Users/mordechai/Ohr Avraham Chaim/Siddur/data/ashrei_embedded.json')
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_ashrei(ashrei):
    """Save the embedded Ashrei JSON."""
    path = Path('/Users/mordechai/Ohr Avraham Chaim/Siddur/data/ashrei_embedded.json')
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(ashrei, f, ensure_ascii=False, indent=2)
    print(f"✓ Saved changes to {path}")

def add_word_layer(ashrei, word_id, layer_name, layer_data):
    """
    Add a layer to a specific word.

    Examples:
      add_word_layer(ashrei, "w1", "translation", "praiseworthy")
      add_word_layer(ashrei, "w1", "root", "אשר")
      add_word_layer(ashrei, "w1", "grammar", {"type": "adjective", "number": "plural"})
    """
    if word_id not in ashrei["words"]:
        print(f"✗ Word {word_id} not found")
        return False

    ashrei["words"][word_id][layer_name] = layer_data
    print(f"✓ Added '{layer_name}' to {word_id}: {ashrei['words'][word_id]['hebrew']}")
    return True

def add_phrase_layer(ashrei, phrase_id, layer_name, layer_data):
    """
    Add a layer to a specific phrase.

    Examples:
      add_phrase_layer(ashrei, "p1", "translation", "Praiseworthy are those who dwell in Your house")
      add_phrase_layer(ashrei, "p1", "kavanah", "Focus on being in God's presence")
    """
    if phrase_id not in ashrei["phrases"]:
        print(f"✗ Phrase {phrase_id} not found")
        return False

    ashrei["phrases"][phrase_id][layer_name] = layer_data
    print(f"✓ Added '{layer_name}' to {phrase_id}: {ashrei['phrases'][phrase_id]['hebrew']}")
    return True

def add_verse_layer(ashrei, verse_id, layer_name, layer_data):
    """
    Add a layer to a specific verse.

    Examples:
      add_verse_layer(ashrei, "v1", "translation", "Praiseworthy are those...")
      add_verse_layer(ashrei, "v1", "instruction", "Say while standing")
      add_verse_layer(ashrei, "v1", "kavanah", "Think about dwelling in God's house")
    """
    if verse_id not in ashrei["verses"]:
        print(f"✗ Verse {verse_id} not found")
        return False

    ashrei["verses"][verse_id][layer_name] = layer_data
    print(f"✓ Added '{layer_name}' to {verse_id}")
    return True

def add_prayer_layer(ashrei, layer_name, layer_data):
    """
    Add a layer to the entire prayer.

    Examples:
      add_prayer_layer(ashrei, "general_instruction", "Said three times daily")
      add_prayer_layer(ashrei, "theme", "Praise and God's sovereignty")
    """
    if "prayer_layers" not in ashrei:
        ashrei["prayer_layers"] = {}

    ashrei["prayer_layers"][layer_name] = layer_data
    print(f"✓ Added prayer-level '{layer_name}' layer")
    return True

def show_word(ashrei, word_id):
    """Display all layers for a word."""
    if word_id not in ashrei["words"]:
        print(f"✗ Word {word_id} not found")
        return

    word = ashrei["words"][word_id]
    print(f"\n{word_id}: {word['hebrew']}")
    print("─" * 50)
    for key, value in word.items():
        if key not in ['id', 'hebrew', 'hebrew_clean']:
            print(f"  {key}: {value}")

def show_phrase(ashrei, phrase_id):
    """Display all layers for a phrase."""
    if phrase_id not in ashrei["phrases"]:
        print(f"✗ Phrase {phrase_id} not found")
        return

    phrase = ashrei["phrases"][phrase_id]
    print(f"\n{phrase_id}: {phrase['hebrew']}")
    print("─" * 50)
    for key, value in phrase.items():
        if key != 'id':
            if isinstance(value, list) and key == 'occurrences':
                print(f"  {key}: {len(value)} occurrences")
            else:
                print(f"  {key}: {value}")

def show_verse(ashrei, verse_id):
    """Display all layers for a verse."""
    if verse_id not in ashrei["verses"]:
        print(f"✗ Verse {verse_id} not found")
        return

    verse = ashrei["verses"][verse_id]
    print(f"\n{verse_id}: {verse['hebrew_full']}")
    print("─" * 50)
    for key, value in verse.items():
        if key not in ['id', 'word_ids']:
            print(f"  {key}: {value}")

# Example usage functions

def example_add_translations():
    """Example: Add translations to first verse."""
    print("\nEXAMPLE: Adding translations to verse 1 words")
    print("=" * 60)

    ashrei = load_ashrei()

    # Add word-level translations
    translations = {
        "w1": "praiseworthy",
        "w2": "dwellers/those who dwell",
        "w3": "Your house",
        "w4": "still/continuously",
        "w5": "they will praise You",
        "w6": "Selah"
    }

    for word_id, translation in translations.items():
        add_word_layer(ashrei, word_id, "translation", translation)

    save_ashrei(ashrei)

def example_add_kavanot():
    """Example: Add kavanot to phrases."""
    print("\nEXAMPLE: Adding kavanot to repeated phrases")
    print("=" * 60)

    ashrei = load_ashrei()

    # Add kavanah to the repeated phrase "לְעולָם וָעֶד"
    for phrase_id, phrase in ashrei["phrases"].items():
        if phrase["hebrew"] == "לְעולָם וָעֶד":
            add_phrase_layer(
                ashrei,
                phrase_id,
                "kavanah",
                "Forever and ever - focus on God's eternal nature"
            )

    save_ashrei(ashrei)

def example_add_instructions():
    """Example: Add instructions at verse level."""
    print("\nEXAMPLE: Adding instructions to specific verses")
    print("=" * 60)

    ashrei = load_ashrei()

    # Add instruction for verse 16 (פותח את ידך)
    # This is verse 16 in our structure
    add_verse_layer(
        ashrei,
        "v16",
        "instruction",
        "Say with special concentration - this verse has special power for sustenance"
    )

    save_ashrei(ashrei)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Layer Addition Tool for Ashrei")
        print("=" * 60)
        print("\nUsage:")
        print("  python3 add_layer.py show <type> <id>")
        print("    Example: python3 add_layer.py show word w1")
        print("    Example: python3 add_layer.py show phrase p1")
        print("    Example: python3 add_layer.py show verse v1")
        print("\n  python3 add_layer.py example <name>")
        print("    Example: python3 add_layer.py example translations")
        print("    Example: python3 add_layer.py example kavanot")
        print("    Example: python3 add_layer.py example instructions")
        sys.exit(0)

    command = sys.argv[1]

    if command == "show":
        if len(sys.argv) < 4:
            print("Usage: python3 add_layer.py show <type> <id>")
            sys.exit(1)

        ashrei = load_ashrei()
        item_type = sys.argv[2]
        item_id = sys.argv[3]

        if item_type == "word":
            show_word(ashrei, item_id)
        elif item_type == "phrase":
            show_phrase(ashrei, item_id)
        elif item_type == "verse":
            show_verse(ashrei, item_id)

    elif command == "example":
        if len(sys.argv) < 3:
            print("Usage: python3 add_layer.py example <name>")
            print("Examples: translations, kavanot, instructions")
            sys.exit(1)

        example_name = sys.argv[2]

        if example_name == "translations":
            example_add_translations()
        elif example_name == "kavanot":
            example_add_kavanot()
        elif example_name == "instructions":
            example_add_instructions()
