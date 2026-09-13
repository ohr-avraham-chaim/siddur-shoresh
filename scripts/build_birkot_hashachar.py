#!/usr/bin/env python3
"""Build complete Birkot HaShachar (15 morning blessings + Yehi Ratzon prayer)."""

import json
import re
from collections import defaultdict

def get_common_mappings():
    """Common blessing formula mappings."""
    return {
        "בָּרוּךְ": {"trans": "Blessed", "root": "ב-ר-כ", "meaning": "blessing, knee", "type": "adjective"},
        "אַתָּה": {"trans": "You are", "root": "א-ת-ת", "meaning": "you (masculine singular)", "type": "pronoun"},
        "ה'": {"trans": "Hashem", "root": "ה-ו-י", "meaning": "God's name (YHVH)", "type": "proper noun"},
        "אֱלהֵינוּ": {"trans": "our God", "root": "א-ל-ה", "meaning": "God, deity", "type": "noun"},
        "אֱלֹהֵינוּ": {"trans": "our God", "root": "א-ל-ה", "meaning": "God, deity", "type": "noun"},
        "מֶלֶךְ": {"trans": "King", "root": "מ-ל-כ", "meaning": "kingship, ruling", "type": "noun"},
        "הָעולָם": {"trans": "of the world / universe", "root": "ע-ל-מ", "meaning": "eternity, world", "type": "noun"},
        "הָעולָם.": {"trans": "of the world / universe", "root": "ע-ל-מ", "meaning": "eternity, world", "type": "noun"},
        "הָעוֹלָם,": {"trans": "of the world / universe", "root": "ע-ל-מ", "meaning": "eternity, world", "type": "noun"},
    }

def get_blessings_mappings():
    """All unique word mappings for the 15 blessings."""
    mappings = get_common_mappings()
    mappings.update({
        # Blessing 1 - Rooster/understanding
        "אֲשֶׁר": {"trans": "Who", "root": "א-ש-ר", "meaning": "who, which, that", "type": "relative pronoun"},
        "נָתַן": {"trans": "gave", "root": "נ-ת-נ", "meaning": "give", "type": "verb"},
        "לַשּכְוִי": {"trans": "to the rooster / mind", "root": "ש-כ-ו", "meaning": "rooster, understanding", "type": "noun"},
        "בִינָה": {"trans": "understanding / discernment", "root": "ב-י-נ", "meaning": "between, understanding", "type": "noun"},
        "לְהַבְחִין": {"trans": "to distinguish", "root": "ב-ח-ן", "meaning": "test, distinguish", "type": "verb"},
        "בֵּין": {"trans": "between", "root": "ב-י-נ", "meaning": "between", "type": "preposition"},
        "יום": {"trans": "day", "root": "י-ו-מ", "meaning": "day", "type": "noun"},
        "וּבֵין": {"trans": "and between", "root": "ב-י-נ", "meaning": "between", "type": "preposition"},
        "לָיְלָה.": {"trans": "night", "root": "ל-י-ל", "meaning": "night", "type": "noun"},

        # Blessings 2-4 - Identity blessings
        "שֶׁלּא": {"trans": "who did not", "root": "ש-ל-א", "meaning": "that not", "type": "conjunction"},
        "שֶׁלֹּא": {"trans": "who did not", "root": "ש-ל-א", "meaning": "that not", "type": "conjunction"},
        "עָשנִי": {"trans": "make me", "root": "ע-ש-ה", "meaning": "do, make", "type": "verb"},
        "עָשַׂנִי": {"trans": "make me", "root": "ע-ש-ה", "meaning": "do, make", "type": "verb"},
        "גּוי.": {"trans": "a non-Jew / gentile", "root": "ג-ו-י", "meaning": "nation, gentile", "type": "noun"},
        "עָבֶד.": {"trans": "a slave", "root": "ע-ב-ד", "meaning": "slave, servant", "type": "noun"},
        "אשָּׁה.": {"trans": "a woman", "root": "א-ש-ה", "meaning": "woman, wife", "type": "noun"},
        "שֶׁעָשַׂנִי": {"trans": "Who made me", "root": "ע-ש-ה", "meaning": "do, make", "type": "verb"},
        "כִּרְצוֹנוֹ.": {"trans": "according to His will", "root": "ר-צ-ה", "meaning": "will, desire, favor", "type": "noun"},

        # Blessing 5 - Opens eyes of blind
        "פּוקֵחַ": {"trans": "Who opens", "root": "פ-ק-ח", "meaning": "open (eyes)", "type": "verb"},
        "עִוְרִים.": {"trans": "the blind", "root": "ע-ו-ר", "meaning": "blind", "type": "adjective"},

        # Blessing 6 - Clothes naked
        "מַלְבִּישׁ": {"trans": "Who clothes", "root": "ל-ב-ש", "meaning": "wear, clothe", "type": "verb"},
        "עֲרֻמִּים.": {"trans": "the naked", "root": "ע-ר-מ", "meaning": "naked, bare", "type": "adjective"},

        # Blessing 7 - Frees bound
        "מַתִּיר": {"trans": "Who frees / releases", "root": "נ-ת-ר", "meaning": "loosen, permit", "type": "verb"},
        "אֲסוּרִים.": {"trans": "the bound / imprisoned", "root": "א-ס-ר", "meaning": "bind, imprison", "type": "adjective"},

        # Blessing 8 - Straightens bent
        "זוקֵף": {"trans": "Who straightens", "root": "ז-ק-פ", "meaning": "raise, straighten", "type": "verb"},
        "כְּפוּפִים.": {"trans": "the bent / stooped", "root": "כ-פ-פ", "meaning": "bend, stoop", "type": "adjective"},

        # Blessing 9 - Spreads earth on waters
        "רוקַע": {"trans": "Who spreads / stretches", "root": "ר-ק-ע", "meaning": "spread, stamp", "type": "verb"},
        "הָאָרֶץ": {"trans": "the earth", "root": "א-ר-ץ", "meaning": "earth, land", "type": "noun"},
        "עַל": {"trans": "upon", "root": "ע-ל-ל", "meaning": "upon, over", "type": "preposition"},
        "הַמָּיִם.": {"trans": "the waters", "root": "מ-י-ם", "meaning": "water", "type": "noun"},

        # Blessing 10 - Provides needs
        "שֶׁעָשה": {"trans": "Who made / provided", "root": "ע-ש-ה", "meaning": "do, make", "type": "verb"},
        "לִּי": {"trans": "for me", "root": "ל", "meaning": "to, for", "type": "preposition"},
        "כָּל": {"trans": "all", "root": "כ-ל-ל", "meaning": "all, every", "type": "noun"},
        "צָרְכִּי.": {"trans": "my needs", "root": "צ-ר-כ", "meaning": "need", "type": "noun"},

        # Blessing 11 - Directs steps
        "הַמֵּכִין": {"trans": "Who directs / prepares", "root": "כ-ו-נ", "meaning": "establish, prepare", "type": "verb"},
        "מִצְעֲדֵי": {"trans": "the steps of", "root": "צ-ע-ד", "meaning": "step, pace", "type": "noun"},
        "גָבֶר.": {"trans": "a man", "root": "ג-ב-ר", "meaning": "man, warrior", "type": "noun"},

        # Blessing 12 - Girds Israel with strength
        "אוזֵר": {"trans": "Who girds / strengthens", "root": "א-ז-ר", "meaning": "gird, strengthen", "type": "verb"},
        "יִשרָאֵל": {"trans": "Israel", "root": "י-ש-ר", "meaning": "straight, Israel", "type": "proper noun"},
        "בִּגְבוּרָה.": {"trans": "with strength / might", "root": "ג-ב-ר", "meaning": "strength, might", "type": "noun"},

        # Blessing 13 - Crowns Israel with glory
        "עוטֵר": {"trans": "Who crowns", "root": "ע-ט-ר", "meaning": "crown, surround", "type": "verb"},
        "בְּתִפְאָרָה.": {"trans": "with glory / beauty", "root": "פ-א-ר", "meaning": "glory, beauty", "type": "noun"},

        # Blessing 14 - Gives strength to weary
        "הַנּותֵן": {"trans": "Who gives", "root": "נ-ת-נ", "meaning": "give", "type": "verb"},
        "לַיָּעֵף": {"trans": "to the weary", "root": "י-ע-פ", "meaning": "weary, tired", "type": "adjective"},
        "כּחַ.": {"trans": "strength", "root": "כ-ח-ח", "meaning": "strength, power", "type": "noun"},

        # Blessing 15 - Removes sleep
        "הַמַּעֲבִיר": {"trans": "Who removes", "root": "ע-ב-ר", "meaning": "pass, remove", "type": "verb"},
        "שֵׁנָה": {"trans": "sleep", "root": "י-ש-נ", "meaning": "sleep", "type": "noun"},
        "מֵעֵינַי": {"trans": "from my eyes", "root": "ע-י-נ", "meaning": "eye", "type": "noun"},
        "וּתְנוּמָה": {"trans": "and slumber", "root": "נ-ו-מ", "meaning": "slumber, drowsiness", "type": "noun"},
        "מֵעַפְעַפָּי.": {"trans": "from my eyelids", "root": "ע-פ-פ", "meaning": "eyelid", "type": "noun"},
    })
    return mappings

def build_fifteen_blessings():
    """Build all 15 blessings as single combined text."""

    blessings_text = [
        "בָּרוּךְ אַתָּה ה' אֱלהֵינוּ מֶלֶךְ הָעולָם. אֲשֶׁר נָתַן לַשּכְוִי בִינָה לְהַבְחִין בֵּין יום וּבֵין לָיְלָה.",
        "בָּרוּךְ אַתָּה ה' אֱלהֵינוּ מֶלֶךְ הָעולָם. שֶׁלּא עָשנִי גּוי.",
        "בָּרוּךְ אַתָּה ה' אֱלהֵינוּ מֶלֶךְ הָעולָם. שֶׁלּא עָשנִי עָבֶד.",
        "בָּרוּךְ אַתָּה ה' אֱלֹהֵינוּ מֶלֶךְ הָעוֹלָם, שֶׁלֹּא עָשַׂנִי אשָּׁה.",
        "בָּרוּךְ אַתָּה ה' אֱלהֵינוּ מֶלֶךְ הָעולָם. פּוקֵחַ עִוְרִים.",
        "בָּרוּךְ אַתָּה ה' אֱלהֵינוּ מֶלֶךְ הָעולָם. מַלְבִּישׁ עֲרֻמִּים.",
        "בָּרוּךְ אַתָּה ה' אֱלהֵינוּ מֶלֶךְ הָעולָם. מַתִּיר אֲסוּרִים.",
        "בָּרוּךְ אַתָּה ה' אֱלהֵינוּ מֶלֶךְ הָעולָם. זוקֵף כְּפוּפִים.",
        "בָּרוּךְ אַתָּה ה' אֱלהֵינוּ מֶלֶךְ הָעולָם. רוקַע הָאָרֶץ עַל הַמָּיִם.",
        "בָּרוּךְ אַתָּה ה' אֱלהֵינוּ מֶלֶךְ הָעולָם. שֶׁעָשה לִּי כָּל צָרְכִּי.",
        "בָּרוּךְ אַתָּה ה' אֱלהֵינוּ מֶלֶךְ הָעולָם. הַמֵּכִין מִצְעֲדֵי גָבֶר.",
        "בָּרוּךְ אַתָּה ה' אֱלהֵינוּ מֶלֶךְ הָעולָם. אוזֵר יִשרָאֵל בִּגְבוּרָה.",
        "בָּרוּךְ אַתָּה ה' אֱלהֵינוּ מֶלֶךְ הָעולָם. עוטֵר יִשרָאֵל בְּתִפְאָרָה.",
        "בָּרוּךְ אַתָּה ה' אֱלהֵינוּ מֶלֶךְ הָעולָם. הַנּותֵן לַיָּעֵף כּחַ.",
        "בָּרוּךְ אַתָּה ה' אֱלהֵינוּ מֶלֶךְ הָעולָם. הַמַּעֲבִיר שֵׁנָה מֵעֵינַי וּתְנוּמָה מֵעַפְעַפָּי."
    ]

    # Combine all blessings
    combined_text = " ".join(blessings_text)

    mappings = get_blessings_mappings()

    # Parse words
    final_words = combined_text.replace('.', '. ').replace(',', ', ').split()

    # Initialize structure
    data = {
        "text_name": {
            "hebrew": "בִּרְכּוֹת הַשַּׁחַר",
            "english": "Birkot HaShachar - Morning Blessings"
        },
        "blessing_count": 15,
        "words": {},
        "blessings": {}
    }

    # Count word frequency
    word_frequency = defaultdict(int)
    for raw_word in final_words:
        word_clean = re.sub(r'[׃:.,]', '', raw_word)
        word_frequency[word_clean] += 1

    # Build words
    word_id = 1
    blessing_num = 1
    blessing_word_ids = []

    for raw_word in final_words:
        word_clean = re.sub(r'[׃:.,]', '', raw_word)
        punctuation = ''
        for char in raw_word:
            if char in '׃:.,':
                punctuation += char

        # Get mapping
        mapping = mappings.get(raw_word) or mappings.get(word_clean)

        word_entry = {
            "id": f"w{word_id}",
            "hebrew": raw_word,
            "hebrew_clean": word_clean,
            "punctuation": punctuation,
            "blessing": blessing_num,
            "position_in_blessing": len(blessing_word_ids) + 1,
            "position_global": word_id,
            "frequency_in_text": word_frequency[word_clean]
        }

        if mapping:
            word_entry["translation"] = mapping["trans"]
            word_entry["shoresh"] = {
                "root": mapping["root"],
                "root_letters": list(mapping["root"].split("-")) if "-" in mapping["root"] else [mapping["root"]],
                "meaning": mapping["meaning"],
                "word_type": mapping["type"]
            }

        data["words"][f"w{word_id}"] = word_entry
        blessing_word_ids.append(f"w{word_id}")

        # Check if end of blessing
        if '.' in punctuation:
            data["blessings"][f"b{blessing_num}"] = {
                "id": f"b{blessing_num}",
                "word_ids": blessing_word_ids,
                "hebrew": ' '.join(data["words"][wid]["hebrew"] for wid in blessing_word_ids)
            }
            blessing_num += 1
            blessing_word_ids = []

        word_id += 1

    # Calculate shoresh frequencies
    root_counts = defaultdict(int)
    for word in data["words"].values():
        if "shoresh" in word:
            root_counts[word["shoresh"]["root"]] += 1

    for word in data["words"].values():
        if "shoresh" in word:
            word["shoresh"]["frequency_in_text"] = root_counts[word["shoresh"]["root"]]

    return data

def main():
    print("="*60)
    print("Building Birkot HaShachar - 15 Morning Blessings")
    print("="*60)

    blessings = build_fifteen_blessings()

    # Save
    filename = 'data/birkot_hashachar_embedded.json'
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(blessings, f, ensure_ascii=False, indent=2)

    # Stats
    total = len(blessings["words"])
    with_trans = sum(1 for w in blessings["words"].values() if "translation" in w)
    with_shoresh = sum(1 for w in blessings["words"].values() if "shoresh" in w)
    unique_roots = len(set(w["shoresh"]["root"] for w in blessings["words"].values() if "shoresh" in w))

    print(f"\n✅ Birkot HaShachar complete:")
    print(f"   Total blessings: {blessings['blessing_count']}")
    print(f"   Total words: {total}")
    print(f"   Translations: {with_trans}/{total} ({100*with_trans/total:.1f}%)")
    print(f"   With shoresh: {with_shoresh}/{total} ({100*with_shoresh/total:.1f}%)")
    print(f"   Unique roots: {unique_roots}")
    print("="*60)

if __name__ == "__main__":
    main()
