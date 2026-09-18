#!/usr/bin/env python3
"""Build complete Asher Yatzar bracha with translations and shoresh."""

import json
import re
from collections import defaultdict

def get_word_mappings():
    """Complete mappings for all words in Asher Yatzar."""
    return {
        # Opening blessing formula (shared)
        "בָּרוּךְ": {"trans": "Blessed", "root": "ב-ר-כ", "meaning": "blessing, knee", "type": "adjective"},
        "אַתָּה": {"trans": "You are", "root": "א-ת-ת", "meaning": "you (masculine singular)", "type": "pronoun"},
        "ה'": {"trans": "Hashem", "root": "ה-ו-י", "meaning": "God's name (YHVH)", "type": "proper noun"},
        "אֱלהֵינוּ": {"trans": "our God", "root": "א-ל-ה", "meaning": "God, deity", "type": "noun"},
        "מֶלֶךְ": {"trans": "King", "root": "מ-ל-כ", "meaning": "kingship, ruling", "type": "noun"},
        "הָעולָם": {"trans": "of the world / universe", "root": "ע-ל-מ", "meaning": "eternity, world", "type": "noun"},

        # Specific content
        "אֲשֶׁר": {"trans": "Who", "root": "א-ש-ר", "meaning": "who, which, that", "type": "relative pronoun"},
        "יָצַר": {"trans": "formed / created", "root": "י-צ-ר", "meaning": "form, create", "type": "verb"},
        "אֶת": {"trans": "(direct object marker)", "root": "א-ת-ת", "meaning": "direct object marker", "type": "particle"},
        "הָאָדָם": {"trans": "the human / man", "root": "א-ד-מ", "meaning": "human, man, earth", "type": "noun"},
        "בְּחָכְמָה": {"trans": "with wisdom", "root": "ח-כ-מ", "meaning": "wisdom", "type": "noun"},
        "וּבָרָא": {"trans": "and created", "root": "ב-ר-א", "meaning": "create (ex nihilo)", "type": "verb"},
        "בו": {"trans": "in him / it", "root": "ב-ב-ב", "meaning": "in, with", "type": "preposition"},
        "נְקָבִים": {"trans": "orifices / openings", "root": "נ-ק-ב", "meaning": "hole, opening", "type": "noun"},
        "חֲלוּלִים": {"trans": "hollow spaces / cavities", "root": "ח-ל-ל", "meaning": "hollow, empty", "type": "noun"},
        "גָּלוּי": {"trans": "revealed / known", "root": "ג-ל-ה", "meaning": "reveal, uncover", "type": "adjective"},
        "וְיָדוּעַ": {"trans": "and known", "root": "י-ד-ע", "meaning": "know", "type": "adjective"},
        "לִפְנֵי": {"trans": "before", "root": "פ-נ-נ", "meaning": "face, before", "type": "preposition"},
        "כִסֵּא": {"trans": "throne", "root": "כ-ס-א", "meaning": "throne, seat", "type": "noun"},
        "כְבודֶךָ": {"trans": "Your glory", "root": "כ-ב-ד", "meaning": "weight, glory, honor", "type": "noun"},
        "שֶׁאִם": {"trans": "that if", "root": "א-מ-מ", "meaning": "if, when (conditional)", "type": "conjunction"},
        "יִפָּתֵחַ": {"trans": "should open / be opened", "root": "פ-ת-ח", "meaning": "open", "type": "verb"},
        "אֶחָד": {"trans": "one", "root": "א-ח-ד", "meaning": "one, unity", "type": "number"},
        "מֵהֶם": {"trans": "from them", "root": "ה-מ-מ", "meaning": "they, them", "type": "pronoun"},
        "או": {"trans": "or", "root": "א-ו-ו", "meaning": "or", "type": "conjunction"},
        "יִסָּתֵם": {"trans": "should close / be blocked", "root": "ס-ת-מ", "meaning": "close, block", "type": "verb"},
        "אִי": {"trans": "not / impossible", "root": "א-י-י", "meaning": "not, non-", "type": "negative particle"},
        "אֶפְשַׁר": {"trans": "possible", "root": "פ-ש-ר", "meaning": "possible, permit", "type": "adjective"},
        "לְהִתְקַיֵּם": {"trans": "to exist / survive", "root": "ק-ו-מ", "meaning": "stand, exist", "type": "verb"},
        "וְלַעֲמוד": {"trans": "and to stand", "root": "ע-מ-ד", "meaning": "stand", "type": "verb"},
        "לְפָנֶיךָ": {"trans": "before You", "root": "פ-נ-נ", "meaning": "face, before", "type": "preposition"},
        "אֲפִילוּ": {"trans": "even", "root": "א-פ-ל", "meaning": "even, also", "type": "adverb"},
        "שָׁעָה": {"trans": "hour / moment", "root": "ש-ע-ה", "meaning": "hour, time", "type": "noun"},
        "אֶחָת:": {"trans": "one", "root": "א-ח-ד", "meaning": "one, unity", "type": "number"},

        # Closing blessing
        "רופֵא": {"trans": "Healer of", "root": "ר-פ-א", "meaning": "heal, cure", "type": "verb"},
        "כָל": {"trans": "all", "root": "כ-ל-ל", "meaning": "all, every", "type": "noun"},
        "בָּשר": {"trans": "flesh", "root": "ב-ש-ר", "meaning": "flesh, meat", "type": "noun"},
        "וּמַפְלִיא": {"trans": "and does wondrously", "root": "פ-ל-א", "meaning": "wonder, miracle", "type": "verb"},
        "לַעֲשות:": {"trans": "to do / make", "root": "ע-ש-ה", "meaning": "do, make", "type": "verb"},
    }

def build_asher_yatzar():
    """Build complete embedded JSON for Asher Yatzar."""

    # Hebrew text
    text = "בָּרוּךְ אַתָּה ה' אֱלהֵינוּ מֶלֶךְ הָעולָם אֲשֶׁר יָצַר אֶת הָאָדָם בְּחָכְמָה וּבָרָא בו נְקָבִים נְקָבִים חֲלוּלִים חֲלוּלִים. גָּלוּי וְיָדוּעַ לִפְנֵי כִסֵּא כְבודֶךָ שֶׁאִם יִפָּתֵחַ אֶחָד מֵהֶם או יִסָּתֵם אֶחָד מֵהֶם אִי אֶפְשַׁר לְהִתְקַיֵּם וְלַעֲמוד לְפָנֶיךָ אֲפִילוּ שָׁעָה אֶחָת: בָּרוּךְ אַתָּה ה' רופֵא כָל בָּשר וּמַפְלִיא לַעֲשות:"

    # Split into sentences
    sentences = [s.strip() for s in text.split(':') if s.strip()]

    # Parse all words
    all_words = []
    for sentence in sentences:
        words = sentence.split()
        all_words.extend(words)

    # Add back punctuation for last word in each sentence
    final_text_words = text.replace('.', '. ').replace(':', ': ').split()

    # Get mappings
    mappings = get_word_mappings()

    # Initialize structure
    bracha = {
        "prayer_name": {
            "hebrew": "אֲשֶׁר יָצַר",
            "english": "Asher Yatzar",
            "translation": "Who Formed [the Human]"
        },
        "words": {},
        "sentences": {},
        "blessing_formula": {
            "opening": "בָּרוּךְ אַתָּה ה' אֱלהֵינוּ מֶלֶךְ הָעולָם",
            "opening_translation": "Blessed are You, Hashem our God, King of the universe",
            "closing": "בָּרוּךְ אַתָּה ה' רופֵא כָל בָּשר וּמַפְלִיא לַעֲשות",
            "closing_translation": "Blessed are You, Hashem, Healer of all flesh and does wondrous things"
        }
    }

    # Count word frequency
    word_frequency = defaultdict(int)
    for raw_word in final_text_words:
        word_clean = re.sub(r'[׃:.]', '', raw_word)
        word_frequency[word_clean] += 1

    # Build words
    word_id = 1
    sentence_num = 1
    sentence_word_ids = []

    for raw_word in final_text_words:
        word_clean = re.sub(r'[׃:.]', '', raw_word)
        punctuation = ''
        for char in raw_word:
            if char in '׃:.':
                punctuation += char

        # Get mapping
        mapping = mappings.get(raw_word) or mappings.get(word_clean)

        word_entry = {
            "id": f"w{word_id}",
            "hebrew": raw_word,
            "hebrew_clean": word_clean,
            "punctuation": punctuation,
            "sentence": sentence_num,
            "position_in_sentence": len(sentence_word_ids) + 1,
            "position_global": word_id,
            "frequency_in_asher_yatzar": word_frequency[word_clean]
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
        sentence_word_ids.append(f"w{word_id}")

        # Check if end of sentence
        if ':' in punctuation or '.' in punctuation:
            bracha["sentences"][f"s{sentence_num}"] = {
                "id": f"s{sentence_num}",
                "word_ids": sentence_word_ids,
                "hebrew": ' '.join(bracha["words"][wid]["hebrew"] for wid in sentence_word_ids)
            }
            sentence_num += 1
            sentence_word_ids = []

        word_id += 1

    # Calculate shoresh frequencies
    root_counts = defaultdict(int)
    for word in bracha["words"].values():
        if "shoresh" in word:
            root_counts[word["shoresh"]["root"]] += 1

    for word in bracha["words"].values():
        if "shoresh" in word:
            word["shoresh"]["frequency_in_asher_yatzar"] = root_counts[word["shoresh"]["root"]]

    return bracha

def main():
    print("Building Asher Yatzar bracha...")
    bracha = build_asher_yatzar()

    # Save
    with open('data/asher_yatzar_embedded.json', 'w', encoding='utf-8') as f:
        json.dump(bracha, f, ensure_ascii=False, indent=2)

    # Stats
    total = len(bracha["words"])
    with_trans = sum(1 for w in bracha["words"].values() if "translation" in w)
    with_shoresh = sum(1 for w in bracha["words"].values() if "shoresh" in w)
    unique_roots = len(set(w["shoresh"]["root"] for w in bracha["words"].values() if "shoresh" in w))

    print(f"\n✅ Asher Yatzar complete:")
    print(f"   Total words: {total}")
    print(f"   Translations: {with_trans}/{total} ({100*with_trans/total:.1f}%)")
    print(f"   With shoresh: {with_shoresh}/{total} ({100*with_shoresh/total:.1f}%)")
    print(f"   Unique roots: {unique_roots}")
    print(f"   Sentences: {len(bracha['sentences'])}")

if __name__ == "__main__":
    main()
