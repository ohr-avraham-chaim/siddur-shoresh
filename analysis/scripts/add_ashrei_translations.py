#!/usr/bin/env python3
"""
Add simple word-by-word translations to all 173 words in Ashrei.
Based on traditional translations and context.
"""

import json
from pathlib import Path

def load_ashrei():
    """Load the embedded Ashrei JSON."""
    path = Path('/Users/mordechai/Ohr Avraham Chaim/Siddur/data/ashrei_embedded.json')
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_ashrei(ashrei):
    """Save the embedded Ashrei JSON."""
    path = Path('/Users/mordechai/Ohr Avraham Chaim/Siddur/data/ashrei_embedded.json')
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(ashrei, f, ensure_ascii=False, indent=2)
    print(f"✓ Saved translations to {path}")

def get_translation_mapping():
    """
    Comprehensive word-by-word translation mapping.
    Based on traditional Ashrei translations.
    """
    return {
        # Verse 1: Psalm 84:5
        "אַשְׁרֵי": "Praiseworthy / Happy are",
        "יושְׁבֵי": "those who dwell",
        "בֵיתֶךָ": "in Your house",
        "עוד": "continually / still",
        "יְהַלְלוּךָ": "they will praise You",
        "סֶּלָה": "Selah / forever",

        # Verse 2: Psalm 144:15
        "הָעָם": "the people",
        "שֶׁכָּכָה": "that such [is]",
        "לּו": "for them / theirs",
        "שה'": "that Hashem [is]",
        "אֱלהָיו": "their God",

        # Verse 3: Psalm 145:1 - תהלה לדוד
        "תְּהִלָּה": "A praise / psalm",
        "לְדָוִד": "of David",
        "אֲרומִמְךָ": "I will exalt You",
        "אֱלוהַי": "my God",
        "הַמֶּלֶךְ": "the King",
        "וַאֲבָרְכָה": "and I will bless",
        "שִׁמְךָ": "Your Name",
        "לְעולָם": "forever",
        "וָעֶד": "and ever",

        # Verse 4: ב - Beit
        "בְּכָל": "every / in every",
        "יום": "day",
        "אֲבָרְכֶךָּ": "I will bless You",
        "וַאֲהַלְלָה": "and I will praise",

        # Verse 5: ג - Gimmel
        "גָּדול": "Great [is]",
        "ה'": "Hashem",
        "וּמְהֻלָּל": "and praised",
        "מְאד": "exceedingly",
        "וְלִגְדֻלָּתו": "and of His greatness",
        "אֵין": "there is no",
        "חֵקֶר": "limit / fathoming",

        # Verse 6: ד - Dalet
        "דּור": "generation",
        "לְדור": "to generation",
        "יְשַׁבַּח": "will praise",
        "מַעֲשיךָ": "Your works",
        "וּגְבוּרתֶיךָ": "and Your mighty acts",
        "יַגִּידוּ": "they will declare",

        # Verse 7: ה - Hei
        "הֲדַר": "The splendor of",
        "כְּבוד": "the glory of",
        "הודֶךָ": "Your majesty",
        "וְדִבְרֵי": "and the words of",
        "נִפְלְאתֶיךָ": "Your wonders",
        "אָשיחָה": "I will speak",

        # Verse 8: ו - Vav
        "וֶעֱזוּז": "And the might of",
        "נורְאתֶיךָ": "Your awesome deeds",
        "יאמֵרוּ": "they will speak",
        "וּגְדֻלָּתְךָ": "and Your greatness",
        "אֲסַפְּרֶנָּה": "I will relate",

        # Verse 9: ז - Zayin
        "זֵכֶר": "The remembrance of",
        "רַב": "Your abundant",
        "טוּבְךָ": "goodness",
        "יַבִּיעוּ": "they will utter",
        "וְצִדְקָתְךָ": "and Your righteousness",
        "יְרַנֵּנוּ": "they will sing joyously",

        # Verse 10: ח - Chet
        "חַנּוּן": "Gracious",
        "וְרַחוּם": "and merciful [is]",
        "אֶרֶךְ": "slow to",
        "אַפַּיִם": "anger",
        "וּגְדָל": "and great in",
        "חָסֶד": "kindness",

        # Verse 11: ט - Tet
        "טוב": "Good [is]",
        "לַכּל": "to all",
        "וְרַחֲמָיו": "and His mercy [extends]",
        "עַל": "over",
        "כָּל": "all",
        "מַעֲשיו": "His works",

        # Verse 12: י - Yud
        "יודוּךָ": "will thank You",
        "וַחֲסִידֶיךָ": "and Your pious ones",
        "יְבָרְכוּכָה": "will bless You",

        # Verse 13: כ - Kaf
        "מַלְכוּתְךָ": "Your kingdom",
        "יְדַבֵּרוּ": "they will speak",

        # Verse 14: ל - Lamed
        "לְהודִיעַ": "To inform",
        "לִבְנֵי": "to the sons of",
        "הָאָדָם": "man",
        "גְּבוּרתָיו": "His mighty acts",
        "וּכְבוד": "and the glory of",
        "הֲדַר": "the majesty of",
        "מַלְכוּתו": "His kingdom",

        # Verse 15: מ - Mem
        "מַלְכוּת": "kingdom",
        "עולָמִים": "of all worlds",
        "וּמֶמְשַׁלְתְּךָ": "and Your dominion",
        "וָדר": "and generation",

        # Verse 16: ס - Samech
        "סומֵךְ": "supports",
        "לְכָל": "all",
        "הַנּפְלִים": "who fall",
        "וְזוקֵף": "and straightens",
        "הַכְּפוּפִים": "all who are bent",

        # Verse 17: ע - Ayin
        "עֵינֵי": "The eyes of",
        "כל": "all",
        "אֵלֶיךָ": "to You",
        "יְשבֵּרוּ": "look with hope",
        "וְאַתָּה": "and You",
        "נותֵן": "give",
        "לָהֶם": "to them",
        "אֶת": "[direct object]",
        "אָכְלָם": "their food",
        "בְּעִתּו": "in its time",

        # Verse 18: פ - Pei
        "פּותֵחַ": "You open",
        "יָדֶךָ": "Your hand",
        "וּמַשבִּיעַ": "and satisfy",
        "חַי": "living thing",
        "רָצון": "with favor",

        # Verse 19: צ - Tzadi
        "צַדִּיק": "Righteous [is]",
        "דְּרָכָיו": "His ways",
        "וְחָסִיד": "and kind",

        # Verse 20: ק - Kuf
        "קָרוב": "Near [is]",
        "קרְאָיו": "those who call upon Him",
        "אֲשֶׁר": "who",
        "יִקְרָאֻהוּ": "call upon Him",
        "בֶאֱמֶת": "in truth",

        # Verse 21: ר - Reish
        "רְצון": "The will of",
        "יְרֵאָיו": "those who fear Him",
        "יַעֲשה": "He will do",
        "שַׁוְעָתָם": "their cry",
        "יִשְׁמַע": "He will hear",
        "וְיושִׁיעֵם": "and save them",

        # Verse 22: ש - Shin
        "שׁומֵר": "guards",
        "אהֲבָיו": "those who love Him",
        "וְאֵת": "but all",
        "הָרְשָׁעִים": "the wicked",
        "יַשְׁמִיד": "He will destroy",

        # Verse 23: ת - Tav
        "תְּהִלַּת": "The praise of",
        "יְדַבֶּר": "will speak",
        "פִּי": "my mouth",
        "וִיבָרֵךְ": "and let bless",
        "בָּשר": "all flesh",
        "שֵׁם": "the Name of",
        "קָדְשׁו": "His holiness",

        # Verse 24: Conclusion (Psalm 115:18)
        "וַאֲנַחְנוּ": "And we",
        "נְבָרֵךְ": "will bless",
        "יָהּ": "God",
        "מֵעַתָּה": "from now",
        "וְעַד": "and until",
        "עולָם": "eternity",
        "הַלְלוּיָהּ": "Halleluyah / Praise God"
    }

def add_all_translations():
    """Add translations to all words in Ashrei."""
    print("=" * 70)
    print("ADDING TRANSLATIONS TO ALL ASHREI WORDS")
    print("=" * 70)

    ashrei = load_ashrei()
    translation_map = get_translation_mapping()

    translated_count = 0
    missing_count = 0
    missing_words = []

    for word_id, word_data in ashrei["words"].items():
        hebrew_clean = word_data["hebrew_clean"]

        if hebrew_clean in translation_map:
            word_data["translation"] = translation_map[hebrew_clean]
            translated_count += 1
        else:
            missing_count += 1
            missing_words.append(f"{word_id}: {hebrew_clean} (verse {word_data['verse']})")
            print(f"⚠️  Missing translation for {word_id}: {hebrew_clean}")

    # Save updated JSON
    save_ashrei(ashrei)

    # Summary
    print("\n" + "=" * 70)
    print("TRANSLATION SUMMARY")
    print("=" * 70)
    print(f"✓ Translated: {translated_count} / {len(ashrei['words'])} words")
    print(f"⚠️  Missing: {missing_count} words")

    if missing_words:
        print("\nMissing translations:")
        for missing in missing_words[:10]:  # Show first 10
            print(f"  {missing}")
        if len(missing_words) > 10:
            print(f"  ... and {len(missing_words) - 10} more")

    # Show sample translations
    print("\n" + "=" * 70)
    print("SAMPLE TRANSLATIONS")
    print("=" * 70)

    for i in range(1, 13):  # First 12 words (first 2 verses)
        word = ashrei["words"][f"w{i}"]
        translation = word.get("translation", "NOT TRANSLATED")
        print(f"w{i}: {word['hebrew_clean']:20} → {translation}")

if __name__ == '__main__':
    add_all_translations()
