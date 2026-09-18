#!/usr/bin/env python3
"""Build complete Birkot HaTorah (3 Torah blessings) with translations and shoresh."""

import json
import re
from collections import defaultdict

def get_shared_blessing_roots():
    """Roots that appear in standard blessing formula."""
    return {
        "בָּרוּךְ": {"trans": "Blessed", "root": "ב-ר-כ", "meaning": "blessing, knee", "type": "adjective"},
        "אַתָּה": {"trans": "You are", "root": "א-ת-ת", "meaning": "you (masculine singular)", "type": "pronoun"},
        "ה'": {"trans": "Hashem", "root": "ה-ו-י", "meaning": "God's name (YHVH)", "type": "proper noun"},
        "אֱלהֵינוּ": {"trans": "our God", "root": "א-ל-ה", "meaning": "God, deity", "type": "noun"},
        "מֶלֶךְ": {"trans": "King", "root": "מ-ל-כ", "meaning": "kingship, ruling", "type": "noun"},
        "הָעולָם": {"trans": "of the world / universe", "root": "ע-ל-מ", "meaning": "eternity, world", "type": "noun"},
        "הָעולָם.": {"trans": "of the world / universe", "root": "ע-ל-מ", "meaning": "eternity, world", "type": "noun"},
    }

def get_first_blessing_mappings():
    """Mapping for first Torah blessing - La'asok B'Divrei Torah."""
    mappings = get_shared_blessing_roots()
    mappings.update({
        "אֲשֶׁר": {"trans": "Who", "root": "א-ש-ר", "meaning": "who, which, that", "type": "relative pronoun"},
        "קִדְּשָׁנוּ": {"trans": "sanctified us", "root": "ק-ד-ש", "meaning": "holy, sanctify", "type": "verb"},
        "בְּמִצְותָיו": {"trans": "with His commandments", "root": "צ-ו-ה", "meaning": "command", "type": "noun"},
        "וְצִוָּנוּ": {"trans": "and commanded us", "root": "צ-ו-ה", "meaning": "command", "type": "verb"},
        "לַעֲסוק": {"trans": "to engage / occupy ourselves", "root": "ע-ס-ק", "meaning": "engage, be busy with", "type": "verb"},
        "בְּדִבְרֵי": {"trans": "in the words of", "root": "ד-ב-ר", "meaning": "word, speak", "type": "noun"},
        "תורָה:": {"trans": "Torah", "root": "י-ר-ה", "meaning": "teach, instruct, Torah", "type": "noun"},
    })
    return mappings

def get_second_blessing_mappings():
    """Mapping for second Torah blessing - V'Ha'arev Na."""
    mappings = get_shared_blessing_roots()
    mappings.update({
        "וְהַעֲרֶב": {"trans": "And make sweet / pleasant", "root": "ע-ר-ב", "meaning": "sweet, pleasant, evening", "type": "verb"},
        "נָא": {"trans": "please", "root": "נ-א-א", "meaning": "please, I pray", "type": "particle"},
        "אֶת": {"trans": "(direct object marker)", "root": "א-ת-ת", "meaning": "direct object marker", "type": "particle"},
        "דִּבְרֵי": {"trans": "the words of", "root": "ד-ב-ר", "meaning": "word, speak", "type": "noun"},
        "תורָתְךָ": {"trans": "Your Torah", "root": "י-ר-ה", "meaning": "teach, instruct, Torah", "type": "noun"},
        "בְּפִינוּ": {"trans": "in our mouth", "root": "פ-ה-ה", "meaning": "mouth", "type": "noun"},
        "וּבְפִיּות": {"trans": "and in the mouths of", "root": "פ-ה-ה", "meaning": "mouth", "type": "noun"},
        "עַמְּךָ": {"trans": "Your nation", "root": "ע-מ-מ", "meaning": "nation, people", "type": "noun"},
        "בֵּית": {"trans": "house of", "root": "ב-י-ת", "meaning": "house", "type": "noun"},
        "יִשרָאֵל.": {"trans": "Israel", "root": "י-ש-ר", "meaning": "straight, Israel", "type": "proper noun"},
        "יִשרָאֵל:": {"trans": "Israel", "root": "י-ש-ר", "meaning": "straight, Israel", "type": "proper noun"},
        "וְנִהְיֶה": {"trans": "and we will be", "root": "ה-י-ה", "meaning": "be, exist, become", "type": "verb"},
        "אֲנַחְנוּ": {"trans": "we", "root": "א-נ-ח", "meaning": "we, us", "type": "pronoun"},
        "וְצֶאֱצָאֵינוּ.": {"trans": "and our descendants", "root": "י-צ-א", "meaning": "go out, offspring", "type": "noun"},
        "וְצֶאֱצָאֵינוּ": {"trans": "and our descendants", "root": "י-צ-א", "meaning": "go out, offspring", "type": "noun"},
        "וְצֶאֱצָאֵי": {"trans": "and the descendants of", "root": "י-צ-א", "meaning": "go out, offspring", "type": "noun"},
        "צֶאֱצָאֵינוּ": {"trans": "our descendants", "root": "י-צ-א", "meaning": "go out, offspring", "type": "noun"},
        "כֻּלָּנוּ": {"trans": "all of us", "root": "כ-ל-ל", "meaning": "all, every", "type": "noun"},
        "יודְעֵי": {"trans": "knowers of", "root": "י-ד-ע", "meaning": "know", "type": "verb"},
        "שְׁמֶךָ": {"trans": "Your Name", "root": "ש-מ-מ", "meaning": "name", "type": "noun"},
        "וְלומְדֵי": {"trans": "and students of", "root": "ל-מ-ד", "meaning": "learn, teach", "type": "verb"},
        "תורָתֶךָ": {"trans": "Your Torah", "root": "י-ר-ה", "meaning": "teach, instruct, Torah", "type": "noun"},
        "לִשְׁמָהּ:": {"trans": "for its own sake", "root": "ש-מ-מ", "meaning": "name, for its sake", "type": "noun"},
        "הַמְלַמֵּד": {"trans": "Who teaches", "root": "ל-מ-ד", "meaning": "learn, teach", "type": "verb"},
        "תּורָה": {"trans": "Torah", "root": "י-ר-ה", "meaning": "teach, instruct, Torah", "type": "noun"},
        "לְעַמּו": {"trans": "to His nation", "root": "ע-מ-מ", "meaning": "nation, people", "type": "noun"},
        "יִשרָאֵל": {"trans": "Israel", "root": "י-ש-ר", "meaning": "straight, Israel", "type": "proper noun"},
    })
    return mappings

def get_third_blessing_mappings():
    """Mapping for third Torah blessing - Asher Bachar Banu."""
    mappings = get_shared_blessing_roots()
    mappings.update({
        "אֲשֶׁר": {"trans": "Who", "root": "א-ש-ר", "meaning": "who, which, that", "type": "relative pronoun"},
        "בָּחַר": {"trans": "chose", "root": "ב-ח-ר", "meaning": "choose, select", "type": "verb"},
        "בָּנוּ": {"trans": "us", "root": "ב-נ-נ", "meaning": "in us", "type": "preposition+pronoun"},
        "מִכָּל": {"trans": "from all", "root": "כ-ל-ל", "meaning": "all, every", "type": "noun"},
        "הָעַמִּים": {"trans": "the nations", "root": "ע-מ-מ", "meaning": "nation, people", "type": "noun"},
        "וְנָתַן": {"trans": "and gave", "root": "נ-ת-נ", "meaning": "give", "type": "verb"},
        "לָנוּ": {"trans": "to us", "root": "ל", "meaning": "to, for", "type": "preposition"},
        "אֶת": {"trans": "(direct object marker)", "root": "א-ת-ת", "meaning": "direct object marker", "type": "particle"},
        "תּורָתו:": {"trans": "His Torah", "root": "י-ר-ה", "meaning": "teach, instruct, Torah", "type": "noun"},
        "ה'.": {"trans": "Hashem", "root": "ה-ו-י", "meaning": "God's name (YHVH)", "type": "proper noun"},
        "נותֵן": {"trans": "Giver of", "root": "נ-ת-נ", "meaning": "give", "type": "verb"},
        "הַתּורָה:": {"trans": "the Torah", "root": "י-ר-ה", "meaning": "teach, instruct, Torah", "type": "noun"},
    })
    return mappings

def build_blessing(text, mappings, blessing_name, hebrew_name):
    """Build embedded JSON for a single blessing."""

    # Parse words
    final_words = text.replace('.', '. ').replace(':', ': ').split()

    # Initialize structure
    blessing = {
        "prayer_name": {
            "hebrew": hebrew_name,
            "english": blessing_name
        },
        "words": {},
        "sentences": {}
    }

    # Count word frequency
    word_frequency = defaultdict(int)
    for raw_word in final_words:
        word_clean = re.sub(r'[׃:.]', '', raw_word)
        word_frequency[word_clean] += 1

    # Build words
    word_id = 1
    sentence_num = 1
    sentence_word_ids = []

    for raw_word in final_words:
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
            "frequency_in_blessing": word_frequency[word_clean]
        }

        if mapping:
            word_entry["translation"] = mapping["trans"]
            word_entry["shoresh"] = {
                "root": mapping["root"],
                "root_letters": list(mapping["root"].split("-")),
                "meaning": mapping["meaning"],
                "word_type": mapping["type"]
            }

        blessing["words"][f"w{word_id}"] = word_entry
        sentence_word_ids.append(f"w{word_id}")

        # Check if end of sentence
        if ':' in punctuation or '.' in punctuation:
            blessing["sentences"][f"s{sentence_num}"] = {
                "id": f"s{sentence_num}",
                "word_ids": sentence_word_ids,
                "hebrew": ' '.join(blessing["words"][wid]["hebrew"] for wid in sentence_word_ids)
            }
            sentence_num += 1
            sentence_word_ids = []

        word_id += 1

    # Calculate shoresh frequencies
    root_counts = defaultdict(int)
    for word in blessing["words"].values():
        if "shoresh" in word:
            root_counts[word["shoresh"]["root"]] += 1

    for word in blessing["words"].values():
        if "shoresh" in word:
            word["shoresh"]["frequency_in_blessing"] = root_counts[word["shoresh"]["root"]]

    return blessing

def main():
    # Three blessings
    blessings_data = [
        {
            "text": "בָּרוּךְ אַתָּה ה' אֱלהֵינוּ מֶלֶךְ הָעולָם אֲשֶׁר קִדְּשָׁנוּ בְּמִצְותָיו וְצִוָּנוּ לַעֲסוק בְּדִבְרֵי תורָה:",
            "mappings": get_first_blessing_mappings(),
            "filename": "birkat_hatorah_1_laasok",
            "name": "Birkat HaTorah 1 - La'asok",
            "hebrew": "לַעֲסוק בְּדִבְרֵי תורָה"
        },
        {
            "text": "וְהַעֲרֶב נָא ה' אֱלהֵינוּ אֶת דִּבְרֵי תורָתְךָ בְּפִינוּ וּבְפִיּות עַמְּךָ בֵּית יִשרָאֵל. וְנִהְיֶה אֲנַחְנוּ וְצֶאֱצָאֵינוּ. וְצֶאֱצָאֵי צֶאֱצָאֵינוּ וְצֶאֱצָאֵי עַמְּךָ בֵּית יִשרָאֵל. כֻּלָּנוּ יודְעֵי שְׁמֶךָ וְלומְדֵי תורָתֶךָ לִשְׁמָהּ: בָּרוּךְ אַתָּה ה' הַמְלַמֵּד תּורָה לְעַמּו יִשרָאֵל:",
            "mappings": get_second_blessing_mappings(),
            "filename": "birkat_hatorah_2_vhaarev",
            "name": "Birkat HaTorah 2 - V'Ha'arev Na",
            "hebrew": "וְהַעֲרֶב נָא"
        },
        {
            "text": "בָּרוּךְ אַתָּה ה' אֱלהֵינוּ מֶלֶךְ הָעולָם. אֲשֶׁר בָּחַר בָּנוּ מִכָּל הָעַמִּים וְנָתַן לָנוּ אֶת תּורָתו: בָּרוּךְ אַתָּה ה'. נותֵן הַתּורָה:",
            "mappings": get_third_blessing_mappings(),
            "filename": "birkat_hatorah_3_asher_bachar",
            "name": "Birkat HaTorah 3 - Asher Bachar",
            "hebrew": "אֲשֶׁר בָּחַר בָּנוּ"
        }
    ]

    print("="*60)
    print("Building Birkot HaTorah (3 Torah Blessings)")
    print("="*60)

    total_words = 0
    total_roots = set()

    for blessing_data in blessings_data:
        print(f"\nBuilding {blessing_data['name']}...")

        blessing = build_blessing(
            blessing_data["text"],
            blessing_data["mappings"],
            blessing_data["name"],
            blessing_data["hebrew"]
        )

        # Save
        filename = f"data/{blessing_data['filename']}_embedded.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(blessing, f, ensure_ascii=False, indent=2)

        # Stats
        words = len(blessing["words"])
        with_trans = sum(1 for w in blessing["words"].values() if "translation" in w)
        with_shoresh = sum(1 for w in blessing["words"].values() if "shoresh" in w)
        unique_roots = set(w["shoresh"]["root"] for w in blessing["words"].values() if "shoresh" in w)

        print(f"   Words: {words}")
        print(f"   Translations: {with_trans}/{words} ({100*with_trans/words:.1f}%)")
        print(f"   With shoresh: {with_shoresh}/{words} ({100*with_shoresh/words:.1f}%)")
        print(f"   Unique roots: {len(unique_roots)}")
        print(f"   Sentences: {len(blessing['sentences'])}")

        total_words += words
        total_roots.update(unique_roots)

    print("\n" + "="*60)
    print("BIRKOT HATORAH COMPLETE")
    print("="*60)
    print(f"Total words across 3 blessings: {total_words}")
    print(f"Total unique roots: {len(total_roots)}")
    print("✅ All Torah blessings complete!")

if __name__ == "__main__":
    main()
