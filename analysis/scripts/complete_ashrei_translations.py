#!/usr/bin/env python3
"""
Complete translation map for all 137 unique words in Ashrei.
Uses exact Hebrew from the JSON (with nikud).
"""

import json
from pathlib import Path

def load_ashrei():
    path = Path('/Users/mordechai/Ohr Avraham Chaim/Siddur/data/ashrei_embedded.json')
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_ashrei(ashrei):
    path = Path('/Users/mordechai/Ohr Avraham Chaim/Siddur/data/ashrei_embedded.json')
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(ashrei, f, ensure_ascii=False, indent=2)
    print(f"✓ Saved all translations to {path}")

def get_complete_translation_map():
    """
    Complete translation map for ALL words in Ashrei.
    Uses exact Hebrew with nikud as it appears in the JSON.
    """
    return {
        # Already translated (91 words) - keeping existing
        "בֵיתֶךָ": "in Your house",
        "עוד": "continually",
        "יְהַלְלוּךָ": "they will praise You",
        "הָעָם": "the people",
        "לּו": "for them",
        "שה'": "that Hashem",
        "אֱלהָיו": "their God",
        "לְדָוִד": "of David",
        "אֲרומִמְךָ": "I will exalt You",
        "אֱלוהַי": "my God",
        "וַאֲבָרְכָה": "and I will bless",
        "לְעולָם": "forever",
        "וָעֶד": "and ever",
        "יום": "day",
        "וַאֲהַלְלָה": "and I will praise",
        "מְאד": "exceedingly",
        "אֵין": "there is no",
        "חֵקֶר": "limit",
        "דּור": "generation",
        "לְדור": "to generation",
        "מַעֲשיךָ": "Your works",
        "וּגְבוּרתֶיךָ": "and Your mighty acts",
        "הֲדַר": "the splendor of",
        "הודֶךָ": "Your majesty",
        "וְדִבְרֵי": "and the words of",
        "נִפְלְאתֶיךָ": "Your wonders",
        "אָשיחָה": "I will speak",
        "וֶעֱזוּז": "And the might of",
        "נורְאתֶיךָ": "Your awesome deeds",
        "יאמֵרוּ": "they will speak",
        "זֵכֶר": "The remembrance of",
        "רַב": "abundant",
        "טוּבְךָ": "Your goodness",
        "וְצִדְקָתְךָ": "and Your righteousness",
        "חַנּוּן": "Gracious",
        "וְרַחוּם": "and merciful",
        "אֶרֶךְ": "slow to",
        "וּגְדָל": "and great in",
        "חָסֶד": "kindness",
        "טוב": "Good",
        "לַכּל": "to all",
        "וְרַחֲמָיו": "and His mercies",
        "עַל": "over",
        "מַעֲשיו": "His works",
        "יודוּךָ": "will thank You",
        "וַחֲסִידֶיךָ": "and Your pious ones",
        "יְבָרְכוּכָה": "will bless You",
        "מַלְכוּתְךָ": "Your kingdom",
        "לְהודִיעַ": "To inform",
        "לִבְנֵי": "to the sons of",
        "הָאָדָם": "man",
        "וּכְבוד": "and the glory of",
        "מַלְכוּתו": "His kingdom",
        "מַלְכוּת": "kingdom",
        "עולָמִים": "of all worlds",
        "וָדר": "and generation",
        "סומֵךְ": "supports",
        "לְכָל": "all",
        "הַנּפְלִים": "who fall",
        "וְזוקֵף": "and straightens",
        "עֵינֵי": "The eyes of",
        "כל": "all",
        "אֵלֶיךָ": "to You",
        "נותֵן": "give",
        "לָהֶם": "to them",
        "אֶת": "[direct object]",
        "אָכְלָם": "their food",
        "פּותֵחַ": "You open",
        "יָדֶךָ": "Your hand",
        "חַי": "living thing",
        "רָצון": "with favor",
        "בְּכָל": "in every",
        "וְחָסִיד": "and kind",
        "קָרוב": "Near",
        "קרְאָיו": "those who call upon Him",
        "יִקְרָאֻהוּ": "call upon Him",
        "בֶאֱמֶת": "in truth",
        "רְצון": "The will of",
        "יְרֵאָיו": "those who fear Him",
        "יַעֲשה": "He will do",
        "שׁומֵר": "guards",
        "אהֲבָיו": "those who love Him",
        "וְאֵת": "but all",
        "וַאֲנַחְנוּ": "And we",
        "נְבָרֵךְ": "will bless",
        "יָהּ": "God",
        "וְעַד": "and until",
        "עולָם": "eternity",
        "הַלְלוּיָהּ": "Halleluyah",

        # NEW: Adding 46 missing translations
        "אַשְׁרֵי": "Praiseworthy / Happy are",
        "יושְׁבֵי": "those who dwell",
        "סֶּלָה": "Selah",
        "שֶׁכָּכָה": "that such [is]",
        "תְּהִלָּה": "A praise",
        "הַמֶּלֶךְ": "the King",
        "שִׁמְךָ": "Your Name",
        "אֲבָרְכֶךָּ": "I will bless You",
        "גָּדול": "Great",
        "וּמְהֻלָּל": "and praised",
        "וְלִגְדֻלָּתו": "and of His greatness",
        "יְשַׁבַּח": "will praise",
        "יַגִּידוּ": "they will declare",
        "כְּבוד": "the glory of",
        "וּגְדֻלָּתְךָ": "and Your greatness",
        "אֲסַפְּרֶנָּה": "I will relate",
        "יַבִּיעוּ": "they will utter",
        "יְרַנֵּנוּ": "they will sing joyously",
        "אַפַּיִם": "anger",
        "כָּל": "all",
        "וּגְבוּרָתְךָ": "and Your mighty acts",
        "יְדַבֵּרוּ": "they will speak",
        "גְּבוּרתָיו": "His mighty acts",
        "וּמֶמְשַׁלְתְּךָ": "and Your dominion",
        "הַכְּפוּפִים": "who are bent",
        "יְשבֵּרוּ": "look with hope",
        "וְאַתָּה": "and You",
        "בְּעִתּו": "in its time",
        "וּמַשבִּיעַ": "and satisfy",
        "צַדִּיק": "Righteous",
        "דְּרָכָיו": "His ways",
        "לְכל": "all",
        "אֲשֶׁר": "who",
        "שַׁוְעָתָם": "their cry",
        "יִשְׁמַע": "He will hear",
        "וְיושִׁיעֵם": "and save them",
        "הָרְשָׁעִים": "the wicked",
        "יַשְׁמִיד": "He will destroy",
        "תְּהִלַּת": "The praise of",
        "יְדַבֶּר": "will speak",
        "פִּי": "my mouth",
        "בָּשר": "all flesh",
        "שֵׁם": "the Name of",
        "קָדְשׁו": "His holiness",
        "מֵעַתָּה": "from now",
    }

def apply_all_translations():
    """Apply complete translation map to all words."""
    print("=" * 70)
    print("APPLYING COMPLETE ASHREI TRANSLATIONS")
    print("=" * 70)

    ashrei = load_ashrei()
    translation_map = get_complete_translation_map()

    translated = 0
    missing = 0
    missing_words = []

    for word_id, word_data in ashrei["words"].items():
        hebrew_clean = word_data["hebrew_clean"]

        if hebrew_clean in translation_map:
            word_data["translation"] = translation_map[hebrew_clean]
            translated += 1
        else:
            missing += 1
            missing_words.append(f"{word_id}: {hebrew_clean} (v{word_data['verse']})")

    save_ashrei(ashrei)

    # Summary
    print("\n" + "=" * 70)
    print("TRANSLATION COMPLETE")
    print("=" * 70)
    print(f"✓ Translated: {translated} / {len(ashrei['words'])} words")
    print(f"✓ Complete: {(translated / len(ashrei['words']) * 100):.1f}%")

    if missing > 0:
        print(f"\n⚠️  Still missing: {missing} words")
        for m in missing_words[:5]:
            print(f"  {m}")
    else:
        print("\n🎉 ALL WORDS TRANSLATED!")

    # Show sample verse with translations
    print("\n" + "=" * 70)
    print("SAMPLE: VERSE 1 WITH TRANSLATIONS")
    print("=" * 70)

    verse1 = ashrei["verses"]["v1"]
    print(f"Hebrew: {verse1['hebrew_full']}\n")
    print("Word-by-word:")
    for wid in verse1["word_ids"]:
        word = ashrei["words"][wid]
        print(f"  {word['hebrew_clean']:20} → {word.get('translation', 'MISSING')}")

    print("\nEnglish: Praiseworthy are those who dwell in Your house, continually they will praise You, Selah.")

if __name__ == '__main__':
    apply_all_translations()
