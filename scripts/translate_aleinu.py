#!/usr/bin/env python3
"""
Add complete word-by-word translations to Aleinu.
Based on traditional Aleinu translations.
"""

import json
from pathlib import Path

def load_aleinu():
    path = Path('/Users/mordechai/Ohr Avraham Chaim/Siddur/data/aleinu_embedded.json')
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_aleinu(aleinu):
    path = Path('/Users/mordechai/Ohr Avraham Chaim/Siddur/data/aleinu_embedded.json')
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(aleinu, f, ensure_ascii=False, indent=2)
    print(f"✓ Saved translations to {path}")

def get_aleinu_translations():
    """
    Complete translation map for Aleinu based on traditional translations.
    Aleinu has two main paragraphs with distinct themes.
    """

    # First, collect unique words from Aleinu JSON to ensure we cover all
    aleinu = load_aleinu()

    # Build complete translation map
    translations = {}

    # Process each word and add translation
    for wid, word_data in aleinu["words"].items():
        hebrew = word_data["hebrew_clean"]
        para = word_data["paragraph"]

        # Add translations based on the word
        if hebrew not in translations:
            translations[hebrew] = get_word_translation(hebrew, para)

    return translations

def get_word_translation(hebrew, paragraph):
    """Get translation for a specific Hebrew word."""

    # Comprehensive Aleinu translation map
    word_map = {
        # Paragraph 1 - Opening phrase and God's uniqueness
        "עָלֵינוּ": "It is upon us",
        "לְשַׁבֵּחַ": "to praise",
        "לַאֲדון": "the Master of",
        "הַכּל": "all",
        "לָתֵת": "to give",
        "גְּדֻלָּה": "greatness",
        "לְיוצֵר": "to the Creator of",
        "בְּרֵאשִׁית": "the beginning",
        "שֶׁלּא": "who did not",
        "עָשנוּ": "make us",
        "כְּגויֵי": "like the nations of",
        "הָאֲרָצות": "the lands",
        "וְלא": "and did not",
        "שמָנוּ": "place us",
        "כְּמִשְׁפְּחות": "like the families of",
        "הָאֲדָמָה": "the earth",
        "שם": "place",
        "חֶלְקֵנוּ": "our portion",
        "כָּהֶם": "like them",
        "וְגורָלֵנוּ": "and our lot",
        "כְּכָל": "like all",
        "הֲמונָם": "their multitude",
        "שֶׁהֵם": "for they",
        "מִשְׁתַּחֲוִים": "bow down",
        "לְהֶבֶל": "to vanity",
        "וְרִיק": "and emptiness",
        "וּמִתְפַּלְלִים": "and pray",
        "אֶל": "to",
        "אֵל": "a god",
        "לא": "not",
        "יושִׁיעַ": "who saves",
        "וַאֲנַחְנוּ": "But we",
        "כּורְעִים": "bend the knee",
        "וּמִשְׁתַּחֲוִים": "and bow",
        "וּמודִים": "and give thanks",
        "לִפְנֵי": "before",
        "מֶלֶךְ": "the King",
        "מַלְכֵי": "of kings of",
        "הַמְּלָכִים": "kings",
        "הַקָּדושׁ": "the Holy One",
        "בָּרוּךְ": "Blessed",
        "הוּא": "is He",
        "שֶׁהוּא": "Who",
        "נוטֶה": "stretches out",
        "שָׁמַיִם": "the heavens",
        "וְיוסֵד": "and establishes",
        "אָרֶץ": "the earth",
        "וּמושַׁב": "and the seat of",
        "יְקָרו": "His glory",
        "בַּשָּׁמַיִם": "in the heavens",
        "מִמַּעַל": "above",
        "וּשְׁכִינַת": "and the Presence of",
        "עֻזּו": "His might",
        "בְּגָבְהֵי": "in the highest",
        "מְרומִים": "heights",
        "אֱלהֵינוּ": "our God",
        "אֵין": "there is no",
        "עוד": "other",
        "אֱמֶת": "True",
        "מַלְכֵּנוּ": "our King",
        "אֶפֶס": "nothing",
        "זוּלָתו": "besides Him",
        "כַּכָּתוּב": "as it is written",
        "בְּתורָתו": "in His Torah",
        "וְיָדַעְתָּ": "And you shall know",
        "הַיּום": "today",
        "וַהֲשֵׁבתָ": "and take to",
        "לְבָבֶךָ": "your heart",
        "כִּי": "that",
        "ה'": "Hashem",
        "הָאֱלהִים": "is God",
        "מִתָּחַת": "below",

        # Paragraph 2 - Hope for the future
        "עַל": "Therefore",
        "כֵּן": "so",
        "נְקַוֶּה": "we hope",
        "לְּךָ": "to You",
        "לִרְאות": "to see",
        "מְהֵרָה": "soon",
        "בְּתִפְאֶרֶת": "in the glory of",
        "עֻזֶּךָ": "Your might",
        "לְהַעֲבִיר": "to remove",
        "גִּלּוּלִים": "idols",
        "מִן": "from",
        "הָאָרֶץ": "the earth",
        "וְהָאֱלִילִים": "and the false gods",
        "כָּרות": "utterly",
        "יִכָּרֵתוּן": "will be cut off",
        "לְתַקֵּן": "to perfect",
        "עולָם": "the world",
        "בְּמַלְכוּת": "under the kingdom of",
        "שַׁדַּי": "the Almighty",
        "וְכָל": "and all",
        "בְּנֵי": "the children of",
        "בָשר": "flesh",
        "יִקְרְאוּ": "will call",
        "בִשְׁמֶךָ": "upon Your Name",
        "לְהַפְנות": "to turn",
        "אֵלֶיךָ": "to You",
        "כָּל": "all",
        "רִשְׁעֵי": "the wicked of",
        "יַכִּירוּ": "will recognize",
        "וְיֵדְעוּ": "and know",
        "יושְׁבֵי": "the inhabitants of",
        "תֵבֵל": "the world",
        "לְךָ": "to You",
        "תִּכְרַע": "will bend",
        "בֶּרֶךְ": "every knee",
        "תִּשָּׁבַע": "will swear",
        "לָשׁון": "every tongue",
        "לְפָנֶיךָ": "Before You",
        "יִכְרְעוּ": "they will bend",
        "וְיִפּלוּ": "and fall",
        "וְלִכְבוד": "and to the glory of",
        "שִׁמְךָ": "Your Name",
        "יְקָר": "honor",
        "יִתֵּנוּ": "they will give",
        "וִיקַבְּלוּ": "And they will accept",
        "כֻלָּם": "all of them",
        "אֶת": "[direct object]",
        "על": "the yoke of",
        "מַלְכוּתֶךָ": "Your kingdom",
        "וְתִמְלךְ": "and You shall reign",
        "עֲלֵיהֶם": "over them",
        "לְעולָם": "forever",
        "וָעֶד": "and ever",
        "הַמַּלְכוּת": "the kingdom",
        "שֶׁלְּךָ": "is Yours",
        "הִיא": "it is",
        "וּלְעולְמֵי": "and for all",
        "עַד": "eternity",
        "תִּמְלךְ": "You will reign",
        "בְּכָבוד": "in glory",
        "בְּתורָתֶךָ": "in Your Torah",
        "יִמְלךְ": "will reign",
        "וְנֶאֱמַר": "And it is said",
        "וְהָיָה": "And it shall be",
        "לְמֶלֶךְ": "as King",
        "בַּיּום": "on the day",
        "הַהוּא": "that",
        "יִהְיֶה": "will be",
        "אֶחָד": "One",
        "וּשְׁמו": "and His Name",
    }

    return word_map.get(hebrew, f"[translation needed for {hebrew}]")

def apply_translations():
    """Apply translations to all Aleinu words."""
    print("=" * 70)
    print("ADDING TRANSLATIONS TO ALEINU")
    print("=" * 70)

    aleinu = load_aleinu()

    # Apply translations
    for wid, word_data in aleinu["words"].items():
        hebrew = word_data["hebrew_clean"]
        para = word_data["paragraph"]
        translation = get_word_translation(hebrew, para)
        word_data["translation"] = translation

    save_aleinu(aleinu)

    # Summary
    translated = sum(1 for w in aleinu["words"].values()
                    if "translation" in w and not w["translation"].startswith("[translation needed"))
    total = len(aleinu["words"])

    print("\n" + "=" * 70)
    print("TRANSLATION SUMMARY")
    print("=" * 70)
    print(f"✓ Translated: {translated}/{total} words ({translated/total*100:.1f}%)")

    # Check for missing
    missing = [(wid, w["hebrew_clean"]) for wid, w in aleinu["words"].items()
              if w["translation"].startswith("[translation needed")]

    if missing:
        print(f"\n⚠️  Missing {len(missing)} translations:")
        for wid, hebrew in missing[:10]:
            print(f"  {wid}: {hebrew}")
    else:
        print("\n🎉 ALL WORDS TRANSLATED!")

    # Show first 15 words as sample
    print("\n" + "=" * 70)
    print("SAMPLE: FIRST 15 WORDS")
    print("=" * 70)

    for i in range(1, 16):
        if f"w{i}" in aleinu["words"]:
            w = aleinu["words"][f"w{i}"]
            print(f"w{i}: {w['hebrew_clean']:20} → {w['translation']}")

if __name__ == '__main__':
    apply_translations()
