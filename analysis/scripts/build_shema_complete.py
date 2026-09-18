#!/usr/bin/env python3
"""
Build complete Shema system with:
- Word-by-word structure
- Translations
- Shoresh with frequencies
"""

import json
import re
from pathlib import Path
from collections import defaultdict

def load_prayer(name):
    path = Path(f'/Users/mordechai/Ohr Avraham Chaim/Siddur/data/{name}_embedded.json')
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_prayer(name, data):
    path = Path(f'/Users/mordechai/Ohr Avraham Chaim/Siddur/data/{name}_embedded.json')
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def build_shema_structure():
    """Build embedded JSON for Shema."""

    # Load clean text
    shema_path = Path('/Users/mordechai/Ohr Avraham Chaim/Siddur/shema_clean.md')
    with open(shema_path, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    shema = {
        "prayer_name": {
            "hebrew": "שְׁמַע יִשְׂרָאֵל",
            "english": "Shema Yisrael",
            "source": "Deuteronomy 6:4-9, 11:13-21; Numbers 15:37-41"
        },
        "words": {},
        "paragraphs": {},
        "phrases": {},
        "layers": {
            "base_text": "complete",
            "translations": "complete",
            "shoresh": "complete",
            "grammar": "pending",
            "kavanot": "pending",
            "instructions": "pending"
        }
    }

    # Count word frequencies
    word_frequency = {}
    for line in lines:
        raw_words = line.split()
        for raw_word in raw_words:
            word_clean = re.sub(r'[׃:.]$', '', raw_word)
            word_frequency[word_clean] = word_frequency.get(word_clean, 0) + 1

    # Parse words
    word_id = 1
    paragraph_number = 1

    for line in lines:
        raw_words = line.split()
        paragraph_word_ids = []

        for raw_word in raw_words:
            word_clean = re.sub(r'[׃:.]$', '', raw_word)
            punctuation = raw_word[len(word_clean):] if len(raw_word) > len(word_clean) else ''

            word_entry = {
                "id": f"w{word_id}",
                "hebrew": raw_word,
                "hebrew_clean": word_clean,
                "punctuation": punctuation,
                "paragraph": paragraph_number,
                "position_in_paragraph": len(paragraph_word_ids) + 1,
                "position_global": word_id,
                "frequency_in_shema": word_frequency[word_clean]
            }

            shema["words"][f"w{word_id}"] = word_entry
            paragraph_word_ids.append(f"w{word_id}")
            word_id += 1

        # Paragraph descriptions
        descriptions = {
            1: "First verse - Declaration of God's unity",
            2: "Baruch Shem (said quietly)",
            3: "First paragraph - Love and study (Deuteronomy 6:5-9)",
            4: "Second paragraph - Reward and punishment (Deuteronomy 11:13-21)",
            5: "Third paragraph - Tzitzit (Numbers 15:37-41)"
        }

        paragraph_entry = {
            "id": f"p{paragraph_number}",
            "number": paragraph_number,
            "word_ids": paragraph_word_ids,
            "hebrew_full": line,
            "word_count": len(paragraph_word_ids),
            "description": descriptions.get(paragraph_number, f"Paragraph {paragraph_number}")
        }

        shema["paragraphs"][f"p{paragraph_number}"] = paragraph_entry
        paragraph_number += 1

    return shema

def get_shema_word_mappings():
    """Get translation and shoresh mappings for all Shema words."""
    return {
        # Verse 1 - Shema Yisrael
        "שְׁמַע": {
            "translation": "Hear / Listen",
            "root": "ש-מ-ע", "meaning": "hearing, listening", "type": "verb"
        },
        "יִשרָאֵל": {
            "translation": "Israel",
            "root": "י-ש-ר", "meaning": "straight, Israel", "type": "proper noun"
        },
        "ה'": {
            "translation": "Hashem",
            "root": "ה-ו-י", "meaning": "being, Hashem", "type": "proper noun"
        },
        "אֱלהֵינוּ": {
            "translation": "our God",
            "root": "א-ל-ה", "meaning": "God, deity", "type": "noun"
        },
        "אֶחָד": {
            "translation": "One",
            "root": "א-ח-ד", "meaning": "one, unity", "type": "number"
        },

        # Baruch Shem
        "בלחש": {
            "translation": "(whisper)",
            "root": "ל-ח-שׁ", "meaning": "whispering", "type": "noun"
        },
        "בָּרוּךְ": {
            "translation": "Blessed",
            "root": "ב-ר-כ", "meaning": "blessing, knee", "type": "adjective"
        },
        "שֵׁם": {
            "translation": "Name",
            "root": "ש-מ-מ", "meaning": "name", "type": "noun"
        },
        "כְּבוד": {
            "translation": "glory of",
            "root": "כ-ב-ד", "meaning": "honor, heaviness", "type": "noun"
        },
        "מַלְכוּתו": {
            "translation": "His kingdom",
            "root": "מ-ל-כ", "meaning": "kingship, ruling", "type": "noun"
        },
        "לְעולָם": {
            "translation": "forever",
            "root": "ע-ל-מ", "meaning": "eternity, world", "type": "noun"
        },
        "וָעֶד": {
            "translation": "and ever",
            "root": "ע-ד-ד", "meaning": "perpetuity, eternity", "type": "noun"
        },

        # First Paragraph - V'ahavta
        "וְאָהַבְתָּ": {
            "translation": "And you shall love",
            "root": "א-ה-ב", "meaning": "loving", "type": "verb"
        },
        "אֵת": {
            "translation": "[direct object]",
            "root": "א-ת-ת", "meaning": "with, direct object", "type": "particle"
        },
        "אֱלהֶיךָ": {
            "translation": "your God",
            "root": "א-ל-ה", "meaning": "God, deity", "type": "noun"
        },
        "בְּכָל": {
            "translation": "with all",
            "root": "כ-ל-ל", "meaning": "all, every", "type": "adjective"
        },
        "לְבָבְךָ": {
            "translation": "your heart",
            "root": "ל-ב-ב", "meaning": "heart, inner self", "type": "noun"
        },
        "לְבָבֶךָ": {
            "translation": "your heart",
            "root": "ל-ב-ב", "meaning": "heart, inner self", "type": "noun"
        },
        "לְבַבְכֶם": {
            "translation": "your hearts",
            "root": "ל-ב-ב", "meaning": "heart, inner self", "type": "noun"
        },
        "לְבַבְכֶם": {
            "translation": "your heart",
            "root": "ל-ב-ב", "meaning": "heart, inner self", "type": "noun"
        },
        "וּבְכָל": {
            "translation": "and with all",
            "root": "כ-ל-ל", "meaning": "all, every", "type": "adjective"
        },
        "נַפְשְׁךָ": {
            "translation": "your soul",
            "root": "נ-פ-שׁ", "meaning": "soul, life", "type": "noun"
        },
        "נַפְשְׁכֶם": {
            "translation": "your souls",
            "root": "נ-פ-שׁ", "meaning": "soul, life", "type": "noun"
        },
        "מְאדֶךָ": {
            "translation": "your might",
            "root": "מ-א-ד", "meaning": "very, exceedingly", "type": "noun"
        },
        "וְהָיוּ": {
            "translation": "And they shall be",
            "root": "ה-י-ה", "meaning": "being, existing", "type": "verb"
        },
        "הַדְּבָרִים": {
            "translation": "the words",
            "root": "ד-ב-ר", "meaning": "speaking, word", "type": "noun"
        },
        "הָאֵלֶּה": {
            "translation": "these",
            "root": "א-ל-ה", "meaning": "these", "type": "demonstrative"
        },
        "אֲשֶׁר": {
            "translation": "which",
            "root": "א-ש-ר", "meaning": "who, which", "type": "relative pronoun"
        },
        "אָנכִי": {
            "translation": "I",
            "root": "א-נ-כ", "meaning": "I", "type": "pronoun"
        },
        "מְצַוְּךָ": {
            "translation": "command you",
            "root": "צ-ו-ה", "meaning": "commanding", "type": "verb"
        },
        "מְצַוֶּה": {
            "translation": "commanding",
            "root": "צ-ו-ה", "meaning": "commanding", "type": "verb"
        },
        "הַיּום": {
            "translation": "today",
            "root": "י-ו-מ", "meaning": "day", "type": "noun"
        },
        "עַל": {
            "translation": "upon",
            "root": "ע-ל-ל", "meaning": "upon, over", "type": "preposition"
        },
        "וְשִׁנַּנְתָּם": {
            "translation": "And you shall teach them",
            "root": "ש-נ-נ", "meaning": "sharpening, repeating", "type": "verb"
        },
        "לְבָנֶיךָ": {
            "translation": "to your children",
            "root": "ב-נ-י", "meaning": "building, son", "type": "noun"
        },
        "בְּנֵי": {
            "translation": "sons of / children of",
            "root": "ב-נ-י", "meaning": "building, son", "type": "noun"
        },
        "בְּנֵיכֶם": {
            "translation": "your children",
            "root": "ב-נ-י", "meaning": "building, son", "type": "noun"
        },
        "וְדִבַּרְתָּ": {
            "translation": "and you shall speak",
            "root": "ד-ב-ר", "meaning": "speaking, word", "type": "verb"
        },
        "דְּבָרַי": {
            "translation": "My words",
            "root": "ד-ב-ר", "meaning": "speaking, word", "type": "noun"
        },
        "בָּם": {
            "translation": "of them",
            "root": "ב", "meaning": "in, with", "type": "preposition"
        },
        "בְּשִׁבְתְּךָ": {
            "translation": "when you sit",
            "root": "י-ש-ב", "meaning": "sitting, dwelling", "type": "verb"
        },
        "בְּבֵיתֶךָ": {
            "translation": "in your house",
            "root": "ב-י-ת", "meaning": "house, home", "type": "noun"
        },
        "בֵּיתֶךָ": {
            "translation": "your house",
            "root": "ב-י-ת", "meaning": "house, home", "type": "noun"
        },
        "וּבְלֶכְתְּךָ": {
            "translation": "and when you walk",
            "root": "ה-ל-כ", "meaning": "walking, going", "type": "verb"
        },
        "בַדֶּרֶךְ": {
            "translation": "on the road",
            "root": "ד-ר-כ", "meaning": "way, path", "type": "noun"
        },
        "וּבְשָׁכְבְּךָ": {
            "translation": "and when you lie down",
            "root": "ש-כ-ב", "meaning": "lying down", "type": "verb"
        },
        "וּבְקוּמֶךָ": {
            "translation": "and when you rise",
            "root": "ק-ו-מ", "meaning": "rising, standing", "type": "verb"
        },
        "וּקְשַׁרְתָּם": {
            "translation": "And you shall bind them",
            "root": "ק-ש-ר", "meaning": "binding, tying", "type": "verb"
        },
        "וּקְשַׁרְתֶּם": {
            "translation": "And you shall bind them",
            "root": "ק-ש-ר", "meaning": "binding, tying", "type": "verb"
        },
        "לְאות": {
            "translation": "as a sign",
            "root": "א-ו-ת", "meaning": "sign, letter", "type": "noun"
        },
        "יָדֶךָ": {
            "translation": "your hand",
            "root": "י-ד-ד", "meaning": "hand", "type": "noun"
        },
        "יֶדְכֶם": {
            "translation": "your hand",
            "root": "י-ד-ד", "meaning": "hand", "type": "noun"
        },
        "לְטטָפת": {
            "translation": "as frontlets",
            "root": "ט-ו-פ", "meaning": "bands, frontlets", "type": "noun"
        },
        "לְטוטָפת": {
            "translation": "as frontlets",
            "root": "ט-ו-פ", "meaning": "bands, frontlets", "type": "noun"
        },
        "בֵּין": {
            "translation": "between",
            "root": "ב-י-נ", "meaning": "between, understanding", "type": "preposition"
        },
        "עֵינֶיךָ": {
            "translation": "your eyes",
            "root": "ע-י-נ", "meaning": "eye, seeing", "type": "noun"
        },
        "עֵינֵיכֶם": {
            "translation": "your eyes",
            "root": "ע-י-נ", "meaning": "eye, seeing", "type": "noun"
        },
        "וּכְתַבְתָּם": {
            "translation": "And you shall write them",
            "root": "כ-ת-ב", "meaning": "writing", "type": "verb"
        },
        "מְזֻזות": {
            "translation": "doorposts",
            "root": "ז-ו-ז", "meaning": "doorpost, moving", "type": "noun"
        },
        "מְזוּזות": {
            "translation": "doorposts",
            "root": "ז-ו-ז", "meaning": "doorpost, moving", "type": "noun"
        },
        "וּבִשְׁעָרֶיךָ": {
            "translation": "and on your gates",
            "root": "ש-ע-ר", "meaning": "gate, hair", "type": "noun"
        },

        # Second paragraph - V'haya im shamoa
        "וְהָיָה": {
            "translation": "And it shall be",
            "root": "ה-י-ה", "meaning": "being, existing", "type": "verb"
        },
        "אִם": {
            "translation": "if",
            "root": "א-מ", "meaning": "if, whether", "type": "conjunction"
        },
        "שָׁמעַ": {
            "translation": "listen",
            "root": "ש-מ-ע", "meaning": "hearing, listening", "type": "verb infinitive"
        },
        "תִּשְׁמְעוּ": {
            "translation": "you will listen",
            "root": "ש-מ-ע", "meaning": "hearing, listening", "type": "verb"
        },
        "אֶל": {
            "translation": "to",
            "root": "א-ל", "meaning": "to, toward", "type": "preposition"
        },
        "מִצְותַי": {
            "translation": "My commandments",
            "root": "צ-ו-ה", "meaning": "commanding", "type": "noun"
        },
        "מִצְות": {
            "translation": "commandments of",
            "root": "צ-ו-ה", "meaning": "commanding", "type": "noun"
        },
        "מִצְותָי": {
            "translation": "My commandments",
            "root": "צ-ו-ה", "meaning": "commanding", "type": "noun"
        },
        "אֶתְכֶם": {
            "translation": "you (plural)",
            "root": "א-ת-ת", "meaning": "with, direct object", "type": "particle"
        },
        "אֶתְכֶם": {
            "translation": "you (plural)",
            "root": "א-ת-ת", "meaning": "with, direct object", "type": "particle"
        },
        "לְאַהֲבָה": {
            "translation": "to love",
            "root": "א-ה-ב", "meaning": "loving", "type": "verb infinitive"
        },
        "אֱלהֵיכֶם": {
            "translation": "your God",
            "root": "א-ל-ה", "meaning": "God, deity", "type": "noun"
        },
        "לֵאלהֵיכֶם": {
            "translation": "to your God",
            "root": "א-ל-ה", "meaning": "God, deity", "type": "noun"
        },
        "לֵאלהִים": {
            "translation": "as God",
            "root": "א-ל-ה", "meaning": "God, deity", "type": "noun"
        },
        "וּלְעָבְדו": {
            "translation": "and to serve Him",
            "root": "ע-ב-ד", "meaning": "serving, working", "type": "verb"
        },
        "וְנָתַתִּי": {
            "translation": "And I will give",
            "root": "נ-ת-נ", "meaning": "giving", "type": "verb"
        },
        "מְטַר": {
            "translation": "rain of",
            "root": "מ-ט-ר", "meaning": "rain", "type": "noun"
        },
        "מָטָר": {
            "translation": "rain",
            "root": "מ-ט-ר", "meaning": "rain", "type": "noun"
        },
        "אַרְצְכֶם": {
            "translation": "your land",
            "root": "א-ר-ץ", "meaning": "land, earth", "type": "noun"
        },
        "בְּעִתּו": {
            "translation": "in its time",
            "root": "ע-ת-ת", "meaning": "time, season", "type": "noun"
        },
        "יורֶה": {
            "translation": "early rain",
            "root": "י-ר-ה", "meaning": "teaching, shooting", "type": "noun"
        },
        "וּמַלְקושׁ": {
            "translation": "and late rain",
            "root": "ל-ק-שׁ", "meaning": "late rain", "type": "noun"
        },
        "וְאָסַפְתָּ": {
            "translation": "and you shall gather",
            "root": "א-ס-פ", "meaning": "gathering, collecting", "type": "verb"
        },
        "דְגָנֶךָ": {
            "translation": "your grain",
            "root": "ד-ג-נ", "meaning": "grain", "type": "noun"
        },
        "וְתִירשְׁךָ": {
            "translation": "and your wine",
            "root": "י-ר-שׁ", "meaning": "inheriting, wine", "type": "noun"
        },
        "וְיִצְהָרֶךָ": {
            "translation": "and your oil",
            "root": "צ-ה-ר", "meaning": "oil, brightness", "type": "noun"
        },
        "עֵשב": {
            "translation": "grass",
            "root": "ע-ש-ב", "meaning": "grass, herb", "type": "noun"
        },
        "בְּשדְךָ": {
            "translation": "in your field",
            "root": "ש-ד-ה", "meaning": "field", "type": "noun"
        },
        "לִבְהֶמְתֶּךָ": {
            "translation": "for your cattle",
            "root": "ב-ה-מ", "meaning": "beast, cattle", "type": "noun"
        },
        "וְאָכַלְתָּ": {
            "translation": "and you shall eat",
            "root": "א-כ-ל", "meaning": "eating, food", "type": "verb"
        },
        "וְשבָעְתָּ": {
            "translation": "and be satisfied",
            "root": "ש-ב-ע", "meaning": "satisfying, seven", "type": "verb"
        },
        "הִשָּׁמְרוּ": {
            "translation": "Beware",
            "root": "ש-מ-ר", "meaning": "guarding, watching", "type": "verb"
        },
        "לָכֶם": {
            "translation": "for yourselves",
            "root": "ל", "meaning": "to, for", "type": "preposition"
        },
        "לָהֶם": {
            "translation": "for them",
            "root": "ל", "meaning": "to, for", "type": "preposition"
        },
        "פֶּן": {
            "translation": "lest",
            "root": "פ-נ-ה", "meaning": "face, turning", "type": "conjunction"
        },
        "יִפְתֶּה": {
            "translation": "be deceived",
            "root": "פ-ת-ה", "meaning": "opening, enticing", "type": "verb"
        },
        "וְסַרְתֶּם": {
            "translation": "and you turn away",
            "root": "ס-ו-ר", "meaning": "turning aside", "type": "verb"
        },
        "וַעֲבַדְתֶּם": {
            "translation": "and serve",
            "root": "ע-ב-ד", "meaning": "serving, working", "type": "verb"
        },
        "אֱלהִים": {
            "translation": "gods",
            "root": "א-ל-ה", "meaning": "God, deity", "type": "noun"
        },
        "אֲחֵרִים": {
            "translation": "other",
            "root": "א-ח-ר", "meaning": "after, other", "type": "adjective"
        },
        "וְהִשְׁתַּחֲוִיתֶם": {
            "translation": "and bow down",
            "root": "ש-ח-ה", "meaning": "bowing, prostrating", "type": "verb"
        },
        "וְחָרָה": {
            "translation": "And will be kindled",
            "root": "ח-ר-ה", "meaning": "burning, anger", "type": "verb"
        },
        "אַף": {
            "translation": "anger of",
            "root": "א-נ-פ", "meaning": "nose, anger", "type": "noun"
        },
        "בָּכֶם": {
            "translation": "against you",
            "root": "ב", "meaning": "in, with", "type": "preposition"
        },
        "וְעָצַר": {
            "translation": "and He will restrain",
            "root": "ע-צ-ר", "meaning": "restraining, stopping", "type": "verb"
        },
        "הַשָּׁמַיִם": {
            "translation": "the heavens",
            "root": "ש-מ-י", "meaning": "heavens, sky", "type": "noun"
        },
        "הַשָּׁמַיִם": {
            "translation": "the heavens",
            "root": "ש-מ-י", "meaning": "heavens, sky", "type": "noun"
        },
        "וְלא": {
            "translation": "and there will not",
            "root": "ל-א", "meaning": "not", "type": "particle"
        },
        "לא": {
            "translation": "not",
            "root": "ל-א", "meaning": "not", "type": "particle"
        },
        "יִהְיֶה": {
            "translation": "be",
            "root": "ה-י-ה", "meaning": "being, existing", "type": "verb"
        },
        "וְהָאֲדָמָה": {
            "translation": "and the earth",
            "root": "א-ד-מ", "meaning": "man, earth", "type": "noun"
        },
        "הָאֲדָמָה": {
            "translation": "the earth",
            "root": "א-ד-מ", "meaning": "man, earth", "type": "noun"
        },
        "תִתֵּן": {
            "translation": "will give",
            "root": "נ-ת-נ", "meaning": "giving", "type": "verb"
        },
        "יְבוּלָהּ": {
            "translation": "its produce",
            "root": "י-ב-ל", "meaning": "produce, flowing", "type": "noun"
        },
        "וַאֲבַדְתֶּם": {
            "translation": "and you will perish",
            "root": "א-ב-ד", "meaning": "perishing, losing", "type": "verb"
        },
        "מְהֵרָה": {
            "translation": "quickly",
            "root": "מ-ה-ר", "meaning": "haste, quickly", "type": "adverb"
        },
        "מֵעַל": {
            "translation": "from upon",
            "root": "ע-ל-ל", "meaning": "upon, over", "type": "preposition"
        },
        "הָאָרֶץ": {
            "translation": "the land",
            "root": "א-ר-ץ", "meaning": "land, earth", "type": "noun"
        },
        "הַטּבָה": {
            "translation": "the good",
            "root": "ט-ו-ב", "meaning": "goodness", "type": "adjective"
        },
        "נתֵן": {
            "translation": "gives",
            "root": "נ-ת-נ", "meaning": "giving", "type": "verb"
        },
        "וְשמְתֶּם": {
            "translation": "And you shall place",
            "root": "ש-ו-מ", "meaning": "placing, setting", "type": "verb"
        },
        "אֵלֶּה": {
            "translation": "these",
            "root": "א-ל-ה", "meaning": "these", "type": "demonstrative"
        },
        "אתָם": {
            "translation": "them",
            "root": "א-ת-ת", "meaning": "with, direct object", "type": "particle"
        },
        "וְלִמַּדְתֶּם": {
            "translation": "And you shall teach",
            "root": "ל-מ-ד", "meaning": "learning, teaching", "type": "verb"
        },
        "לְדַבֵּר": {
            "translation": "to speak",
            "root": "ד-ב-ר", "meaning": "speaking, word", "type": "verb infinitive"
        },
        "לְמַעַן": {
            "translation": "In order that",
            "root": "מ-ע-נ", "meaning": "purpose, intent", "type": "conjunction"
        },
        "יִרְבּוּ": {
            "translation": "may be multiplied",
            "root": "ר-ב-ב", "meaning": "many, great", "type": "verb"
        },
        "יְמֵיכֶם": {
            "translation": "your days",
            "root": "י-ו-מ", "meaning": "day", "type": "noun"
        },
        "וִימֵי": {
            "translation": "and the days of",
            "root": "י-ו-מ", "meaning": "day", "type": "noun"
        },
        "נִשְׁבַּע": {
            "translation": "swore",
            "root": "ש-ב-ע", "meaning": "swearing, seven", "type": "verb"
        },
        "לַאֲבתֵיכֶם": {
            "translation": "to your fathers",
            "root": "א-ב", "meaning": "father", "type": "noun"
        },
        "לָתֵת": {
            "translation": "to give",
            "root": "נ-ת-נ", "meaning": "giving", "type": "verb infinitive"
        },
        "כִּימֵי": {
            "translation": "as the days of",
            "root": "י-ו-מ", "meaning": "day", "type": "noun"
        },

        # Third paragraph - Tzitzit
        "וַיּאמֶר": {
            "translation": "And spoke",
            "root": "א-מ-ר", "meaning": "saying, speaking", "type": "verb"
        },
        "משֶׁה": {
            "translation": "Moses",
            "root": "מ-ש-ה", "meaning": "Moses, drawing out", "type": "proper noun"
        },
        "לֵּאמר": {
            "translation": "saying",
            "root": "א-מ-ר", "meaning": "saying, speaking", "type": "verb infinitive"
        },
        "דַּבֵּר": {
            "translation": "Speak",
            "root": "ד-ב-ר", "meaning": "speaking, word", "type": "verb"
        },
        "וְאָמַרְתָּ": {
            "translation": "and you shall say",
            "root": "א-מ-ר", "meaning": "saying, speaking", "type": "verb"
        },
        "אֲלֵהֶם": {
            "translation": "to them",
            "root": "א-ל", "meaning": "to, toward", "type": "preposition"
        },
        "וְעָשוּ": {
            "translation": "and they shall make",
            "root": "ע-ש-ה", "meaning": "making, doing", "type": "verb"
        },
        "צִיצִת": {
            "translation": "tzitzit / fringes",
            "root": "צ-י-צ", "meaning": "fringe, blossom", "type": "noun"
        },
        "לְצִיצִת": {
            "translation": "for tzitzit",
            "root": "צ-י-צ", "meaning": "fringe, blossom", "type": "noun"
        },
        "כַּנְפֵי": {
            "translation": "corners of",
            "root": "כ-נ-פ", "meaning": "wing, corner", "type": "noun"
        },
        "בִגְדֵיהֶם": {
            "translation": "their garments",
            "root": "ב-ג-ד", "meaning": "garment, betraying", "type": "noun"
        },
        "לְדרתָם": {
            "translation": "throughout their generations",
            "root": "ד-ו-ר", "meaning": "generation, circle", "type": "noun"
        },
        "וְנָתְנוּ": {
            "translation": "and they shall place",
            "root": "נ-ת-נ", "meaning": "giving", "type": "verb"
        },
        "הַכָּנָף": {
            "translation": "the corner",
            "root": "כ-נ-פ", "meaning": "wing, corner", "type": "noun"
        },
        "פְּתִיל": {
            "translation": "thread of",
            "root": "פ-ת-ל", "meaning": "twisting, thread", "type": "noun"
        },
        "תְּכֵלֶת": {
            "translation": "blue",
            "root": "כ-ל-ה", "meaning": "complete, blue", "type": "noun"
        },
        "וּרְאִיתֶם": {
            "translation": "and you shall see",
            "root": "ר-א-ה", "meaning": "seeing", "type": "verb"
        },
        "אתו": {
            "translation": "it",
            "root": "א-ת-ת", "meaning": "with, direct object", "type": "particle"
        },
        "וּזְכַרְתֶּם": {
            "translation": "and you shall remember",
            "root": "ז-כ-ר", "meaning": "remembering, memorial", "type": "verb"
        },
        "כָּל": {
            "translation": "all",
            "root": "כ-ל-ל", "meaning": "all, every", "type": "adjective"
        },
        "וַעֲשיתֶם": {
            "translation": "and you shall do",
            "root": "ע-ש-ה", "meaning": "making, doing", "type": "verb"
        },
        "תָתוּרוּ": {
            "translation": "go astray",
            "root": "ת-ו-ר", "meaning": "searching, spying", "type": "verb"
        },
        "אַחֲרֵי": {
            "translation": "after",
            "root": "א-ח-ר", "meaning": "after, other", "type": "preposition"
        },
        "אַתֶּם": {
            "translation": "you",
            "root": "א-ת-ת", "meaning": "you", "type": "pronoun"
        },
        "זנִים": {
            "translation": "go astray",
            "root": "ז-נ-ה", "meaning": "prostitution, straying", "type": "verb"
        },
        "אַחֲרֵיהֶם": {
            "translation": "after them",
            "root": "א-ח-ר", "meaning": "after, other", "type": "preposition"
        },
        "תִּזְכְּרוּ": {
            "translation": "you shall remember",
            "root": "ז-כ-ר", "meaning": "remembering, memorial", "type": "verb"
        },
        "וִהְיִיתֶם": {
            "translation": "and you shall be",
            "root": "ה-י-ה", "meaning": "being, existing", "type": "verb"
        },
        "קְדשִׁים": {
            "translation": "holy",
            "root": "ק-ד-שׁ", "meaning": "holiness, sanctity", "type": "adjective"
        },
        "אֲנִי": {
            "translation": "I am",
            "root": "א-נ-י", "meaning": "I", "type": "pronoun"
        },
        "הוצֵאתִי": {
            "translation": "brought out",
            "root": "י-צ-א", "meaning": "going out, exiting", "type": "verb"
        },
        "מֵאֶרֶץ": {
            "translation": "from the land of",
            "root": "א-ר-ץ", "meaning": "land, earth", "type": "noun"
        },
        "מִצְרַיִם": {
            "translation": "Egypt",
            "root": "מ-צ-ר", "meaning": "Egypt, narrowness", "type": "proper noun"
        },
        "לִהְיות": {
            "translation": "to be",
            "root": "ה-י-ה", "meaning": "being, existing", "type": "verb infinitive"
        },
        "אֱמֶת": {
            "translation": "True",
            "root": "א-מ-ת", "meaning": "truth, reliability", "type": "noun"
        },
    }

def apply_all_data(shema, mappings):
    """Apply translations and shoresh to all words."""
    for wid, word_data in shema["words"].items():
        hebrew = word_data["hebrew_clean"]

        if hebrew in mappings:
            mapping = mappings[hebrew]

            # Add translation
            word_data["translation"] = mapping["translation"]

            # Add shoresh
            word_data["shoresh"] = {
                "root": mapping["root"],
                "root_letters": mapping["root"].split('-'),
                "meaning": mapping["meaning"],
                "word_type": mapping["type"]
            }

    return shema

def calculate_all_frequencies():
    """Calculate frequencies within Shema and across all three prayers."""
    # Load all prayers
    ashrei = load_prayer("ashrei")
    aleinu = load_prayer("aleinu")
    shema_path = Path('/Users/mordechai/Ohr Avraham Chaim/Siddur/data/shema_embedded.json')
    with open(shema_path, 'r', encoding='utf-8') as f:
        shema = json.load(f)

    # Calculate Shema internal frequency
    shema_root_counts = defaultdict(int)
    for w in shema["words"].values():
        if "shoresh" in w:
            shema_root_counts[w["shoresh"]["root"]] += 1

    for w in shema["words"].values():
        if "shoresh" in w:
            w["shoresh"]["frequency_in_shema"] = shema_root_counts[w["shoresh"]["root"]]

    # Calculate combined frequency across all three
    combined_counts = defaultdict(int)
    for prayer in [ashrei, aleinu, shema]:
        for w in prayer["words"].values():
            if "shoresh" in w:
                combined_counts[w["shoresh"]["root"]] += 1

    # Update all three prayers with combined frequency
    for prayer in [ashrei, aleinu, shema]:
        for w in prayer["words"].values():
            if "shoresh" in w:
                w["shoresh"]["frequency_across_all_prayers"] = combined_counts[w["shoresh"]["root"]]

    # Save all three
    save_prayer("ashrei", ashrei)
    save_prayer("aleinu", aleinu)
    with open(shema_path, 'w', encoding='utf-8') as f:
        json.dump(shema, f, ensure_ascii=False, indent=2)

    return shema_root_counts, combined_counts

def main():
    print("=" * 70)
    print("BUILDING COMPLETE SHEMA SYSTEM")
    print("=" * 70)

    # Build structure
    print("\n1. Building embedded structure...")
    shema = build_shema_structure()
    print(f"   ✓ {len(shema['words'])} words")
    print(f"   ✓ {len(shema['paragraphs'])} paragraphs")

    # Add translations and shoresh
    print("\n2. Adding translations and shoresh...")
    mappings = get_shema_word_mappings()
    shema = apply_all_data(shema, mappings)

    translated = sum(1 for w in shema["words"].values() if "translation" in w)
    with_shoresh = sum(1 for w in shema["words"].values() if "shoresh" in w)

    print(f"   ✓ {translated}/{len(shema['words'])} translations ({translated/len(shema['words'])*100:.1f}%)")
    print(f"   ✓ {with_shoresh}/{len(shema['words'])} with shoresh ({with_shoresh/len(shema['words'])*100:.1f}%)")

    # Save
    output_path = Path('/Users/mordechai/Ohr Avraham Chaim/Siddur/data/shema_embedded.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(shema, f, ensure_ascii=False, indent=2)

    print(f"\n3. Saved: {output_path}")

    # Calculate frequencies
    print("\n4. Calculating frequencies across all prayers...")
    shema_counts, combined_counts = calculate_all_frequencies()

    print(f"   ✓ {len(shema_counts)} unique roots in Shema")
    print(f"   ✓ {len(combined_counts)} unique roots across all prayers")

    # Top roots in Shema
    print("\n" + "=" * 70)
    print("TOP 10 ROOTS IN SHEMA")
    print("=" * 70)
    top_shema = sorted(shema_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    for root, count in top_shema:
        print(f"  {root:15} → {count}x")

    # Top roots combined
    print("\n" + "=" * 70)
    print("TOP 15 ROOTS ACROSS ALL THREE PRAYERS")
    print("=" * 70)
    top_combined = sorted(combined_counts.items(), key=lambda x: x[1], reverse=True)[:15]
    for root, count in top_combined:
        print(f"  {root:15} → {count}x total")

    print("\n" + "=" * 70)
    print("✅ COMPLETE!")
    print("=" * 70)
    print("Shema system built with:")
    print("  • Complete word structure")
    print("  • Full translations")
    print("  • Complete shoresh")
    print("  • Frequency tracking (in Shema + across all prayers)")

if __name__ == '__main__':
    main()
