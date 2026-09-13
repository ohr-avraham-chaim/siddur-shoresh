#!/usr/bin/env python3
"""
Parse Ashrei into comprehensive word-by-word mapping system.
Implements hybrid "DNA Mapping" + "Layer Cake" approach.
"""

import json
import re
from pathlib import Path
from collections import defaultdict

def parse_ashrei_verses(ashrei_text):
    """Parse clean Ashrei text into structured verse data."""
    lines = ashrei_text.strip().split('\n')
    verses = []

    for i, line in enumerate(lines, 1):
        line = line.strip()
        if not line:
            continue

        # Split into words (preserving punctuation)
        words = line.split()

        verse = {
            'verse_number': i,
            'full_text': line,
            'words': [],
            'word_count': len(words)
        }

        for pos, word in enumerate(words, 1):
            # Extract root word and punctuation
            word_clean = re.sub(r'[׃:.]$', '', word)  # Remove trailing punctuation
            punctuation = word[len(word_clean):] if len(word) > len(word_clean) else ''

            word_data = {
                'position': pos,
                'word': word,
                'word_clean': word_clean,
                'punctuation': punctuation,
                'verse': i,
                'global_position': sum(len(lines[j].split()) for j in range(i-1)) + pos
            }
            verse['words'].append(word_data)

        verses.append(verse)

    return verses

def extract_phrases(verses, min_words=2, max_words=8):
    """
    Extract all possible phrases from Ashrei.
    Track every occurrence for DNA mapping.
    """
    phrases = defaultdict(list)

    for verse in verses:
        words = verse['words']

        # Extract phrases of varying lengths
        for length in range(min_words, min(max_words + 1, len(words) + 1)):
            for start in range(len(words) - length + 1):
                # Build phrase
                phrase_words = words[start:start + length]
                phrase_text = ' '.join(w['word_clean'] for w in phrase_words)

                occurrence = {
                    'verse': verse['verse_number'],
                    'position_in_verse': start + 1,
                    'word_count': length,
                    'full_context': verse['full_text'],
                    'words': phrase_words
                }

                phrases[phrase_text].append(occurrence)

    # Filter to only phrases that appear more than once OR are significant single occurrences
    significant_phrases = {}
    for phrase, occurrences in phrases.items():
        if len(occurrences) > 1:  # Repeated phrases
            significant_phrases[phrase] = {
                'hebrew': phrase,
                'frequency': len(occurrences),
                'occurrences': occurrences,
                'category': 'repeated'
            }
        elif len(phrase.split()) >= 4:  # Long phrases (significant even if once)
            significant_phrases[phrase] = {
                'hebrew': phrase,
                'frequency': 1,
                'occurrences': occurrences,
                'category': 'significant_long'
            }

    return significant_phrases

def load_translations():
    """Load all 6 English translation sources."""
    base_path = Path('/Users/mordechai/Ohr Avraham Chaim/Siddur')

    translation_files = [
        'Siddur Ashkenaz - en - merged.json',
        'Siddur Ashkenaz - en - Translation based on the Metsudah linear siddur, by Avrohom Davis, 1981.json',
        'Siddur Ashkenaz - en - Ha-Siddur Ha-Shalem (1949).json',
        'Siddur Ashkenaz - en - The Standard Prayer Book, tr. by Simeon Singer, [1915].json',
        'Siddur Ashkenaz - en - Sefaria Community Translation.json',
        'Siddur Ashkenaz - en - Siddur sha\'ar zahav.json'
    ]

    translations = {}

    for filename in translation_files:
        filepath = base_path / filename
        if filepath.exists():
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # Extract translation name
            version_name = data.get('versionTitle', 'Unknown')

            # Try to find Ashrei in the structure
            # Structure: text -> Weekday -> Shacharit -> Pesukei Dezimra -> Ashrei
            try:
                ashrei_data = data['text']['Weekday']['Shacharit']['Pesukei Dezimra']['Ashrei']
                if ashrei_data and len(ashrei_data) > 2:  # Has actual content
                    translations[version_name] = ashrei_data
            except (KeyError, TypeError):
                # Try alternate paths
                pass

    return translations

def create_ashrei_database(verses, phrases, translations):
    """
    Create comprehensive Ashrei database.
    Hybrid "DNA Mapping" + "Layer Cake" structure.
    """
    database = {
        'metadata': {
            'prayer_name_hebrew': 'אַשְׁרֵי',
            'prayer_name_english': 'Ashrei',
            'source': 'Psalm 145 with introductory verses',
            'total_verses': len(verses),
            'total_words': sum(v['word_count'] for v in verses),
            'total_phrases': len(phrases)
        },
        'verses': verses,
        'phrases': phrases,
        'translations': translations,
        'structure': {
            'introduction': {
                'verses': [1, 2],
                'description': 'Opening verses (Psalm 84:5, 144:15)'
            },
            'psalm_145': {
                'verses': list(range(3, 24)),
                'description': 'Psalm 145 - alphabetic acrostic (missing נ)',
                'acrostic': True
            },
            'conclusion': {
                'verses': [24],
                'description': 'Closing verse (Psalm 115:18)'
            }
        },
        'word_index': build_word_index(verses),
        'approved_translations': {},  # To be filled by user
        'kavanot': {},  # To be filled with intentions
        'instructions': {
            'when': 'Three times daily - Shacharit (twice), Mincha',
            'posture': 'Standing preferred during Psukei Dezimra',
            'focus': 'Verse 16 (פותח את ידך) said with special concentration',
            'custom': 'Some say verse 1-2 sitting, stand for verse 3 (תהלה לדוד)'
        }
    }

    return database

def build_word_index(verses):
    """Build complete word index for fast lookup."""
    word_index = defaultdict(list)

    for verse in verses:
        for word_data in verse['words']:
            word_clean = word_data['word_clean']
            word_index[word_clean].append({
                'verse': verse['verse_number'],
                'position': word_data['position'],
                'full_word': word_data['word'],
                'context': verse['full_text']
            })

    return dict(word_index)

def main():
    print("=" * 70)
    print("PARSING ASHREI - COMPREHENSIVE MAPPING SYSTEM")
    print("=" * 70)

    # Load clean Ashrei text
    ashrei_path = Path('/Users/mordechai/Ohr Avraham Chaim/Siddur/clean_ashrei.md')
    with open(ashrei_path, 'r', encoding='utf-8') as f:
        ashrei_text = f.read()

    print(f"\n1. Parsing {len(ashrei_text.split())} words from clean Ashrei text...")
    verses = parse_ashrei_verses(ashrei_text)
    print(f"   ✓ Parsed {len(verses)} verses")
    print(f"   ✓ Total words: {sum(v['word_count'] for v in verses)}")

    print("\n2. Extracting phrases and tracking occurrences...")
    phrases = extract_phrases(verses)
    print(f"   ✓ Found {len(phrases)} significant phrases")

    # Show most repeated phrases
    repeated = [(p, data['frequency']) for p, data in phrases.items() if data['frequency'] > 1]
    repeated_sorted = sorted(repeated, key=lambda x: x[1], reverse=True)
    print(f"   ✓ {len(repeated)} repeated phrases (top 5):")
    for phrase, freq in repeated_sorted[:5]:
        print(f"      - \"{phrase}\" appears {freq} times")

    print("\n3. Loading translation sources...")
    translations = load_translations()
    print(f"   ✓ Loaded {len(translations)} translation sources")
    for name in translations.keys():
        print(f"      - {name}")

    print("\n4. Building comprehensive database...")
    database = create_ashrei_database(verses, phrases, translations)

    # Save to JSON
    output_dir = Path('/Users/mordechai/Ohr Avraham Chaim/Siddur/data')
    output_dir.mkdir(exist_ok=True)

    output_path = output_dir / 'ashrei_comprehensive.json'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(database, f, ensure_ascii=False, indent=2)

    print(f"   ✓ Database saved: {output_path}")

    # Generate summary report
    print("\n" + "=" * 70)
    print("ASHREI DATABASE SUMMARY")
    print("=" * 70)
    print(f"Total Verses: {database['metadata']['total_verses']}")
    print(f"Total Words: {database['metadata']['total_words']}")
    print(f"Total Phrases: {database['metadata']['total_phrases']}")
    print(f"Unique Words: {len(database['word_index'])}")
    print(f"Translation Sources: {len(database['translations'])}")
    print("\nMost Common Words:")
    word_freq = {word: len(occurrences) for word, occurrences in database['word_index'].items()}
    top_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:10]
    for word, count in top_words:
        print(f"  {word}: {count} times")

    print("\n" + "=" * 70)

if __name__ == '__main__':
    main()
