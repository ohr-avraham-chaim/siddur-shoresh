#!/usr/bin/env python3
"""Build Birkat Kohanim, Eilu Devarim texts, and Elohai Neshama."""

import json
import re
from collections import defaultdict

def get_common_roots():
    """Common roots across prayers."""
    return {
        "ה'": {"trans": "Hashem", "root": "ה-ו-י", "meaning": "God's name (YHVH)", "type": "proper noun"},
        "בָּרוּךְ": {"trans": "Blessed", "root": "ב-ר-כ", "meaning": "blessing, knee", "type": "adjective"},
        "אַתָּה": {"trans": "You are", "root": "א-ת-ת", "meaning": "you (masculine singular)", "type": "pronoun"},
        "אֱלהֵינוּ": {"trans": "our God", "root": "א-ל-ה", "meaning": "God, deity", "type": "noun"},
        "מֶלֶךְ": {"trans": "King", "root": "מ-ל-כ", "meaning": "kingship, ruling", "type": "noun"},
        "הָעולָם": {"trans": "of the world / universe", "root": "ע-ל-מ", "meaning": "eternity, world", "type": "noun"},
        "אֶת": {"trans": "(direct object marker)", "root": "א-ת-ת", "meaning": "direct object marker", "type": "particle"},
        "וְ": {"trans": "and", "root": "ו", "meaning": "and", "type": "conjunction"},
        "כָּל": {"trans": "all", "root": "כ-ל-ל", "meaning": "all, every", "type": "noun"},
    }

def get_birkat_kohanim_mappings():
    """Priestly Blessing mappings."""
    mappings = get_common_roots()
    mappings.update({
        "וַיְדַבֵּר": {"trans": "And [He] spoke", "root": "ד-ב-ר", "meaning": "speak, word", "type": "verb"},
        "אֶל": {"trans": "to", "root": "א-ל", "meaning": "to, toward", "type": "preposition"},
        "משֶׁה": {"trans": "Moses", "root": "מ-ש-ה", "meaning": "Moses (proper name)", "type": "proper noun"},
        "לֵּאמר.": {"trans": "saying", "root": "א-מ-ר", "meaning": "say, speak", "type": "verb"},
        "לֵּאמר": {"trans": "saying", "root": "א-מ-ר", "meaning": "say, speak", "type": "verb"},
        "דַּבֵּר": {"trans": "Speak", "root": "ד-ב-ר", "meaning": "speak, word", "type": "verb"},
        "אַהֲרן": {"trans": "Aaron", "root": "א-ה-ר", "meaning": "Aaron (proper name)", "type": "proper noun"},
        "וְאֶל": {"trans": "and to", "root": "א-ל", "meaning": "to, toward", "type": "preposition"},
        "בָּנָיו": {"trans": "his sons", "root": "ב-נ-נ", "meaning": "son, child", "type": "noun"},
        "כּה": {"trans": "thus / so", "root": "כ-כ-ה", "meaning": "thus, so", "type": "adverb"},
        "תְבָרְכוּ": {"trans": "you shall bless", "root": "ב-ר-כ", "meaning": "bless", "type": "verb"},
        "בְּנֵי": {"trans": "children of", "root": "ב-נ-נ", "meaning": "son, child", "type": "noun"},
        "יִשרָאֵל": {"trans": "Israel", "root": "י-ש-ר", "meaning": "straight, Israel", "type": "proper noun"},
        "אָמור": {"trans": "saying", "root": "א-מ-ר", "meaning": "say, speak", "type": "verb"},
        "לָהֶם]:": {"trans": "to them", "root": "ה-מ-מ", "meaning": "they, them", "type": "pronoun"},
        "יְבָרֶכְךָ": {"trans": "May He bless you", "root": "ב-ר-כ", "meaning": "bless", "type": "verb"},
        "וְיִשְׁמְרֶךָ:": {"trans": "and guard you", "root": "ש-מ-ר", "meaning": "guard, keep, protect", "type": "verb"},
        "יָאֵר": {"trans": "May He illuminate", "root": "א-ו-ר", "meaning": "light", "type": "verb"},
        "פָּנָיו": {"trans": "His face", "root": "פ-נ-נ", "meaning": "face", "type": "noun"},
        "אֵלֶיךָ": {"trans": "to you", "root": "א-ל", "meaning": "to, toward", "type": "preposition"},
        "וִיחֻנֶּךָּ:": {"trans": "and be gracious to you", "root": "ח-נ-נ", "meaning": "favor, grace", "type": "verb"},
        "יִשּא": {"trans": "May He lift up", "root": "נ-ש-א", "meaning": "lift, carry, bear", "type": "verb"},
        "וְיָשם": {"trans": "and grant", "root": "ש-ו-מ", "meaning": "place, put, grant", "type": "verb"},
        "לְךָ": {"trans": "to you", "root": "ל", "meaning": "to, for", "type": "preposition"},
        "שָׁלום:": {"trans": "peace", "root": "ש-ל-מ", "meaning": "peace, wholeness", "type": "noun"},
    })
    return mappings

def get_eilu_devarim_1_mappings():
    """First Eilu Devarim mappings."""
    mappings = get_common_roots()
    mappings.update({
        "אֵלּוּ": {"trans": "These are", "root": "א-ל-ה", "meaning": "these", "type": "demonstrative"},
        "דְבָרִים": {"trans": "things / matters", "root": "ד-ב-ר", "meaning": "thing, word, matter", "type": "noun"},
        "שֶׁאֵין": {"trans": "that have no", "root": "א-י-נ", "meaning": "there is not", "type": "negative"},
        "לָהֶם": {"trans": "for them", "root": "ה-מ-מ", "meaning": "they, them", "type": "pronoun"},
        "שִׁעוּר.": {"trans": "measure / limit", "root": "ש-ע-ר", "meaning": "measure, estimate", "type": "noun"},
        "הַפֵּאָה": {"trans": "the corner [of field]", "root": "פ-א-ה", "meaning": "corner, edge", "type": "noun"},
        "וְהַבִּכּוּרִים": {"trans": "and the first fruits", "root": "ב-כ-ר", "meaning": "firstborn, first fruits", "type": "noun"},
        "וְהָרְאָיון": {"trans": "and the pilgrimage offering", "root": "ר-א-ה", "meaning": "see, appear", "type": "noun"},
        "וּגְמִילוּת": {"trans": "and acts of", "root": "ג-מ-ל", "meaning": "give, bestow, repay", "type": "noun"},
        "חֲסָדִים": {"trans": "kindness / loving-kindness", "root": "ח-ס-ד", "meaning": "kindness, loyalty", "type": "noun"},
        "וְתַלְמוּד": {"trans": "and study of", "root": "ל-מ-ד", "meaning": "learn, teach", "type": "noun"},
        "תּורָה:": {"trans": "Torah", "root": "י-ר-ה", "meaning": "teach, instruct, Torah", "type": "noun"},
    })
    return mappings

def get_eilu_devarim_2_mappings():
    """Second Eilu Devarim mappings."""
    mappings = get_common_roots()
    mappings.update({
        "אֵלּוּ": {"trans": "These are", "root": "א-ל-ה", "meaning": "these", "type": "demonstrative"},
        "דְבָרִים": {"trans": "things / matters", "root": "ד-ב-ר", "meaning": "thing, word, matter", "type": "noun"},
        "שֶׁאָדָם": {"trans": "that a person", "root": "א-ד-מ", "meaning": "human, man", "type": "noun"},
        "אוכֵל": {"trans": "eats / enjoys", "root": "א-כ-ל", "meaning": "eat", "type": "verb"},
        "פֵּרותֵיהֶם": {"trans": "their fruits", "root": "פ-ר-ה", "meaning": "fruit, produce", "type": "noun"},
        "בָּעולָם": {"trans": "in the world", "root": "ע-ל-מ", "meaning": "world, eternity", "type": "noun"},
        "הַזֶּה": {"trans": "this", "root": "ז-ה-ה", "meaning": "this", "type": "demonstrative"},
        "וְהַקֶּרֶן": {"trans": "and the principal", "root": "ק-ר-נ", "meaning": "horn, principal", "type": "noun"},
        "קַיֶּמֶת": {"trans": "remains / endures", "root": "ק-ו-מ", "meaning": "stand, exist", "type": "verb"},
        "לו": {"trans": "for him", "root": "ל", "meaning": "to, for", "type": "preposition"},
        "לָעולָם": {"trans": "for the world", "root": "ע-ל-מ", "meaning": "world, eternity", "type": "noun"},
        "הַבָּא.": {"trans": "to come", "root": "ב-ו-א", "meaning": "come, enter", "type": "verb"},
        "וְאֵלּוּ": {"trans": "and these are", "root": "א-ל-ה", "meaning": "these", "type": "demonstrative"},
        "הֵן.": {"trans": "they", "root": "ה-נ-נ", "meaning": "behold, they", "type": "pronoun"},
        "כִּבּוּד": {"trans": "honoring", "root": "כ-ב-ד", "meaning": "weight, honor, glory", "type": "noun"},
        "אָב": {"trans": "father", "root": "א-ב-ב", "meaning": "father", "type": "noun"},
        "וָאֵם.": {"trans": "and mother", "root": "א-מ-מ", "meaning": "mother", "type": "noun"},
        "וּגְמִילוּת": {"trans": "and acts of", "root": "ג-מ-ל", "meaning": "give, bestow", "type": "noun"},
        "חֲסָדִים.": {"trans": "kindness", "root": "ח-ס-ד", "meaning": "kindness, loyalty", "type": "noun"},
        "וְהַשְׁכָּמַת": {"trans": "and early attendance at", "root": "ש-כ-מ", "meaning": "rise early", "type": "noun"},
        "בֵּית": {"trans": "house of", "root": "ב-י-ת", "meaning": "house", "type": "noun"},
        "הַמִּדְרָשׁ.": {"trans": "study", "root": "ד-ר-ש", "meaning": "seek, study", "type": "noun"},
        "שַׁחֲרִית": {"trans": "morning", "root": "ש-ח-ר", "meaning": "dawn, morning", "type": "noun"},
        "וְעַרְבִית.": {"trans": "and evening", "root": "ע-ר-ב", "meaning": "evening", "type": "noun"},
        "וְהַכְנָסַת": {"trans": "and bringing in", "root": "כ-נ-ס", "meaning": "enter, gather", "type": "noun"},
        "אורְחִים.": {"trans": "guests", "root": "א-ר-ח", "meaning": "path, guest", "type": "noun"},
        "וּבִקּוּר": {"trans": "and visiting", "root": "ב-ק-ר", "meaning": "visit, examine", "type": "noun"},
        "חולִים.": {"trans": "the sick", "root": "ח-ל-ה", "meaning": "sick, weak", "type": "adjective"},
        "וְהַכְנָסַת": {"trans": "and bringing in", "root": "כ-נ-ס", "meaning": "enter, gather", "type": "noun"},
        "כַּלָּה.": {"trans": "a bride", "root": "כ-ל-ה", "meaning": "bride, complete", "type": "noun"},
        "וּלְוָיַת": {"trans": "and accompanying", "root": "ל-ו-ה", "meaning": "accompany, escort", "type": "noun"},
        "הַמֵּת.": {"trans": "the deceased", "root": "מ-ו-ת", "meaning": "death, die", "type": "noun"},
        "וְעִיּוּן": {"trans": "and concentration in", "root": "ע-י-נ", "meaning": "eye, attention", "type": "noun"},
        "תפילה.": {"trans": "prayer", "root": "פ-ל-ל", "meaning": "pray, judge", "type": "noun"},
        "וַהֲבָאַת": {"trans": "and making", "root": "ב-ו-א", "meaning": "bring, come", "type": "verb"},
        "שָׁלום": {"trans": "peace", "root": "ש-ל-מ", "meaning": "peace, wholeness", "type": "noun"},
        "בֵּין": {"trans": "between", "root": "ב-י-נ", "meaning": "between", "type": "preposition"},
        "אָדָם": {"trans": "person", "root": "א-ד-מ", "meaning": "human, man", "type": "noun"},
        "לַחֲבֵרו": {"trans": "to his fellow", "root": "ח-ב-ר", "meaning": "join, friend", "type": "noun"},
        "וּבֵין": {"trans": "and between", "root": "ב-י-נ", "meaning": "between", "type": "preposition"},
        "אִישׁ": {"trans": "a man", "root": "א-י-ש", "meaning": "man, husband", "type": "noun"},
        "לְאִשְׁתּו.": {"trans": "to his wife", "root": "א-ש-ה", "meaning": "woman, wife", "type": "noun"},
        "וְתַלְמוּד": {"trans": "and study of", "root": "ל-מ-ד", "meaning": "learn, teach", "type": "noun"},
        "תּורָה": {"trans": "Torah", "root": "י-ר-ה", "meaning": "Torah, teach", "type": "noun"},
        "כְּנֶגֶד": {"trans": "equal to / opposite", "root": "נ-ג-ד", "meaning": "opposite, before", "type": "preposition"},
        "כֻּלָּם:": {"trans": "all of them", "root": "כ-ל-ל", "meaning": "all, every", "type": "noun"},
    })
    return mappings

def get_elohai_neshama_mappings():
    """Elohai Neshama mappings."""
    mappings = get_common_roots()
    mappings.update({
        "אֱלהַי.": {"trans": "My God", "root": "א-ל-ה", "meaning": "God, deity", "type": "noun"},
        "נְשָׁמָה": {"trans": "soul", "root": "נ-ש-מ", "meaning": "soul, breath", "type": "noun"},
        "שֶׁנָּתַתָּ": {"trans": "that You gave", "root": "נ-ת-נ", "meaning": "give", "type": "verb"},
        "בִּי": {"trans": "in me", "root": "ב-ב-ב", "meaning": "in", "type": "preposition"},
        "טְהורָה": {"trans": "pure", "root": "ט-ה-ר", "meaning": "pure, clean", "type": "adjective"},
        "הִיא.": {"trans": "it is", "root": "ה-י-א", "meaning": "she, it", "type": "pronoun"},
        "בְרָאתָהּ.": {"trans": "You created it", "root": "ב-ר-א", "meaning": "create", "type": "verb"},
        "יְצַרְתָּהּ.": {"trans": "You formed it", "root": "י-צ-ר", "meaning": "form, create", "type": "verb"},
        "נְפַחְתָּהּ": {"trans": "You breathed it", "root": "נ-פ-ח", "meaning": "blow, breathe", "type": "verb"},
        "מְשַׁמְּרָהּ": {"trans": "You guard it", "root": "ש-מ-ר", "meaning": "guard, keep", "type": "verb"},
        "בְּקִרְבִּי.": {"trans": "within me", "root": "ק-ר-ב", "meaning": "near, midst", "type": "noun"},
        "עָתִיד": {"trans": "destined / will", "root": "ע-ת-ד", "meaning": "ready, destined", "type": "adjective"},
        "לִטְּלָהּ": {"trans": "to take it", "root": "נ-ט-ל", "meaning": "take, lift", "type": "verb"},
        "מִמֶּנִּי.": {"trans": "from me", "root": "מ-נ-נ", "meaning": "from", "type": "preposition"},
        "וּלְהַחֲזִירָהּ": {"trans": "and to return it", "root": "ח-ז-ר", "meaning": "return", "type": "verb"},
        "לֶעָתִיד": {"trans": "in the future", "root": "ע-ת-ד", "meaning": "future, destined", "type": "noun"},
        "לָבוא.": {"trans": "to come", "root": "ב-ו-א", "meaning": "come, enter", "type": "verb"},
        "זְמַן": {"trans": "time", "root": "ז-מ-נ", "meaning": "time, season", "type": "noun"},
        "שֶׁהַנְּשָׁמָה": {"trans": "that the soul", "root": "נ-ש-מ", "meaning": "soul, breath", "type": "noun"},
        "בְּקִרְבִּי": {"trans": "within me", "root": "ק-ר-ב", "meaning": "near, midst", "type": "noun"},
        "מודֶה": {"trans": "I give thanks", "root": "י-ד-ה", "meaning": "thank, praise", "type": "verb"},
        "אֲנִי": {"trans": "I", "root": "א-נ-י", "meaning": "I", "type": "pronoun"},
        "לְפָנֶיךָ": {"trans": "before You", "root": "פ-נ-נ", "meaning": "face, before", "type": "preposition"},
        "אֱלהַי": {"trans": "my God", "root": "א-ל-ה", "meaning": "God, deity", "type": "noun"},
        "וֵאלהֵי": {"trans": "and God of", "root": "א-ל-ה", "meaning": "God, deity", "type": "noun"},
        "אֲבותַי.": {"trans": "my fathers", "root": "א-ב-ב", "meaning": "father", "type": "noun"},
        "רִבּון": {"trans": "Master of", "root": "ר-ב-ב", "meaning": "master, great", "type": "noun"},
        "הַמַּעֲשים": {"trans": "the works / deeds", "root": "ע-ש-ה", "meaning": "do, make", "type": "noun"},
        "אֲדון": {"trans": "Lord of", "root": "א-ד-נ", "meaning": "lord, master", "type": "noun"},
        "הַנְּשָׁמות:": {"trans": "the souls", "root": "נ-ש-מ", "meaning": "soul, breath", "type": "noun"},
        "הַמַּחֲזִיר": {"trans": "Who returns", "root": "ח-ז-ר", "meaning": "return", "type": "verb"},
        "נְשָׁמות": {"trans": "souls", "root": "נ-ש-מ", "meaning": "soul, breath", "type": "noun"},
        "לִפְגָרִים": {"trans": "to corpses / bodies", "root": "פ-ג-ר", "meaning": "corpse, body", "type": "noun"},
        "מֵתִים:": {"trans": "dead", "root": "מ-ו-ת", "meaning": "death, die", "type": "adjective"},
    })
    return mappings

def build_text(text, mappings, text_name, hebrew_name):
    """Build embedded JSON for a text."""

    # Parse words
    final_words = text.replace('[', '').replace(']', '').replace('.', '. ').replace(':', ': ').split()

    # Initialize structure
    data = {
        "text_name": {
            "hebrew": hebrew_name,
            "english": text_name
        },
        "words": {},
        "sentences": {}
    }

    # Count word frequency
    word_frequency = defaultdict(int)
    for raw_word in final_words:
        word_clean = re.sub(r'[׃:.\[\]]', '', raw_word)
        word_frequency[word_clean] += 1

    # Build words
    word_id = 1
    sentence_num = 1
    sentence_word_ids = []

    for raw_word in final_words:
        word_clean = re.sub(r'[׃:.\[\]]', '', raw_word)
        punctuation = ''
        for char in raw_word:
            if char in '׃:.\[\]':
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
        sentence_word_ids.append(f"w{word_id}")

        # Check if end of sentence
        if ':' in punctuation or '.' in punctuation:
            data["sentences"][f"s{sentence_num}"] = {
                "id": f"s{sentence_num}",
                "word_ids": sentence_word_ids,
                "hebrew": ' '.join(data["words"][wid]["hebrew"] for wid in sentence_word_ids)
            }
            sentence_num += 1
            sentence_word_ids = []

        word_id += 1

    # If there are remaining words (no final punctuation), add as sentence
    if sentence_word_ids:
        data["sentences"][f"s{sentence_num}"] = {
            "id": f"s{sentence_num}",
            "word_ids": sentence_word_ids,
            "hebrew": ' '.join(data["words"][wid]["hebrew"] for wid in sentence_word_ids)
        }

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
    texts_data = [
        {
            "text": "וַיְדַבֵּר ה' אֶל משֶׁה לֵּאמר. דַּבֵּר אֶל אַהֲרן וְאֶל בָּנָיו לֵּאמר. כּה תְבָרְכוּ אֶת בְּנֵי יִשרָאֵל אָמור לָהֶם]: יְבָרֶכְךָ ה' וְיִשְׁמְרֶךָ: יָאֵר ה' פָּנָיו אֵלֶיךָ וִיחֻנֶּךָּ: יִשּא ה' פָּנָיו אֵלֶיךָ וְיָשם לְךָ שָׁלום:",
            "mappings": get_birkat_kohanim_mappings(),
            "filename": "birkat_kohanim",
            "name": "Birkat Kohanim - Priestly Blessing",
            "hebrew": "בִּרְכַּת כֹּהֲנִים"
        },
        {
            "text": "אֵלּוּ דְבָרִים שֶׁאֵין לָהֶם שִׁעוּר. הַפֵּאָה וְהַבִּכּוּרִים וְהָרְאָיון וּגְמִילוּת חֲסָדִים וְתַלְמוּד תּורָה:",
            "mappings": get_eilu_devarim_1_mappings(),
            "filename": "eilu_devarim_1",
            "name": "Eilu Devarim 1 - Things Without Measure",
            "hebrew": "אֵלּוּ דְבָרִים (א)"
        },
        {
            "text": "אֵלּוּ דְבָרִים שֶׁאָדָם אוכֵל פֵּרותֵיהֶם בָּעולָם הַזֶּה וְהַקֶּרֶן קַיֶּמֶת לו לָעולָם הַבָּא. וְאֵלּוּ הֵן. כִּבּוּד אָב וָאֵם. וּגְמִילוּת חֲסָדִים. וְהַשְׁכָּמַת בֵּית הַמִּדְרָשׁ. שַׁחֲרִית וְעַרְבִית. וְהַכְנָסַת אורְחִים. וּבִקּוּר חולִים. וְהַכְנָסַת כַּלָּה. וּלְוָיַת הַמֵּת. וְעִיּוּן תפילה. וַהֲבָאַת שָׁלום בֵּין אָדָם לַחֲבֵרו וּבֵין אִישׁ לְאִשְׁתּו. וְתַלְמוּד תּורָה כְּנֶגֶד כֻּלָּם:",
            "mappings": get_eilu_devarim_2_mappings(),
            "filename": "eilu_devarim_2",
            "name": "Eilu Devarim 2 - Fruits in This World",
            "hebrew": "אֵלּוּ דְבָרִים (ב)"
        },
        {
            "text": "אֱלהַי. נְשָׁמָה שֶׁנָּתַתָּ בִּי טְהורָה הִיא. אַתָּה בְרָאתָהּ. אַתָּה יְצַרְתָּהּ. אַתָּה נְפַחְתָּהּ בִּי. וְאַתָּה מְשַׁמְּרָהּ בְּקִרְבִּי. וְאַתָּה עָתִיד לִטְּלָהּ מִמֶּנִּי. וּלְהַחֲזִירָהּ בִּי לֶעָתִיד לָבוא. כָּל זְמַן שֶׁהַנְּשָׁמָה בְּקִרְבִּי מודֶה אֲנִי לְפָנֶיךָ ה' אֱלהַי וֵאלהֵי אֲבותַי. רִבּון כָּל הַמַּעֲשים אֲדון כָּל הַנְּשָׁמות: בָּרוּךְ אַתָּה ה' הַמַּחֲזִיר נְשָׁמות לִפְגָרִים מֵתִים:",
            "mappings": get_elohai_neshama_mappings(),
            "filename": "elohai_neshama",
            "name": "Elohai Neshama - My God, the Soul",
            "hebrew": "אֱלהַי נְשָׁמָה"
        },
    ]

    print("="*60)
    print("Building Morning Texts")
    print("="*60)

    total_words = 0
    total_roots = set()

    for text_data in texts_data:
        print(f"\nBuilding {text_data['name']}...")

        text = build_text(
            text_data["text"],
            text_data["mappings"],
            text_data["name"],
            text_data["hebrew"]
        )

        # Save
        filename = f"data/{text_data['filename']}_embedded.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(text, f, ensure_ascii=False, indent=2)

        # Stats
        words = len(text["words"])
        with_trans = sum(1 for w in text["words"].values() if "translation" in w)
        with_shoresh = sum(1 for w in text["words"].values() if "shoresh" in w)
        unique_roots = set(w["shoresh"]["root"] for w in text["words"].values() if "shoresh" in w)

        print(f"   Words: {words}")
        print(f"   Translations: {with_trans}/{words} ({100*with_trans/words:.1f}%)")
        print(f"   With shoresh: {with_shoresh}/{words} ({100*with_shoresh/words:.1f}%)")
        print(f"   Unique roots: {len(unique_roots)}")
        print(f"   Sentences: {len(text['sentences'])}")

        total_words += words
        total_roots.update(unique_roots)

    print("\n" + "="*60)
    print("MORNING TEXTS COMPLETE")
    print("="*60)
    print(f"Total words across 4 texts: {total_words}")
    print(f"Total unique roots: {len(total_roots)}")
    print("✅ All morning texts complete!")

if __name__ == "__main__":
    main()
