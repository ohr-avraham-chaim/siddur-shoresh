#!/usr/bin/env python3
"""
Build clean embedded JSON for Aleinu.
Same structure as Ashrei: Words → Phrases → Verses → Layers
"""

import json
import re
from pathlib import Path

def build_aleinu_embedded():
    """
    Build embedded JSON structure for Aleinu:
    - Each word gets sequential ID: w1, w2, w3...
    - Phrases are sequences of word IDs
    - Paragraphs (not verses) are sequences of word IDs
    - Layers can be added iteratively
    """

    # Load clean Hebrew text
    aleinu_path = Path('/Users/mordechai/Ohr Avraham Chaim/Siddur/alenu_clean.md')
    with open(aleinu_path, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    # Initialize structure
    aleinu = {
        "prayer_name": {
            "hebrew": "עָלֵינוּ לְשַׁבֵּחַ",
            "english": "Aleinu",
            "source": "Attributed to Joshua (traditional); Tractate Rosh Hashanah"
        },
        "words": {},
        "paragraphs": {},  # Aleinu has 2 paragraphs, not verses
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
    paragraph_number = 1

    for line in lines:
        # Split into words
        raw_words = line.split()

        # Track paragraph
        paragraph_word_ids = []

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
                "paragraph": paragraph_number,
                "position_in_paragraph": len(paragraph_word_ids) + 1,
                "position_global": word_id,
                "frequency_in_aleinu": word_frequency[word_clean]
            }

            aleinu["words"][f"w{word_id}"] = word_entry
            paragraph_word_ids.append(f"w{word_id}")

            word_id += 1

        # Create paragraph entry
        paragraph_entry = {
            "id": f"p{paragraph_number}",
            "number": paragraph_number,
            "word_ids": paragraph_word_ids,
            "hebrew_full": line,
            "word_count": len(paragraph_word_ids),
            "description": "First paragraph" if paragraph_number == 1 else "Second paragraph"
        }

        aleinu["paragraphs"][f"p{paragraph_number}"] = paragraph_entry
        paragraph_number += 1

    return aleinu

def extract_phrases_from_words(aleinu, min_length=2, max_length=8):
    """
    Extract phrases as sequences of word IDs.
    Only track phrases that repeat or are significant.
    """
    phrases = {}
    phrase_id = 1

    # Build temporary phrase tracker
    phrase_tracker = {}  # hebrew text -> list of word ID sequences

    # Extract all possible phrases from each paragraph
    for para_key, para in aleinu["paragraphs"].items():
        word_ids = para["word_ids"]

        # Try phrases of different lengths
        for length in range(min_length, min(max_length + 1, len(word_ids) + 1)):
            for start in range(len(word_ids) - length + 1):
                phrase_word_ids = word_ids[start:start + length]

                # Get Hebrew text for this phrase
                phrase_text = ' '.join(
                    aleinu["words"][wid]["hebrew_clean"]
                    for wid in phrase_word_ids
                )

                # Track occurrence
                if phrase_text not in phrase_tracker:
                    phrase_tracker[phrase_text] = []

                phrase_tracker[phrase_text].append({
                    "word_ids": phrase_word_ids,
                    "paragraph": para["number"]
                })

    # Filter to significant phrases (repeated or long)
    for phrase_text, occurrences in phrase_tracker.items():
        if len(occurrences) > 1 or len(occurrences[0]["word_ids"]) >= 4:
            phrase_entry = {
                "id": f"ph{phrase_id}",
                "hebrew": phrase_text,
                "frequency": len(occurrences),
                "occurrences": occurrences,
                "category": "repeated" if len(occurrences) > 1 else "significant"
            }

            phrases[f"ph{phrase_id}"] = phrase_entry
            phrase_id += 1

    return phrases

def main():
    print("=" * 70)
    print("BUILDING ALEINU EMBEDDED JSON")
    print("=" * 70)

    print("\n1. Building word-by-word sequential structure...")
    aleinu = build_aleinu_embedded()

    total_words = len(aleinu["words"])
    total_paragraphs = len(aleinu["paragraphs"])

    print(f"   ✓ {total_words} words mapped sequentially (w1 → w{total_words})")
    print(f"   ✓ {total_paragraphs} paragraphs structured")

    print("\n2. Extracting significant phrases...")
    aleinu["phrases"] = extract_phrases_from_words(aleinu)

    repeated = sum(1 for p in aleinu["phrases"].values() if p["frequency"] > 1)
    significant = len(aleinu["phrases"]) - repeated

    print(f"   ✓ {len(aleinu['phrases'])} phrases identified")
    print(f"      - {repeated} repeated phrases")
    print(f"      - {significant} significant long phrases")

    # Show top repeated phrases
    top_phrases = sorted(
        [p for p in aleinu["phrases"].values() if p["frequency"] > 1],
        key=lambda x: x["frequency"],
        reverse=True
    )[:5]

    if top_phrases:
        print("\n   Top repeated phrases:")
        for p in top_phrases:
            print(f"      - \"{p['hebrew']}\" ({p['frequency']}x)")

    print("\n3. Saving embedded JSON...")
    output_dir = Path('/Users/mordechai/Ohr Avraham Chaim/Siddur/data')
    output_dir.mkdir(exist_ok=True)

    output_path = output_dir / 'aleinu_embedded.json'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(aleinu, f, ensure_ascii=False, indent=2)

    print(f"   ✓ Saved: {output_path}")
    print(f"   ✓ Size: {output_path.stat().st_size / 1024:.1f} KB")

    # Count unique words
    unique_words = len(set(w["hebrew_clean"] for w in aleinu["words"].values()))

    # Summary
    print("\n" + "=" * 70)
    print("STRUCTURE SUMMARY")
    print("=" * 70)
    print(f"Words: {len(aleinu['words'])} (w1 → w{len(aleinu['words'])})")
    print(f"Unique Words: {unique_words}")
    print(f"Paragraphs: {len(aleinu['paragraphs'])} (p1 → p{len(aleinu['paragraphs'])})")
    print(f"Phrases: {len(aleinu['phrases'])} (ph1 → ph{len(aleinu['phrases'])})")
    print("\nParagraph breakdown:")
    for para_id, para in aleinu["paragraphs"].items():
        print(f"  {para_id}: {para['word_count']} words ({para['description']})")

    print("\nMost frequent words:")
    word_freq = {}
    for wid, word in aleinu["words"].items():
        hebrew = word["hebrew_clean"]
        freq = word["frequency_in_aleinu"]
        if hebrew not in word_freq:
            word_freq[hebrew] = freq

    top_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:10]
    for hebrew, count in top_words:
        print(f"  {hebrew}: {count} times")

    print("\n" + "=" * 70)
    print("READY FOR TRANSLATION LAYER")
    print("=" * 70)
    print("Next: Add translations for all words")

if __name__ == '__main__':
    main()
