#!/usr/bin/env python3
"""
Add shoresh (root) information to words in prayers.
Start with common, clear roots to demonstrate the system.
"""

import json
from pathlib import Path

def load_prayer(prayer_name):
    """Load a prayer JSON file."""
    path = Path(f'/Users/mordechai/Ohr Avraham Chaim/Siddur/data/{prayer_name}_embedded.json')
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_prayer(prayer_name, prayer_data):
    """Save a prayer JSON file."""
    path = Path(f'/Users/mordechai/Ohr Avraham Chaim/Siddur/data/{prayer_name}_embedded.json')
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(prayer_data, f, ensure_ascii=False, indent=2)
    print(f"✓ Saved {prayer_name}")

def get_common_roots_dictionary():
    """
    Dictionary of common Hebrew roots with their meanings.
    This is a starter set - can be expanded to 1500+ roots.
    """
    return {
        "א-ש-ר": {"meaning": "happiness, fortune", "category": "emotion"},
        "י-ש-ב": {"meaning": "sitting, dwelling", "category": "action"},
        "ה-ל-ל": {"meaning": "praise, glory", "category": "worship"},
        "ב-ר-כ": {"meaning": "blessing, knee", "category": "worship"},
        "מ-ל-כ": {"meaning": "kingship, ruling", "category": "authority"},
        "ק-ד-שׁ": {"meaning": "holiness, sanctity", "category": "spiritual"},
        "ע-ש-ה": {"meaning": "making, doing", "category": "action"},
        "ד-ב-ר": {"meaning": "speaking, word", "category": "communication"},
        "י-ד-ע": {"meaning": "knowing, recognizing", "category": "cognition"},
        "ג-ד-ל": {"meaning": "greatness, growing", "category": "size"},
        "ש-ב-ח": {"meaning": "praising, commending", "category": "worship"},
        "ב-ר-א": {"meaning": "creating", "category": "creation"},
        "ע-ל-ה": {"meaning": "ascending, going up", "category": "movement"},
        "י-צ-ר": {"meaning": "forming, creating", "category": "creation"},
        "ג-ו-י": {"meaning": "nation, people", "category": "social"},
        "א-ר-ץ": {"meaning": "land, earth", "category": "geography"},
        "ח-ל-ק": {"meaning": "portion, dividing", "category": "allocation"},
        "ש-ח-ה": {"meaning": "bowing, prostrating", "category": "worship"},
        "י-ד-ה": {"meaning": "thanking, confessing", "category": "worship"},
        "נ-ט-ה": {"meaning": "stretching, bending", "category": "action"},
        "י-ס-ד": {"meaning": "founding, establishing", "category": "creation"},
        "ש-מ-י": {"meaning": "heavens, sky", "category": "geography"},
        "כ-ת-ב": {"meaning": "writing", "category": "communication"},
        "ק-ר-ב": {"meaning": "approaching, near", "category": "proximity"},
        "ק-ר-א": {"meaning": "calling, reading", "category": "communication"},
        "ש-מ-ע": {"meaning": "hearing, listening", "category": "perception"},
        "י-ש-ע": {"meaning": "saving, rescuing", "category": "salvation"},
        "ש-מ-ר": {"meaning": "guarding, watching", "category": "protection"},
        "א-ה-ב": {"meaning": "loving", "category": "emotion"},
        "ר-ש-ע": {"meaning": "wickedness", "category": "morality"},
        "צ-ד-ק": {"meaning": "righteousness", "category": "morality"},
        "ר-ח-מ": {"meaning": "mercy, compassion", "category": "emotion"},
        "ח-ס-ד": {"meaning": "kindness, loyalty", "category": "character"},
        "נ-פ-ל": {"meaning": "falling", "category": "movement"},
        "כ-ר-ע": {"meaning": "kneeling, bowing", "category": "worship"},
        "ח-נ-נ": {"meaning": "grace, favor", "category": "emotion"},
        "ר-ח-ק": {"meaning": "distance, far", "category": "proximity"},
        "ס-מ-כ": {"meaning": "supporting, leaning", "category": "support"},
        "ז-ק-פ": {"meaning": "straightening, raising", "category": "action"},
        "ע-י-נ": {"meaning": "eye, seeing", "category": "perception"},
        "נ-ת-נ": {"meaning": "giving", "category": "action"},
        "א-כ-ל": {"meaning": "eating, food", "category": "sustenance"},
        "פ-ת-ח": {"meaning": "opening", "category": "action"},
        "ש-ב-ע": {"meaning": "satisfaction, seven", "category": "completion"},
        "ח-י-ה": {"meaning": "living, life", "category": "existence"},
        "ד-ר-כ": {"meaning": "way, path", "category": "direction"},
        "ב-ו-א": {"meaning": "coming, entering", "category": "movement"},
        "א-מ-ת": {"meaning": "truth, reliability", "category": "morality"},
        "ל-ב-ב": {"meaning": "heart, inner self", "category": "emotion"},
        "ת-ו-ר": {"meaning": "Torah, instruction", "category": "teaching"},
        "ק-ו-ה": {"meaning": "hoping, waiting", "category": "emotion"},
        "ר-א-ה": {"meaning": "seeing", "category": "perception"},
        "ע-ז-ז": {"meaning": "strength, might", "category": "power"},
        "ע-ב-ר": {"meaning": "passing, crossing", "category": "movement"},
        "ת-ק-נ": {"meaning": "fixing, repairing", "category": "action"},
        "ק-ב-ל": {"meaning": "receiving, accepting", "category": "action"},
        "פ-נ-ה": {"meaning": "turning, facing", "category": "direction"},
        "כ-ב-ד": {"meaning": "honor, heaviness", "category": "respect"},
        "ב-ש-ר": {"meaning": "flesh, messenger", "category": "body"},
        "ש-מ-מ": {"meaning": "name, there", "category": "identity"},
    }

def suggest_root(hebrew_word):
    """
    Attempt to extract root from a Hebrew word.
    This is a simple heuristic - not perfect, but helpful.
    """
    # Remove common prefixes
    prefixes = ['ה', 'ו', 'ל', 'כ', 'ב', 'מ', 'ש']
    # Remove common suffixes
    suffixes = ['ים', 'ות', 'ך', 'כם', 'נו', 'ה', 'ו', 'י', 'ם', 'ן']

    # Strip vowels (nikud) to get consonants only
    consonants = ''.join(c for c in hebrew_word if '\u05D0' <= c <= '\u05EA')

    # Try removing prefixes
    for prefix in prefixes:
        if consonants.startswith(prefix) and len(consonants) > 3:
            consonants = consonants[1:]
            break

    # Try removing suffixes
    for suffix in suffixes:
        if consonants.endswith(suffix):
            consonants = consonants[:-len(suffix)]
            break

    # Extract first 3 letters as potential root
    if len(consonants) >= 3:
        return f"{consonants[0]}-{consonants[1]}-{consonants[2]}"

    return None

def add_shoresh_to_word(word_data, root, root_info, word_type=None, binyan=None, notes=None):
    """Add shoresh information to a word."""
    shoresh = {
        "root": root,
        "root_letters": root.split('-'),
        "meaning": root_info["meaning"],
        "category": root_info["category"]
    }

    if word_type:
        shoresh["word_type"] = word_type
    if binyan:
        shoresh["binyan"] = binyan
    if notes:
        shoresh["notes"] = notes

    word_data["shoresh"] = shoresh

def add_sample_roots_to_ashrei():
    """Add roots to first 20 words of Ashrei as demonstration."""
    print("=" * 70)
    print("ADDING SAMPLE ROOTS TO ASHREI")
    print("=" * 70)

    ashrei = load_prayer("ashrei")
    roots_dict = get_common_roots_dictionary()

    # Sample roots for first 20 words
    word_roots = {
        "w1": ("א-ש-ר", "interjection", None, "Construct plural expressing praise"),
        "w2": ("י-ש-ב", "verb participle", "Kal", "Active participle - those who dwell"),
        "w5": ("ה-ל-ל", "verb", "Piel", "Future tense with suffix ך (You)"),
        "w7": ("א-ש-ר", "interjection", None, "Repeated from w1"),
        "w8": ("ע-מ-מ", "noun", None, "The people/nation"),
        "w15": ("ה-ל-ל", "noun", None, "Praise/psalm"),
        "w17": ("ר-ו-מ", "verb", "Polel", "I will exalt/raise up"),
        "w20": ("ב-ר-כ", "verb", "Piel", "I will bless"),
        "w21": ("ש-מ-מ", "noun", None, "Name with suffix ך (Your)"),
        "w26": ("ב-ר-כ", "verb", "Piel", "I will bless You"),
        "w27": ("ה-ל-ל", "verb", "Piel", "I will praise"),
        "w31": ("ג-ד-ל", "adjective", None, "Great"),
        "w32": ("ה-ו-י", "proper noun", None, "Hashem - the Name"),
        "w33": ("ה-ל-ל", "verb passive", "Pual", "Praised/praiseworthy"),
        "w40": ("ש-ב-ח", "verb", "Piel", "Will praise"),
        "w41": ("ע-ש-ה", "noun", None, "Your works/deeds"),
    }

    added = 0
    for wid, (root, word_type, binyan, notes) in word_roots.items():
        if wid in ashrei["words"] and root in roots_dict:
            add_shoresh_to_word(
                ashrei["words"][wid],
                root,
                roots_dict[root],
                word_type,
                binyan,
                notes
            )
            word = ashrei["words"][wid]
            print(f"✓ {wid}: {word['hebrew_clean']:15} → root {root} ({roots_dict[root]['meaning']})")
            added += 1

    save_prayer("ashrei", ashrei)

    print("\n" + "=" * 70)
    print(f"✓ Added {added} roots to Ashrei")
    print("\nNow you can add more roots using the add_layer.py pattern!")

    return ashrei

def show_root_examples():
    """Show examples of words from same root."""
    ashrei = load_prayer("ashrei")

    print("\n" + "=" * 70)
    print("ROOT PATTERN EXAMPLES")
    print("=" * 70)

    # Find words with ה-ל-ל root
    hallel_words = []
    barak_words = []

    for wid, word in ashrei["words"].items():
        if "shoresh" in word:
            if word["shoresh"]["root"] == "ה-ל-ל":
                hallel_words.append((wid, word["hebrew_clean"], word.get("translation", "")))
            elif word["shoresh"]["root"] == "ב-ר-כ":
                barak_words.append((wid, word["hebrew_clean"], word.get("translation", "")))

    print("\nRoot ה-ל-ל (praise):")
    for wid, hebrew, trans in hallel_words:
        print(f"  {wid}: {hebrew:15} → {trans}")

    print("\nRoot ב-ר-כ (blessing):")
    for wid, hebrew, trans in barak_words:
        print(f"  {wid}: {hebrew:15} → {trans}")

if __name__ == '__main__':
    add_sample_roots_to_ashrei()
    show_root_examples()
