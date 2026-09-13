#!/usr/bin/env python3
"""Complete the remaining 92 words in Shema with translations and shoresh."""

import json
from collections import defaultdict

def load_shema():
    with open('data/shema_embedded.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def save_shema(data):
    with open('data/shema_embedded.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def get_complete_mappings():
    """Word ID to translation and shoresh mappings for all 92 missing words."""
    return {
        "w1": {"trans": "Hear / Listen", "root": "ש-מ-ע", "meaning": "hearing, listening", "type": "verb"},
        "w8": {"trans": "Blessed", "root": "ב-ר-כ", "meaning": "blessing, knee", "type": "adjective"},
        "w9": {"trans": "Name", "root": "ש-מ-מ", "meaning": "name", "type": "noun"},
        "w10": {"trans": "glory / honor", "root": "כ-ב-ד", "meaning": "weight, glory, honor", "type": "noun"},
        "w14": {"trans": "and you shall love", "root": "א-ה-ב", "meaning": "love", "type": "verb"},
        "w18": {"trans": "with all", "root": "כ-ל-ל", "meaning": "all, every", "type": "preposition+noun"},
        "w21": {"trans": "your soul", "root": "נ-פ-ש", "meaning": "soul, life", "type": "noun"},
        "w25": {"trans": "the words / matters", "root": "ד-ב-ר", "meaning": "word, speak", "type": "noun"},
        "w26": {"trans": "these", "root": "א-ל-ה", "meaning": "these", "type": "demonstrative"},
        "w27": {"trans": "that / which", "root": "א-ש-ר", "meaning": "that, which", "type": "relative pronoun"},
        "w29": {"trans": "I command you", "root": "צ-ו-ה", "meaning": "command", "type": "verb"},
        "w33": {"trans": "and you shall teach them diligently", "root": "ש-נ-נ", "meaning": "sharpen, teach", "type": "verb"},
        "w35": {"trans": "and you shall speak", "root": "ד-ב-ר", "meaning": "speak, word", "type": "verb"},
        "w36": {"trans": "of them / with them", "root": "ב-ב-ב", "meaning": "in, with", "type": "preposition"},
        "w37": {"trans": "when you sit", "root": "י-ש-ב", "meaning": "sit, dwell", "type": "verb"},
        "w38": {"trans": "in your house", "root": "ב-י-ת", "meaning": "house", "type": "noun"},
        "w39": {"trans": "and when you walk", "root": "ה-ל-כ", "meaning": "walk, go", "type": "verb"},
        "w40": {"trans": "on the way / road", "root": "ד-ר-כ", "meaning": "way, path", "type": "noun"},
        "w41": {"trans": "and when you lie down", "root": "ש-כ-ב", "meaning": "lie down", "type": "verb"},
        "w43": {"trans": "and you shall bind them", "root": "ק-ש-ר", "meaning": "bind, tie", "type": "verb"},
        "w49": {"trans": "between", "root": "ב-י-נ", "meaning": "between", "type": "preposition"},
        "w51": {"trans": "and you shall write them", "root": "כ-ת-ב", "meaning": "write", "type": "verb"},
        "w54": {"trans": "your house", "root": "ב-י-ת", "meaning": "house", "type": "noun"},
        "w55": {"trans": "and on your gates", "root": "ש-ע-ר", "meaning": "gate", "type": "noun"},
        "w58": {"trans": "listening / hearing", "root": "ש-מ-ע", "meaning": "hear, listen", "type": "verb"},
        "w59": {"trans": "you will listen", "root": "ש-מ-ע", "meaning": "hear, listen", "type": "verb"},
        "w62": {"trans": "that / which", "root": "א-ש-ר", "meaning": "that, which", "type": "relative pronoun"},
        "w64": {"trans": "I command", "root": "צ-ו-ה", "meaning": "command", "type": "verb"},
        "w72": {"trans": "with all", "root": "כ-ל-ל", "meaning": "all, every", "type": "preposition+noun"},
        "w75": {"trans": "your soul", "root": "נ-פ-ש", "meaning": "soul, life", "type": "noun"},
        "w76": {"trans": "and I will give", "root": "נ-ת-נ", "meaning": "give", "type": "verb"},
        "w79": {"trans": "in its time", "root": "ע-ת-ת", "meaning": "time, season", "type": "noun"},
        "w82": {"trans": "and you will gather", "root": "א-ס-פ", "meaning": "gather, collect", "type": "verb"},
        "w84": {"trans": "and your wine", "root": "י-ר-ש", "meaning": "wine, new wine", "type": "noun"},
        "w86": {"trans": "and I will give", "root": "נ-ת-נ", "meaning": "give", "type": "verb"},
        "w88": {"trans": "in your field", "root": "ש-ד-ד", "meaning": "field", "type": "noun"},
        "w89": {"trans": "for your cattle", "root": "ב-ה-מ", "meaning": "beast, cattle", "type": "noun"},
        "w90": {"trans": "and you will eat", "root": "א-כ-ל", "meaning": "eat", "type": "verb"},
        "w91": {"trans": "and be satisfied", "root": "ש-ב-ע", "meaning": "satisfy, be full", "type": "verb"},
        "w92": {"trans": "Guard yourselves", "root": "ש-מ-ר", "meaning": "guard, keep", "type": "verb"},
        "w94": {"trans": "lest", "root": "פ-נ-נ", "meaning": "lest, turn", "type": "conjunction"},
        "w95": {"trans": "it should deceive / be seduced", "root": "פ-ת-ה", "meaning": "deceive, seduce", "type": "verb"},
        "w97": {"trans": "and you turn away", "root": "ס-ו-ר", "meaning": "turn aside, depart", "type": "verb"},
        "w98": {"trans": "and you will serve", "root": "ע-ב-ד", "meaning": "serve, work", "type": "verb"},
        "w101": {"trans": "and you bow down", "root": "ש-ח-ה", "meaning": "bow, prostrate", "type": "verb"},
        "w106": {"trans": "against you", "root": "ב-ב-ב", "meaning": "in, with", "type": "preposition"},
        "w109": {"trans": "the heavens", "root": "ש-מ-מ", "meaning": "heavens, sky", "type": "noun"},
        "w115": {"trans": "will give", "root": "נ-ת-נ", "meaning": "give", "type": "verb"},
        "w118": {"trans": "and you will perish", "root": "א-ב-ד", "meaning": "perish, be lost", "type": "verb"},
        "w123": {"trans": "that / which", "root": "א-ש-ר", "meaning": "that, which", "type": "relative pronoun"},
        "w127": {"trans": "and you shall place", "root": "ש-ו-מ", "meaning": "place, put", "type": "verb"},
        "w129": {"trans": "My words", "root": "ד-ב-ר", "meaning": "word, speak", "type": "noun"},
        "w130": {"trans": "these", "root": "א-ל-ה", "meaning": "these", "type": "demonstrative"},
        "w133": {"trans": "and on", "root": "ע-ל-ל", "meaning": "upon, over", "type": "preposition"},
        "w134": {"trans": "your soul", "root": "נ-פ-ש", "meaning": "soul, life", "type": "noun"},
        "w135": {"trans": "and you shall bind them", "root": "ק-ש-ר", "meaning": "bind, tie", "type": "verb"},
        "w142": {"trans": "between", "root": "ב-י-נ", "meaning": "between", "type": "preposition"},
        "w144": {"trans": "and you shall teach them", "root": "ל-מ-ד", "meaning": "learn, teach", "type": "verb"},
        "w147": {"trans": "your children", "root": "ב-נ-נ", "meaning": "son, child", "type": "noun"},
        "w148": {"trans": "to speak", "root": "ד-ב-ר", "meaning": "speak, word", "type": "verb"},
        "w149": {"trans": "of them", "root": "ב-ב-ב", "meaning": "in, with", "type": "preposition"},
        "w150": {"trans": "when you sit", "root": "י-ש-ב", "meaning": "sit, dwell", "type": "verb"},
        "w151": {"trans": "in your house", "root": "ב-י-ת", "meaning": "house", "type": "noun"},
        "w152": {"trans": "and when you walk", "root": "ה-ל-כ", "meaning": "walk, go", "type": "verb"},
        "w153": {"trans": "on the way", "root": "ד-ר-כ", "meaning": "way, path", "type": "noun"},
        "w154": {"trans": "and when you lie down", "root": "ש-כ-ב", "meaning": "lie down", "type": "verb"},
        "w156": {"trans": "and you shall write them", "root": "כ-ת-ב", "meaning": "write", "type": "verb"},
        "w159": {"trans": "your house", "root": "ב-י-ת", "meaning": "house", "type": "noun"},
        "w160": {"trans": "and on your gates", "root": "ש-ע-ר", "meaning": "gate", "type": "noun"},
        "w165": {"trans": "your children", "root": "ב-נ-נ", "meaning": "son, child", "type": "noun"},
        "w168": {"trans": "that / which", "root": "א-ש-ר", "meaning": "that, which", "type": "relative pronoun"},
        "w169": {"trans": "swore", "root": "ש-ב-ע", "meaning": "swear, oath", "type": "verb"},
        "w174": {"trans": "like the days of", "root": "י-ו-מ", "meaning": "day", "type": "noun"},
        "w175": {"trans": "the heavens", "root": "ש-מ-מ", "meaning": "heavens, sky", "type": "noun"},
        "w181": {"trans": "Moses", "root": "מ-ש-ה", "meaning": "Moses (proper name)", "type": "proper noun"},
        "w182": {"trans": "saying", "root": "א-מ-ר", "meaning": "say, speak", "type": "verb"},
        "w183": {"trans": "Speak", "root": "ד-ב-ר", "meaning": "speak, word", "type": "verb"},
        "w185": {"trans": "the children of", "root": "ב-נ-נ", "meaning": "son, child", "type": "noun"},
        "w187": {"trans": "and you shall say", "root": "א-מ-ר", "meaning": "say, speak", "type": "verb"},
        "w193": {"trans": "the corners", "root": "כ-נ-פ", "meaning": "corner, wing", "type": "noun"},
        "w199": {"trans": "the corner", "root": "כ-נ-פ", "meaning": "corner, wing", "type": "noun"},
        "w200": {"trans": "a thread", "root": "פ-ת-ל", "meaning": "thread, cord", "type": "noun"},
        "w201": {"trans": "of blue", "root": "כ-ל-ל", "meaning": "blue, techelet", "type": "noun"},
        "w207": {"trans": "and you shall remember", "root": "ז-כ-ר", "meaning": "remember", "type": "verb"},
        "w209": {"trans": "all", "root": "כ-ל-ל", "meaning": "all, every", "type": "noun"},
        "w218": {"trans": "and after", "root": "א-ח-ר", "meaning": "after, following", "type": "preposition"},
        "w220": {"trans": "that / which", "root": "א-ש-ר", "meaning": "that, which", "type": "relative pronoun"},
        "w221": {"trans": "you", "root": "א-ת-ת", "meaning": "you (plural)", "type": "pronoun"},
        "w225": {"trans": "you will remember", "root": "ז-כ-ר", "meaning": "remember", "type": "verb"},
        "w228": {"trans": "all", "root": "כ-ל-ל", "meaning": "all, every", "type": "noun"},
        "w231": {"trans": "holy", "root": "ק-ד-ש", "meaning": "holy, sacred", "type": "adjective"},
        "w236": {"trans": "Who", "root": "א-ש-ר", "meaning": "who, which", "type": "relative pronoun"},
    }

def calculate_shoresh_frequencies(shema_data):
    """Calculate frequency counts for all roots across Shema."""
    root_counts = defaultdict(int)

    # Count all roots
    for word in shema_data["words"].values():
        if "shoresh" in word and "root" in word["shoresh"]:
            root_counts[word["shoresh"]["root"]] += 1

    # Apply frequencies
    for word in shema_data["words"].values():
        if "shoresh" in word and "root" in word["shoresh"]:
            root = word["shoresh"]["root"]
            word["shoresh"]["frequency_in_shema"] = root_counts[root]

    return root_counts

def main():
    print("Loading Shema data...")
    shema = load_shema()

    mappings = get_complete_mappings()

    print(f"Adding translations and shoresh for {len(mappings)} words...")

    added = 0
    for word_id, data in mappings.items():
        if word_id in shema["words"]:
            word = shema["words"][word_id]

            # Add translation
            word["translation"] = data["trans"]

            # Add shoresh
            word["shoresh"] = {
                "root": data["root"],
                "root_letters": list(data["root"].split("-")),
                "meaning": data["meaning"],
                "word_type": data["type"]
            }

            added += 1

    print(f"Added {added} translations and shoresh entries")

    # Calculate frequencies
    print("Calculating shoresh frequencies...")
    root_counts = calculate_shoresh_frequencies(shema)

    # Count completion
    total_words = len(shema["words"])
    with_translation = sum(1 for w in shema["words"].values() if "translation" in w and w["translation"])
    with_shoresh = sum(1 for w in shema["words"].values() if "shoresh" in w)
    unique_roots = len(root_counts)

    print(f"\n✅ Shema completion status:")
    print(f"   Total words: {total_words}")
    print(f"   Translations: {with_translation}/{total_words} ({100*with_translation/total_words:.1f}%)")
    print(f"   With shoresh: {with_shoresh}/{total_words} ({100*with_shoresh/total_words:.1f}%)")
    print(f"   Unique roots: {unique_roots}")

    # Save
    print("\nSaving updated Shema data...")
    save_shema(shema)
    print("✅ Complete!")

if __name__ == "__main__":
    main()
