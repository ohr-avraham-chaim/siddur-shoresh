#!/usr/bin/env python3
"""
Add complete shoresh (root) information to all words in Ashrei and Aleinu.
Also add frequency tracking:
- frequency_in_prayer: how many times this root appears in this specific prayer
- frequency_across_prayers: how many times this root appears across Ashrei + Aleinu
"""

import json
from pathlib import Path
from collections import defaultdict

def load_prayer(prayer_name):
    path = Path(f'/Users/mordechai/Ohr Avraham Chaim/Siddur/data/{prayer_name}_embedded.json')
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_prayer(prayer_name, prayer_data):
    path = Path(f'/Users/mordechai/Ohr Avraham Chaim/Siddur/data/{prayer_name}_embedded.json')
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(prayer_data, f, ensure_ascii=False, indent=2)

def get_comprehensive_word_to_root_map():
    """
    Comprehensive mapping of Hebrew words to their roots.
    Based on actual words in Ashrei and Aleinu.
    """
    return {
        # Ashrei words
        "אַשְׁרֵי": ("א-ש-ר", "happiness, fortune", "interjection"),
        "יושְׁבֵי": ("י-ש-ב", "sitting, dwelling", "verb participle"),
        "בֵיתֶךָ": ("ב-י-ת", "house, home", "noun"),
        "עוד": ("ע-ו-ד", "more, again, still", "adverb"),
        "יְהַלְלוּךָ": ("ה-ל-ל", "praise, glory", "verb"),
        "סֶּלָה": ("ס-ל-ה", "selah, pause", "interjection"),
        "הָעָם": ("ע-מ-מ", "people, nation", "noun"),
        "שֶׁכָּכָה": ("כ-כ-ה", "thus, so", "adverb"),
        "לּו": ("ל-ו", "for them", "preposition"),
        "שה'": ("ה-ו-י", "being, Hashem", "proper noun"),
        "אֱלהָיו": ("א-ל-ה", "God, deity", "noun"),
        "תְּהִלָּה": ("ה-ל-ל", "praise, glory", "noun"),
        "לְדָוִד": ("ד-ו-ד", "David", "proper noun"),
        "אֲרומִמְךָ": ("ר-ו-מ", "raising, exalting", "verb"),
        "אֱלוהַי": ("א-ל-ה", "God, deity", "noun"),
        "הַמֶּלֶךְ": ("מ-ל-כ", "kingship, ruling", "noun"),
        "וַאֲבָרְכָה": ("ב-ר-כ", "blessing, knee", "verb"),
        "שִׁמְךָ": ("ש-מ-מ", "name", "noun"),
        "לְעולָם": ("ע-ל-מ", "eternity, world", "noun"),
        "וָעֶד": ("ע-ד-ד", "perpetuity, eternity", "noun"),
        "בְּכָל": ("כ-ל-ל", "all, every", "adjective"),
        "יום": ("י-ו-מ", "day", "noun"),
        "אֲבָרְכֶךָּ": ("ב-ר-כ", "blessing, knee", "verb"),
        "וַאֲהַלְלָה": ("ה-ל-ל", "praise, glory", "verb"),
        "גָּדול": ("ג-ד-ל", "greatness, growing", "adjective"),
        "ה'": ("ה-ו-י", "being, Hashem", "proper noun"),
        "וּמְהֻלָּל": ("ה-ל-ל", "praise, glory", "verb"),
        "מְאד": ("מ-א-ד", "very, exceedingly", "adverb"),
        "וְלִגְדֻלָּתו": ("ג-ד-ל", "greatness, growing", "noun"),
        "אֵין": ("א-י-נ", "nothing, not", "particle"),
        "חֵקֶר": ("ח-ק-ר", "searching, investigating", "noun"),
        "דּור": ("ד-ו-ר", "generation, circle", "noun"),
        "לְדור": ("ד-ו-ר", "generation, circle", "noun"),
        "יְשַׁבַּח": ("ש-ב-ח", "praising, commending", "verb"),
        "מַעֲשיךָ": ("ע-ש-ה", "making, doing", "noun"),
        "וּגְבוּרתֶיךָ": ("ג-ב-ר", "strength, might", "noun"),
        "יַגִּידוּ": ("נ-ג-ד", "telling, declaring", "verb"),
        "הֲדַר": ("ה-ד-ר", "splendor, honor", "noun"),
        "כְּבוד": ("כ-ב-ד", "honor, heaviness", "noun"),
        "הודֶךָ": ("ה-ו-ד", "splendor, majesty", "noun"),
        "וְדִבְרֵי": ("ד-ב-ר", "speaking, word", "noun"),
        "נִפְלְאתֶיךָ": ("פ-ל-א", "wonders, miracles", "noun"),
        "אָשיחָה": ("ש-י-ח", "speaking, meditating", "verb"),
        "וֶעֱזוּז": ("ע-ז-ז", "strength, might", "noun"),
        "נורְאתֶיךָ": ("י-ר-א", "fear, awe", "noun"),
        "יאמֵרוּ": ("א-מ-ר", "saying, speaking", "verb"),
        "וּגְדֻלָּתְךָ": ("ג-ד-ל", "greatness, growing", "noun"),
        "אֲסַפְּרֶנָּה": ("ס-פ-ר", "counting, telling", "verb"),
        "זֵכֶר": ("ז-כ-ר", "remembering, memorial", "noun"),
        "רַב": ("ר-ב-ב", "many, great", "adjective"),
        "טוּבְךָ": ("ט-ו-ב", "goodness", "noun"),
        "יַבִּיעוּ": ("נ-ב-ע", "flowing, uttering", "verb"),
        "וְצִדְקָתְךָ": ("צ-ד-ק", "righteousness", "noun"),
        "יְרַנֵּנוּ": ("ר-נ-נ", "singing, rejoicing", "verb"),
        "חַנּוּן": ("ח-נ-נ", "grace, favor", "adjective"),
        "וְרַחוּם": ("ר-ח-מ", "mercy, compassion", "adjective"),
        "אֶרֶךְ": ("א-ר-כ", "length, patience", "adjective"),
        "אַפַּיִם": ("א-נ-פ", "nose, anger", "noun"),
        "וּגְדָל": ("ג-ד-ל", "greatness, growing", "adjective"),
        "חָסֶד": ("ח-ס-ד", "kindness, loyalty", "noun"),
        "טוב": ("ט-ו-ב", "goodness", "adjective"),
        "לַכּל": ("כ-ל-ל", "all, every", "noun"),
        "וְרַחֲמָיו": ("ר-ח-מ", "mercy, compassion", "noun"),
        "עַל": ("ע-ל-ל", "upon, over", "preposition"),
        "כָּל": ("כ-ל-ל", "all, every", "adjective"),
        "מַעֲשיו": ("ע-ש-ה", "making, doing", "noun"),
        "יודוּךָ": ("י-ד-ה", "thanking, confessing", "verb"),
        "וַחֲסִידֶיךָ": ("ח-ס-ד", "kindness, loyalty", "noun"),
        "יְבָרְכוּכָה": ("ב-ר-כ", "blessing, knee", "verb"),
        "כְּבוד": ("כ-ב-ד", "honor, heaviness", "noun"),
        "מַלְכוּתְךָ": ("מ-ל-כ", "kingship, ruling", "noun"),
        "יאמֵרוּ": ("א-מ-ר", "saying, speaking", "verb"),
        "וּגְבוּרָתְךָ": ("ג-ב-ר", "strength, might", "noun"),
        "יְדַבֵּרוּ": ("ד-ב-ר", "speaking, word", "verb"),
        "לְהודִיעַ": ("י-ד-ע", "knowing, recognizing", "verb"),
        "לִבְנֵי": ("ב-נ-י", "building, son", "noun"),
        "הָאָדָם": ("א-ד-מ", "man, earth", "noun"),
        "גְּבוּרתָיו": ("ג-ב-ר", "strength, might", "noun"),
        "וּכְבוד": ("כ-ב-ד", "honor, heaviness", "noun"),
        "מַלְכוּתו": ("מ-ל-כ", "kingship, ruling", "noun"),
        "מַלְכוּת": ("מ-ל-כ", "kingship, ruling", "noun"),
        "עולָמִים": ("ע-ל-מ", "eternity, world", "noun"),
        "וּמֶמְשַׁלְתְּךָ": ("מ-ש-ל", "ruling, governance", "noun"),
        "וָדר": ("ד-ו-ר", "generation, circle", "noun"),
        "סומֵךְ": ("ס-מ-כ", "supporting, leaning", "verb"),
        "לְכָל": ("כ-ל-ל", "all, every", "noun"),
        "הַנּפְלִים": ("נ-פ-ל", "falling", "verb participle"),
        "וְזוקֵף": ("ז-ק-פ", "straightening, raising", "verb"),
        "הַכְּפוּפִים": ("כ-פ-פ", "bending, bowing", "verb participle"),
        "עֵינֵי": ("ע-י-נ", "eye, seeing", "noun"),
        "כל": ("כ-ל-ל", "all, every", "adjective"),
        "אֵלֶיךָ": ("א-ל", "to, toward", "preposition"),
        "יְשבֵּרוּ": ("ש-ב-ר", "hoping, waiting", "verb"),
        "וְאַתָּה": ("א-ת-ת", "you", "pronoun"),
        "נותֵן": ("נ-ת-נ", "giving", "verb"),
        "לָהֶם": ("ל-ה-מ", "to them", "preposition"),
        "אֶת": ("א-ת-ת", "with, direct object", "particle"),
        "אָכְלָם": ("א-כ-ל", "eating, food", "noun"),
        "בְּעִתּו": ("ע-ת-ת", "time, season", "noun"),
        "פּותֵחַ": ("פ-ת-ח", "opening", "verb"),
        "יָדֶךָ": ("י-ד-ד", "hand", "noun"),
        "וּמַשבִּיעַ": ("ש-ב-ע", "satisfying, seven", "verb"),
        "חַי": ("ח-י-ה", "living, life", "adjective"),
        "רָצון": ("ר-צ-ה", "will, favor", "noun"),
        "צַדִּיק": ("צ-ד-ק", "righteousness", "adjective"),
        "דְּרָכָיו": ("ד-ר-כ", "way, path", "noun"),
        "וְחָסִיד": ("ח-ס-ד", "kindness, loyalty", "adjective"),
        "קָרוב": ("ק-ר-ב", "approaching, near", "adjective"),
        "קרְאָיו": ("ק-ר-א", "calling, reading", "verb participle"),
        "לְכל": ("כ-ל-ל", "all, every", "noun"),
        "אֲשֶׁר": ("א-ש-ר", "who, which", "relative pronoun"),
        "יִקְרָאֻהוּ": ("ק-ר-א", "calling, reading", "verb"),
        "בֶאֱמֶת": ("א-מ-ת", "truth, reliability", "noun"),
        "רְצון": ("ר-צ-ה", "will, favor", "noun"),
        "יְרֵאָיו": ("י-ר-א", "fear, awe", "verb participle"),
        "יַעֲשה": ("ע-ש-ה", "making, doing", "verb"),
        "וְאֶת": ("א-ת-ת", "with, direct object", "particle"),
        "שַׁוְעָתָם": ("ש-ו-ע", "crying out, salvation", "noun"),
        "יִשְׁמַע": ("ש-מ-ע", "hearing, listening", "verb"),
        "וְיושִׁיעֵם": ("י-ש-ע", "saving, rescuing", "verb"),
        "שׁומֵר": ("ש-מ-ר", "guarding, watching", "verb"),
        "אהֲבָיו": ("א-ה-ב", "loving", "verb participle"),
        "וְאֵת": ("א-ת-ת", "with, direct object", "particle"),
        "הָרְשָׁעִים": ("ר-ש-ע", "wickedness", "noun"),
        "יַשְׁמִיד": ("ש-מ-ד", "destroying, annihilating", "verb"),
        "תְּהִלַּת": ("ה-ל-ל", "praise, glory", "noun"),
        "יְדַבֶּר": ("ד-ב-ר", "speaking, word", "verb"),
        "פִּי": ("פ-ה-ה", "mouth", "noun"),
        "וִיבָרֵךְ": ("ב-ר-כ", "blessing, knee", "verb"),
        "בָּשר": ("ב-ש-ר", "flesh, messenger", "noun"),
        "שֵׁם": ("ש-מ-מ", "name", "noun"),
        "קָדְשׁו": ("ק-ד-שׁ", "holiness, sanctity", "noun"),
        "וַאֲנַחְנוּ": ("א-נ-ח", "we", "pronoun"),
        "נְבָרֵךְ": ("ב-ר-כ", "blessing, knee", "verb"),
        "יָהּ": ("י-ה-ה", "God, Yah", "proper noun"),
        "מֵעַתָּה": ("ע-ת-ת", "time, season", "adverb"),
        "וְעַד": ("ע-ד-ד", "perpetuity, eternity", "preposition"),
        "עולָם": ("ע-ל-מ", "eternity, world", "noun"),
        "הַלְלוּיָהּ": ("ה-ל-ל", "praise, glory", "interjection"),

        # Aleinu words
        "עָלֵינוּ": ("ע-ל-ל", "upon, over", "preposition"),
        "לְשַׁבֵּחַ": ("ש-ב-ח", "praising, commending", "verb infinitive"),
        "לַאֲדון": ("א-ד-נ", "master, lord", "noun"),
        "הַכּל": ("כ-ל-ל", "all, every", "noun"),
        "לָתֵת": ("נ-ת-נ", "giving", "verb infinitive"),
        "גְּדֻלָּה": ("ג-ד-ל", "greatness, growing", "noun"),
        "לְיוצֵר": ("י-צ-ר", "forming, creating", "verb participle"),
        "בְּרֵאשִׁית": ("ר-א-שׁ", "head, beginning", "noun"),
        "שֶׁלּא": ("ל-א", "not", "particle"),
        "עָשנוּ": ("ע-ש-ה", "making, doing", "verb"),
        "כְּגויֵי": ("ג-ו-י", "nation, people", "noun"),
        "הָאֲרָצות": ("א-ר-ץ", "land, earth", "noun"),
        "וְלא": ("ל-א", "not", "particle"),
        "שמָנוּ": ("ש-ו-מ", "placing, setting", "verb"),
        "כְּמִשְׁפְּחות": ("ש-פ-ח", "family, clan", "noun"),
        "הָאֲדָמָה": ("א-ד-מ", "man, earth", "noun"),
        "שם": ("ש-ו-מ", "placing, setting", "verb"),
        "חֶלְקֵנוּ": ("ח-ל-ק", "portion, dividing", "noun"),
        "כָּהֶם": ("כ-מ-ה", "like, as", "preposition"),
        "וְגורָלֵנוּ": ("ג-ר-ל", "lot, fate", "noun"),
        "כְּכָל": ("כ-ל-ל", "all, every", "preposition"),
        "הֲמונָם": ("ה-מ-נ", "multitude, crowd", "noun"),
        "שֶׁהֵם": ("ה-מ-מ", "they", "pronoun"),
        "מִשְׁתַּחֲוִים": ("ש-ח-ה", "bowing, prostrating", "verb"),
        "לְהֶבֶל": ("ה-ב-ל", "vanity, breath", "noun"),
        "וְרִיק": ("ר-י-ק", "emptiness, vain", "noun"),
        "וּמִתְפַּלְלִים": ("פ-ל-ל", "praying, judging", "verb"),
        "אֶל": ("א-ל", "to, toward", "preposition"),
        "אֵל": ("א-ל", "God, strength", "noun"),
        "לא": ("ל-א", "not", "particle"),
        "יושִׁיעַ": ("י-ש-ע", "saving, rescuing", "verb"),
        "כּורְעִים": ("כ-ר-ע", "kneeling, bowing", "verb"),
        "וּמִשְׁתַּחֲוִים": ("ש-ח-ה", "bowing, prostrating", "verb"),
        "וּמודִים": ("י-ד-ה", "thanking, confessing", "verb"),
        "לִפְנֵי": ("פ-נ-ה", "face, turning", "noun"),
        "מֶלֶךְ": ("מ-ל-כ", "kingship, ruling", "noun"),
        "מַלְכֵי": ("מ-ל-כ", "kingship, ruling", "noun"),
        "הַמְּלָכִים": ("מ-ל-כ", "kingship, ruling", "noun"),
        "הַקָּדושׁ": ("ק-ד-שׁ", "holiness, sanctity", "adjective"),
        "בָּרוּךְ": ("ב-ר-כ", "blessing, knee", "adjective"),
        "הוּא": ("ה-ו-א", "he, that", "pronoun"),
        "שֶׁהוּא": ("ה-ו-א", "he, that", "pronoun"),
        "נוטֶה": ("נ-ט-ה", "stretching, bending", "verb"),
        "שָׁמַיִם": ("ש-מ-י", "heavens, sky", "noun"),
        "וְיוסֵד": ("י-ס-ד", "founding, establishing", "verb"),
        "אָרֶץ": ("א-ר-ץ", "land, earth", "noun"),
        "וּמושַׁב": ("י-ש-ב", "sitting, dwelling", "noun"),
        "יְקָרו": ("י-ק-ר", "honor, precious", "noun"),
        "בַּשָּׁמַיִם": ("ש-מ-י", "heavens, sky", "noun"),
        "מִמַּעַל": ("מ-ע-ל", "above, upward", "noun"),
        "וּשְׁכִינַת": ("ש-כ-נ", "dwelling, presence", "noun"),
        "עֻזּו": ("ע-ז-ז", "strength, might", "noun"),
        "בְּגָבְהֵי": ("ג-ב-ה", "height, high", "noun"),
        "מְרומִים": ("ר-ו-מ", "raising, exalting", "noun"),
        "אֱלהֵינוּ": ("א-ל-ה", "God, deity", "noun"),
        "עוד": ("ע-ו-ד", "more, again, still", "adverb"),
        "אֱמֶת": ("א-מ-ת", "truth, reliability", "noun"),
        "מַלְכֵּנוּ": ("מ-ל-כ", "kingship, ruling", "noun"),
        "אֶפֶס": ("א-פ-ס", "end, nothing", "noun"),
        "זוּלָתו": ("ז-ו-ל", "except, besides", "preposition"),
        "כַּכָּתוּב": ("כ-ת-ב", "writing", "verb passive"),
        "בְּתורָתו": ("ת-ו-ר", "Torah, instruction", "noun"),
        "וְיָדַעְתָּ": ("י-ד-ע", "knowing, recognizing", "verb"),
        "הַיּום": ("י-ו-מ", "day", "noun"),
        "וַהֲשֵׁבתָ": ("ש-ו-ב", "returning, restoring", "verb"),
        "לְבָבֶךָ": ("ל-ב-ב", "heart, inner self", "noun"),
        "כִּי": ("כ-י", "that, because", "conjunction"),
        "הָאֱלהִים": ("א-ל-ה", "God, deity", "noun"),
        "מִתָּחַת": ("ת-ח-ת", "under, below", "noun"),
        "עַל": ("ע-ל-ל", "upon, over", "preposition"),
        "כֵּן": ("כ-נ-נ", "thus, so", "adverb"),
        "נְקַוֶּה": ("ק-ו-ה", "hoping, waiting", "verb"),
        "לְּךָ": ("ל", "to you", "preposition"),
        "לִרְאות": ("ר-א-ה", "seeing", "verb infinitive"),
        "מְהֵרָה": ("מ-ה-ר", "haste, quickly", "adverb"),
        "בְּתִפְאֶרֶת": ("פ-א-ר", "beauty, glory", "noun"),
        "עֻזֶּךָ": ("ע-ז-ז", "strength, might", "noun"),
        "לְהַעֲבִיר": ("ע-ב-ר", "passing, crossing", "verb infinitive"),
        "גִּלּוּלִים": ("ג-ל-ל", "idols, dung", "noun"),
        "מִן": ("מ-נ", "from", "preposition"),
        "הָאָרֶץ": ("א-ר-ץ", "land, earth", "noun"),
        "וְהָאֱלִילִים": ("א-ל-ל", "idols, worthless", "noun"),
        "כָּרות": ("כ-ר-ת", "cutting, destroying", "verb infinitive"),
        "יִכָּרֵתוּן": ("כ-ר-ת", "cutting, destroying", "verb"),
        "לְתַקֵּן": ("ת-ק-נ", "fixing, repairing", "verb infinitive"),
        "עולָם": ("ע-ל-מ", "eternity, world", "noun"),
        "בְּמַלְכוּת": ("מ-ל-כ", "kingship, ruling", "noun"),
        "שַׁדַּי": ("ש-ד-י", "Almighty", "proper noun"),
        "וְכָל": ("כ-ל-ל", "all, every", "noun"),
        "בְּנֵי": ("ב-נ-י", "building, son", "noun"),
        "בָשר": ("ב-ש-ר", "flesh, messenger", "noun"),
        "יִקְרְאוּ": ("ק-ר-א", "calling, reading", "verb"),
        "בִשְׁמֶךָ": ("ש-מ-מ", "name", "noun"),
        "לְהַפְנות": ("פ-נ-ה", "turning, facing", "verb infinitive"),
        "אֵלֶיךָ": ("א-ל", "to, toward", "preposition"),
        "רִשְׁעֵי": ("ר-ש-ע", "wickedness", "noun"),
        "אָרֶץ": ("א-ר-ץ", "land, earth", "noun"),
        "יַכִּירוּ": ("נ-כ-ר", "recognizing, acknowledging", "verb"),
        "וְיֵדְעוּ": ("י-ד-ע", "knowing, recognizing", "verb"),
        "יושְׁבֵי": ("י-ש-ב", "sitting, dwelling", "verb participle"),
        "תֵבֵל": ("ת-ב-ל", "world, earth", "noun"),
        "לְךָ": ("ל", "to you", "preposition"),
        "תִּכְרַע": ("כ-ר-ע", "kneeling, bowing", "verb"),
        "בֶּרֶךְ": ("ב-ר-כ", "blessing, knee", "noun"),
        "תִּשָּׁבַע": ("ש-ב-ע", "swearing, seven", "verb"),
        "לָשׁון": ("ל-ש-נ", "tongue, language", "noun"),
        "לְפָנֶיךָ": ("פ-נ-ה", "face, turning", "noun"),
        "יִכְרְעוּ": ("כ-ר-ע", "kneeling, bowing", "verb"),
        "וְיִפּלוּ": ("נ-פ-ל", "falling", "verb"),
        "וְלִכְבוד": ("כ-ב-ד", "honor, heaviness", "noun"),
        "שִׁמְךָ": ("ש-מ-מ", "name", "noun"),
        "יְקָר": ("י-ק-ר", "honor, precious", "noun"),
        "יִתֵּנוּ": ("נ-ת-נ", "giving", "verb"),
        "וִיקַבְּלוּ": ("ק-ב-ל", "receiving, accepting", "verb"),
        "כֻלָּם": ("כ-ל-ל", "all, every", "noun"),
        "על": ("ע-ל-ל", "upon, over", "noun"),
        "מַלְכוּתֶךָ": ("מ-ל-כ", "kingship, ruling", "noun"),
        "וְתִמְלךְ": ("מ-ל-כ", "kingship, ruling", "verb"),
        "עֲלֵיהֶם": ("ע-ל-ל", "upon, over", "preposition"),
        "לְעולָם": ("ע-ל-מ", "eternity, world", "noun"),
        "הַמַּלְכוּת": ("מ-ל-כ", "kingship, ruling", "noun"),
        "שֶׁלְּךָ": ("ל", "of yours", "preposition"),
        "הִיא": ("ה-ו-א", "she, that", "pronoun"),
        "וּלְעולְמֵי": ("ע-ל-מ", "eternity, world", "noun"),
        "עַד": ("ע-ד-ד", "perpetuity, eternity", "noun"),
        "תִּמְלךְ": ("מ-ל-כ", "kingship, ruling", "verb"),
        "בְּכָבוד": ("כ-ב-ד", "honor, heaviness", "noun"),
        "בְּתורָתֶךָ": ("ת-ו-ר", "Torah, instruction", "noun"),
        "יִמְלךְ": ("מ-ל-כ", "kingship, ruling", "verb"),
        "וְנֶאֱמַר": ("א-מ-ר", "saying, speaking", "verb"),
        "וְהָיָה": ("ה-י-ה", "being, existing", "verb"),
        "לְמֶלֶךְ": ("מ-ל-כ", "kingship, ruling", "noun"),
        "בַּיּום": ("י-ו-מ", "day", "noun"),
        "הַהוּא": ("ה-ו-א", "he, that", "pronoun"),
        "יִהְיֶה": ("ה-י-ה", "being, existing", "verb"),
        "אֶחָד": ("א-ח-ד", "one, unity", "number"),
        "וּשְׁמו": ("ש-מ-מ", "name", "noun"),
    }

def add_shoresh_to_all_words(prayer_name):
    """Add shoresh to all words in a prayer."""
    print(f"\n{'=' * 70}")
    print(f"ADDING SHORESH TO ALL {prayer_name.upper()} WORDS")
    print('=' * 70)

    prayer = load_prayer(prayer_name)
    word_to_root = get_comprehensive_word_to_root_map()

    added = 0
    missing = []

    for wid, word_data in prayer["words"].items():
        hebrew = word_data["hebrew_clean"]

        if hebrew in word_to_root:
            root, meaning, word_type = word_to_root[hebrew]
            word_data["shoresh"] = {
                "root": root,
                "root_letters": root.split('-'),
                "meaning": meaning,
                "word_type": word_type
            }
            added += 1
        else:
            missing.append(f"{wid}: {hebrew}")

    save_prayer(prayer_name, prayer)

    print(f"✓ Added shoresh to {added}/{len(prayer['words'])} words")

    if missing:
        print(f"\n⚠️  Missing {len(missing)} words:")
        for m in missing[:10]:
            print(f"  {m}")

    return prayer

def calculate_root_frequencies(prayer_data, prayer_name):
    """Calculate how many times each root appears in this prayer."""
    root_counts = defaultdict(int)

    for word_data in prayer_data["words"].values():
        if "shoresh" in word_data:
            root = word_data["shoresh"]["root"]
            root_counts[root] += 1

    # Add frequency to each word
    for word_data in prayer_data["words"].values():
        if "shoresh" in word_data:
            root = word_data["shoresh"]["root"]
            word_data["shoresh"][f"frequency_in_{prayer_name}"] = root_counts[root]

    return root_counts

def calculate_combined_frequencies(ashrei, aleinu):
    """Calculate root frequencies across both prayers."""
    combined_counts = defaultdict(int)

    # Count from both prayers
    for prayer_data in [ashrei, aleinu]:
        for word_data in prayer_data["words"].values():
            if "shoresh" in word_data:
                root = word_data["shoresh"]["root"]
                combined_counts[root] += 1

    # Add combined frequency to all words
    for prayer_data in [ashrei, aleinu]:
        for word_data in prayer_data["words"].values():
            if "shoresh" in word_data:
                root = word_data["shoresh"]["root"]
                word_data["shoresh"]["frequency_across_prayers"] = combined_counts[root]

    return combined_counts

def show_frequency_analysis(ashrei_counts, aleinu_counts, combined_counts):
    """Show frequency analysis of roots."""
    print("\n" + "=" * 70)
    print("ROOT FREQUENCY ANALYSIS")
    print("=" * 70)

    # Top roots in Ashrei
    print("\nTop 10 Roots in ASHREI:")
    top_ashrei = sorted(ashrei_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    for root, count in top_ashrei:
        aleinu_count = aleinu_counts.get(root, 0)
        print(f"  {root:15} → {count:2}x in Ashrei, {aleinu_count:2}x in Aleinu")

    # Top roots in Aleinu
    print("\nTop 10 Roots in ALEINU:")
    top_aleinu = sorted(aleinu_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    for root, count in top_aleinu:
        ashrei_count = ashrei_counts.get(root, 0)
        print(f"  {root:15} → {count:2}x in Aleinu, {ashrei_count:2}x in Ashrei")

    # Top roots combined
    print("\nTop 15 Roots ACROSS BOTH PRAYERS:")
    top_combined = sorted(combined_counts.items(), key=lambda x: x[1], reverse=True)[:15]
    for root, total in top_combined:
        a_count = ashrei_counts.get(root, 0)
        l_count = aleinu_counts.get(root, 0)
        print(f"  {root:15} → {total:2}x total ({a_count:2}x Ashrei + {l_count:2}x Aleinu)")

def main():
    print("=" * 70)
    print("COMPLETE SHORESH SYSTEM FOR ASHREI AND ALEINU")
    print("=" * 70)

    # Add shoresh to all words
    ashrei = add_shoresh_to_all_words("ashrei")
    aleinu = add_shoresh_to_all_words("aleinu")

    # Calculate frequencies within each prayer
    print("\n" + "=" * 70)
    print("CALCULATING ROOT FREQUENCIES")
    print("=" * 70)

    ashrei_counts = calculate_root_frequencies(ashrei, "ashrei")
    aleinu_counts = calculate_root_frequencies(aleinu, "aleinu")

    print(f"✓ Calculated frequencies for {len(ashrei_counts)} unique roots in Ashrei")
    print(f"✓ Calculated frequencies for {len(aleinu_counts)} unique roots in Aleinu")

    # Calculate combined frequencies
    combined_counts = calculate_combined_frequencies(ashrei, aleinu)
    print(f"✓ Calculated combined frequencies across {len(combined_counts)} unique roots")

    # Save updated prayers
    save_prayer("ashrei", ashrei)
    save_prayer("aleinu", aleinu)

    # Show analysis
    show_frequency_analysis(ashrei_counts, aleinu_counts, combined_counts)

    print("\n" + "=" * 70)
    print("✅ COMPLETE!")
    print("=" * 70)
    print("All words in Ashrei and Aleinu now have:")
    print("  • shoresh (3-letter root)")
    print("  • root meaning")
    print("  • word type")
    print("  • frequency_in_[prayer]")
    print("  • frequency_across_prayers")

if __name__ == '__main__':
    main()
