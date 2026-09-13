#!/usr/bin/env python3
"""Build complete Netilat Yadayim bracha with translations and shoresh."""

import json
import re
from collections import defaultdict

def get_word_mappings():
    """Complete mappings for all words in Netilat Yadayim."""
    return {
        "בָּרוּךְ": {"trans": "Blessed", "root": "ב-ר-כ", "meaning": "blessing, knee", "type": "adjective"},
        "אַתָּה": {"trans": "You are", "root": "א-ת-ת", "meaning": "you (masculine singular)", "type": "pronoun"},
        "ה'": {"trans": "Hashem", "root": "ה-ו-י", "meaning": "God's name (YHVH)", "type": "proper noun"},
        "אֱלהֵינוּ": {"trans": "our God", "root": "א-ל-ה", "meaning": "God, deity", "type": "noun"},
        "מֶלֶךְ": {"trans": "King", "root": "מ-ל-כ", "meaning": "kingship, ruling", "type": "noun"},
        "הָעולָם": {"trans": "of the world / universe", "root": "ע-ל-מ", "meaning": "eternity, world", "type": "noun"},
        "אֲשֶׁר": {"trans": "Who", "root": "א-ש-ר", "meaning": "who, which, that", "type": "relative pronoun"},
        "קִדְּשָׁנוּ": {"trans": "sanctified us", "root": "ק-ד-ש", "meaning": "holy, sanctify", "type": "verb"},
        "בְּמִצְותָיו": {"trans": "with His commandments", "root": "צ-ו-ה", "meaning": "command", "type": "noun"},
        "וְצִוָּנוּ": {"trans": "and commanded us", "root": "צ-ו-ה", "meaning": "command", "type": "verb"},
        "עַל": {"trans": "on / concerning", "root": "ע-ל-ל", "meaning": "upon, over", "type": "preposition"},
        "נְטִילַת": {"trans": "washing / lifting", "root": "נ-ט-ל", "meaning": "lift, take, wash", "type": "noun"},
        "יָדַיִם:": {"trans": "hands", "root": "י-ד-ד", "meaning": "hand", "type": "noun"},
    }

def build_netilat_yadayim():
    """Build complete embedded JSON for Netilat Yadayim."""

    # Hebrew text
    text = "בָּרוּךְ אַתָּה ה' אֱלהֵינוּ מֶלֶךְ הָעולָם אֲשֶׁר קִדְּשָׁנוּ בְּמִצְותָיו וְצִוָּנוּ עַל נְטִילַת יָדַיִם:"

    # Parse words
    raw_words = text.split()

    # Get mappings
    mappings = get_word_mappings()

    # Initialize structure
    bracha = {
        "prayer_name": {
            "hebrew": "נְטִילַת יָדַיִם",
            "english": "Netilat Yadayim",
            "translation": "Washing the Hands"
        },
        "words": {},
        "blessing_formula": {
            "opening": "בָּרוּךְ אַתָּה ה' אֱלהֵינוּ מֶלֶךְ הָעולָם",
            "opening_translation": "Blessed are You, Hashem our God, King of the universe",
            "specific_text": "אֲשֶׁר קִדְּשָׁנוּ בְּמִצְותָיו וְצִוָּנוּ עַל נְטִילַת יָדַיִם",
            "specific_translation": "Who sanctified us with His commandments and commanded us concerning the washing of hands"
        }
    }

    # Build words
    word_frequency = defaultdict(int)
    for raw_word in raw_words:
        word_clean = re.sub(r'[׃:.]', '', raw_word)
        word_frequency[word_clean] += 1

    word_id = 1
    for raw_word in raw_words:
        word_clean = re.sub(r'[׃:.]', '', raw_word)
        punctuation = raw_word[len(word_clean):] if len(raw_word) > len(word_clean) else ''

        # Get mapping (try with and without punctuation)
        mapping = mappings.get(raw_word) or mappings.get(word_clean)

        word_entry = {
            "id": f"w{word_id}",
            "hebrew": raw_word,
            "hebrew_clean": word_clean,
            "punctuation": punctuation,
            "position_global": word_id,
            "frequency_in_netilat_yadayim": word_frequency[word_clean]
        }

        if mapping:
            word_entry["translation"] = mapping["trans"]
            word_entry["shoresh"] = {
                "root": mapping["root"],
                "root_letters": list(mapping["root"].split("-")),
                "meaning": mapping["meaning"],
                "word_type": mapping["type"]
            }

        bracha["words"][f"w{word_id}"] = word_entry
        word_id += 1

    # Calculate shoresh frequencies
    root_counts = defaultdict(int)
    for word in bracha["words"].values():
        if "shoresh" in word:
            root_counts[word["shoresh"]["root"]] += 1

    for word in bracha["words"].values():
        if "shoresh" in word:
            word["shoresh"]["frequency_in_netilat_yadayim"] = root_counts[word["shoresh"]["root"]]

    return bracha

def main():
    print("Building Netilat Yadayim bracha...")
    bracha = build_netilat_yadayim()

    # Save
    with open('data/netilat_yadayim_embedded.json', 'w', encoding='utf-8') as f:
        json.dump(bracha, f, ensure_ascii=False, indent=2)

    # Stats
    total = len(bracha["words"])
    with_trans = sum(1 for w in bracha["words"].values() if "translation" in w)
    with_shoresh = sum(1 for w in bracha["words"].values() if "shoresh" in w)
    unique_roots = len(set(w["shoresh"]["root"] for w in bracha["words"].values() if "shoresh" in w))

    print(f"\n✅ Netilat Yadayim complete:")
    print(f"   Total words: {total}")
    print(f"   Translations: {with_trans}/{total} ({100*with_trans/total:.1f}%)")
    print(f"   With shoresh: {with_shoresh}/{total} ({100*with_shoresh/total:.1f}%)")
    print(f"   Unique roots: {unique_roots}")

if __name__ == "__main__":
    main()
