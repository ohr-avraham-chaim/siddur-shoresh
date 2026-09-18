#!/usr/bin/env python3
"""
Build clean embedded JSON for Ashrei.
Simple sequential structure: Words → Phrases → Verses → Layers
"""

import json
import re
from pathlib import Path

def build_ashrei_embedded():
    """
    Build embedded JSON structure:
    - Each word gets sequential ID: w1, w2, w3...
    - Phrases are sequences of word IDs
    - Verses are sequences of word IDs
    - Layers can be added iteratively
    """

    # Load clean Hebrew text
    ashrei_path = Path('/Users/mordechai/Ohr Avraham Chaim/Siddur/clean_ashrei.md')
    with open(ashrei_path, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    # Initialize structure
    ashrei = {
        "prayer_name": {
            "hebrew": "אַשְׁרֵי",
            "english": "Ashrei",
            "source": "Psalm 145 with intro/conclusion verses"
        },
        "words": {},
        "verses": {},
        "phrases": {},
        "layers": {
            "base_text": "complete",
            "translations": "pending",
            "grammar": "pending",
            "kavanot": "pending",
            "instructions": "pending"
        }
    }

    # First pass: count word frequencies
    word_frequency = {}
    for line in lines:
        raw_words = line.split()
        for raw_word in raw_words:
            word_clean = re.sub(r'[׃:.]$', '', raw_word)
            word_frequency[word_clean] = word_frequency.get(word_clean, 0) + 1

    # Parse words sequentially
    word_id = 1
    verse_number = 1

    for line in lines:
        # Split into words
        raw_words = line.split()

        # Track verse
        verse_start_id = word_id
        verse_word_ids = []

        for raw_word in raw_words:
            # Clean word (remove punctuation for base form)
            word_clean = re.sub(r'[׃:.]$', '', raw_word)
            punctuation = raw_word[len(word_clean):] if len(raw_word) > len(word_clean) else ''

            # Create word entry
            word_entry = {
                "id": f"w{word_id}",
                "hebrew": raw_word,
                "hebrew_clean": word_clean,
                "punctuation": punctuation,
                "verse": verse_number,
                "position_in_verse": len(verse_word_ids) + 1,
                "position_global": word_id,
                "frequency_in_ashrei": word_frequency[word_clean]
            }

            ashrei["words"][f"w{word_id}"] = word_entry
            verse_word_ids.append(f"w{word_id}")

            word_id += 1

        # Create verse entry
        verse_entry = {
            "id": f"v{verse_number}",
            "number": verse_number,
            "word_ids": verse_word_ids,
            "hebrew_full": line,
            "word_count": len(verse_word_ids)
        }

        ashrei["verses"][f"v{verse_number}"] = verse_entry
        verse_number += 1

    return ashrei

def extract_phrases_from_words(ashrei, min_length=2, max_length=8):
    """
    Extract phrases as sequences of word IDs.
    Only track phrases that repeat or are significant.
    """
    phrases = {}
    phrase_id = 1

    # Build temporary phrase tracker
    phrase_tracker = {}  # hebrew text -> list of word ID sequences

    # Extract all possible phrases
    for verse_key, verse in ashrei["verses"].items():
        word_ids = verse["word_ids"]

        # Try phrases of different lengths
        for length in range(min_length, min(max_length + 1, len(word_ids) + 1)):
            for start in range(len(word_ids) - length + 1):
                phrase_word_ids = word_ids[start:start + length]

                # Get Hebrew text for this phrase
                phrase_text = ' '.join(
                    ashrei["words"][wid]["hebrew_clean"]
                    for wid in phrase_word_ids
                )

                # Track occurrence
                if phrase_text not in phrase_tracker:
                    phrase_tracker[phrase_text] = []

                phrase_tracker[phrase_text].append({
                    "word_ids": phrase_word_ids,
                    "verse": verse["number"]
                })

    # Filter to significant phrases (repeated or long)
    for phrase_text, occurrences in phrase_tracker.items():
        if len(occurrences) > 1 or len(occurrences[0]["word_ids"]) >= 4:
            phrase_entry = {
                "id": f"p{phrase_id}",
                "hebrew": phrase_text,
                "frequency": len(occurrences),
                "occurrences": occurrences,
                "category": "repeated" if len(occurrences) > 1 else "significant"
            }

            phrases[f"p{phrase_id}"] = phrase_entry
            phrase_id += 1

    return phrases

def main():
    print("=" * 70)
    print("BUILDING ASHREI EMBEDDED JSON")
    print("=" * 70)

    print("\n1. Building word-by-word sequential structure...")
    ashrei = build_ashrei_embedded()

    total_words = len(ashrei["words"])
    total_verses = len(ashrei["verses"])

    print(f"   ✓ {total_words} words mapped sequentially (w1 → w{total_words})")
    print(f"   ✓ {total_verses} verses structured")

    print("\n2. Extracting significant phrases...")
    ashrei["phrases"] = extract_phrases_from_words(ashrei)

    repeated = sum(1 for p in ashrei["phrases"].values() if p["frequency"] > 1)
    significant = len(ashrei["phrases"]) - repeated

    print(f"   ✓ {len(ashrei['phrases'])} phrases identified")
    print(f"      - {repeated} repeated phrases")
    print(f"      - {significant} significant long phrases")

    # Show top repeated phrases
    top_phrases = sorted(
        [p for p in ashrei["phrases"].values() if p["frequency"] > 1],
        key=lambda x: x["frequency"],
        reverse=True
    )[:5]

    print("\n   Top repeated phrases:")
    for p in top_phrases:
        print(f"      - \"{p['hebrew']}\" ({p['frequency']}x)")

    print("\n3. Saving embedded JSON...")
    output_dir = Path('/Users/mordechai/Ohr Avraham Chaim/Siddur/data')
    output_dir.mkdir(exist_ok=True)

    output_path = output_dir / 'ashrei_embedded.json'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(ashrei, f, ensure_ascii=False, indent=2)

    print(f"   ✓ Saved: {output_path}")
    print(f"   ✓ Size: {output_path.stat().st_size / 1024:.1f} KB")

    # Summary
    print("\n" + "=" * 70)
    print("STRUCTURE SUMMARY")
    print("=" * 70)
    print(f"Words: {len(ashrei['words'])} (w1 → w{len(ashrei['words'])})")
    print(f"Verses: {len(ashrei['verses'])} (v1 → v{len(ashrei['verses'])})")
    print(f"Phrases: {len(ashrei['phrases'])} (p1 → p{len(ashrei['phrases'])})")
    print("\nExample word structure:")
    print(json.dumps(ashrei["words"]["w1"], ensure_ascii=False, indent=2))
    print("\nExample verse structure:")
    print(json.dumps(ashrei["verses"]["v1"], ensure_ascii=False, indent=2))
    if ashrei["phrases"]:
        first_phrase = list(ashrei["phrases"].values())[0]
        print("\nExample phrase structure:")
        print(json.dumps(first_phrase, ensure_ascii=False, indent=2))

    print("\n" + "=" * 70)
    print("READY FOR ITERATIVE LAYER ADDITION")
    print("=" * 70)
    print("Next steps:")
    print("  1. Add translation layer (user approval workflow)")
    print("  2. Add grammar layer (roots, verb forms)")
    print("  3. Add kavanot layer (intentions)")
    print("  4. Add instruction layer (when/how to say)")

if __name__ == '__main__':
    main()
