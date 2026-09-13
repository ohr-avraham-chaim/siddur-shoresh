#!/usr/bin/env python3
"""Build Yehi Ratzon prayer (said after Birkot HaShachar)."""

import json
import re
from collections import defaultdict

def get_yehi_ratzon_mappings():
    """Complete mappings for Yehi Ratzon prayer."""
    return {
        # Opening
        "וִיהִי": {"trans": "May it be", "root": "ה-י-ה", "meaning": "be, exist", "type": "verb"},
        "רָצון": {"trans": "the will / favor", "root": "ר-צ-ה", "meaning": "will, desire, favor", "type": "noun"},
        "מִלְּפָנֶיךָ": {"trans": "before You", "root": "פ-נ-נ", "meaning": "face, before", "type": "preposition"},
        "ה'": {"trans": "Hashem", "root": "ה-ו-י", "meaning": "God's name (YHVH)", "type": "proper noun"},
        "אֱלהֵינוּ": {"trans": "our God", "root": "א-ל-ה", "meaning": "God, deity", "type": "noun"},
        "וֵאלהֵי": {"trans": "and God of", "root": "א-ל-ה", "meaning": "God, deity", "type": "noun"},
        "אֲבותֵינוּ": {"trans": "our fathers", "root": "א-ב-ב", "meaning": "father", "type": "noun"},

        # Requests
        "שֶׁתַּרְגִּילֵנוּ": {"trans": "that You accustom us", "root": "ר-ג-ל", "meaning": "foot, accustom", "type": "verb"},
        "בְּתורָתֶךָ.": {"trans": "in Your Torah", "root": "י-ר-ה", "meaning": "Torah, teach", "type": "noun"},
        "וְדַבְּקֵנוּ": {"trans": "and attach us", "root": "ד-ב-ק", "meaning": "cling, attach", "type": "verb"},
        "בְּמִצְותֶיךָ.": {"trans": "to Your commandments", "root": "צ-ו-ה", "meaning": "command", "type": "noun"},

        # Negative requests (what to avoid)
        "וְאַל": {"trans": "and do not", "root": "א-ל", "meaning": "not (negative)", "type": "negative"},
        "תְּבִיאֵנוּ": {"trans": "bring us", "root": "ב-ו-א", "meaning": "come, bring", "type": "verb"},
        "לא": {"trans": "not", "root": "ל-א", "meaning": "not", "type": "negative"},
        "לִידֵי": {"trans": "into the hands of / to", "root": "י-ד-ד", "meaning": "hand", "type": "noun"},
        "חֵטְא.": {"trans": "sin", "root": "ח-ט-א", "meaning": "sin, miss", "type": "noun"},
        "עֲבֵרָה": {"trans": "transgression", "root": "ע-ב-ר", "meaning": "pass over, transgress", "type": "noun"},
        "וְעָון.": {"trans": "and iniquity", "root": "ע-ו-נ", "meaning": "iniquity, guilt", "type": "noun"},
        "נִסָּיון.": {"trans": "temptation / test", "root": "נ-ס-ה", "meaning": "test, try", "type": "noun"},
        "בִזָּיון.": {"trans": "disgrace / shame", "root": "ב-ז-ה", "meaning": "despise, disgrace", "type": "noun"},

        # Evil inclination
        "תַּשְׁלֶט": {"trans": "have power / rule", "root": "ש-ל-ט", "meaning": "rule, have power", "type": "verb"},
        "בָּנוּ": {"trans": "over us", "root": "ב-ב-ב", "meaning": "in, over", "type": "preposition"},
        "יֵצֶר": {"trans": "inclination", "root": "י-צ-ר", "meaning": "form, inclination", "type": "noun"},
        "הָרָע.": {"trans": "the evil", "root": "ר-ע-ע", "meaning": "evil, bad", "type": "adjective"},

        # Distance from evil
        "וְהַרְחִיקֵנוּ": {"trans": "and distance us", "root": "ר-ח-ק", "meaning": "far, distance", "type": "verb"},
        "מֵאָדָם": {"trans": "from a person", "root": "א-ד-מ", "meaning": "human, man", "type": "noun"},
        "רָע": {"trans": "evil / bad", "root": "ר-ע-ע", "meaning": "evil, bad", "type": "adjective"},
        "וּמֵחָבֵר": {"trans": "and from a companion", "root": "ח-ב-ר", "meaning": "join, friend", "type": "noun"},

        # Good inclination and deeds
        "בְּיֵצֶר": {"trans": "to the inclination", "root": "י-צ-ר", "meaning": "form, inclination", "type": "noun"},
        "הַטוב": {"trans": "the good", "root": "ט-ו-ב", "meaning": "good", "type": "adjective"},
        "וּבְמַעֲשים": {"trans": "and to deeds", "root": "ע-ש-ה", "meaning": "do, make, deed", "type": "noun"},
        "טובִים.": {"trans": "good", "root": "ט-ו-ב", "meaning": "good", "type": "adjective"},

        # Subdue inclination
        "וְכף": {"trans": "and subdue / compel", "root": "כ-פ-ה", "meaning": "subdue, compel", "type": "verb"},
        "אֶת": {"trans": "(direct object marker)", "root": "א-ת-ת", "meaning": "direct object marker", "type": "particle"},
        "יִצְרֵנוּ": {"trans": "our inclination", "root": "י-צ-ר", "meaning": "form, inclination", "type": "noun"},
        "לְהִשְׁתַּעְבֶּד": {"trans": "to be enslaved / subjugated", "root": "ע-ב-ד", "meaning": "serve, enslave", "type": "verb"},
        "לָךְ.": {"trans": "to You", "root": "ל", "meaning": "to, for", "type": "preposition"},

        # Daily favors
        "וּתְנֵנוּ": {"trans": "and grant us", "root": "נ-ת-נ", "meaning": "give", "type": "verb"},
        "הַיּום": {"trans": "today", "root": "י-ו-מ", "meaning": "day", "type": "noun"},
        "וּבְכָל": {"trans": "and every", "root": "כ-ל-ל", "meaning": "all, every", "type": "noun"},
        "יום": {"trans": "day", "root": "י-ו-מ", "meaning": "day", "type": "noun"},
        "לְחֵן": {"trans": "for favor / grace", "root": "ח-נ-נ", "meaning": "favor, grace", "type": "noun"},
        "וּלְחֶסֶד": {"trans": "and for kindness", "root": "ח-ס-ד", "meaning": "kindness, loyalty", "type": "noun"},
        "וּלְרַחֲמִים": {"trans": "and for mercy", "root": "ר-ח-מ", "meaning": "mercy, compassion", "type": "noun"},
        "בְּעֵינֶיךָ": {"trans": "in Your eyes", "root": "ע-י-נ", "meaning": "eye", "type": "noun"},
        "וּבְעֵינֵי": {"trans": "and in the eyes of", "root": "ע-י-נ", "meaning": "eye", "type": "noun"},
        "כָל": {"trans": "all", "root": "כ-ל-ל", "meaning": "all, every", "type": "noun"},
        "רואֵינוּ.": {"trans": "those who see us", "root": "ר-א-ה", "meaning": "see", "type": "verb"},

        # Acts of kindness
        "וְתִגְמְלֵנוּ": {"trans": "and bestow upon us", "root": "ג-מ-ל", "meaning": "give, bestow, repay", "type": "verb"},
        "חֲסָדִים": {"trans": "kindnesses", "root": "ח-ס-ד", "meaning": "kindness, loyalty", "type": "noun"},
        "טובִים.": {"trans": "good", "root": "ט-ו-ב", "meaning": "good", "type": "adjective"},

        # Closing blessing
        "בָּרוּךְ": {"trans": "Blessed", "root": "ב-ר-כ", "meaning": "blessing, knee", "type": "adjective"},
        "אַתָּה": {"trans": "You are", "root": "א-ת-ת", "meaning": "you (masculine singular)", "type": "pronoun"},
        "הַגּומֵל": {"trans": "Who bestows", "root": "ג-מ-ל", "meaning": "give, bestow", "type": "verb"},
        "לְעַמּו": {"trans": "to His nation", "root": "ע-מ-מ", "meaning": "nation, people", "type": "noun"},
        "יִשרָאֵל.": {"trans": "Israel", "root": "י-ש-ר", "meaning": "straight, Israel", "type": "proper noun"},
    }

def build_yehi_ratzon():
    """Build Yehi Ratzon prayer."""
    
    text = "וִיהִי רָצון מִלְּפָנֶיךָ ה' אֱלהֵינוּ וֵאלהֵי אֲבותֵינוּ שֶׁתַּרְגִּילֵנוּ בְּתורָתֶךָ. וְדַבְּקֵנוּ בְּמִצְותֶיךָ. וְאַל תְּבִיאֵנוּ לא לִידֵי חֵטְא. וְלא לִידֵי עֲבֵרָה וְעָון. וְלא לִידֵי נִסָּיון. וְלא לִידֵי בִזָּיון. וְאַל תַּשְׁלֶט בָּנוּ יֵצֶר הָרָע. וְהַרְחִיקֵנוּ מֵאָדָם רָע וּמֵחָבֵר רָע. וְדַבְּקֵנוּ בְּיֵצֶר הַטוב וּבְמַעֲשים טובִים. וְכף אֶת יִצְרֵנוּ לְהִשְׁתַּעְבֶּד לָךְ. וּתְנֵנוּ הַיּום וּבְכָל יום לְחֵן וּלְחֶסֶד וּלְרַחֲמִים בְּעֵינֶיךָ וּבְעֵינֵי כָל רואֵינוּ. וְתִגְמְלֵנוּ חֲסָדִים טובִים. בָּרוּךְ אַתָּה ה' הַגּומֵל חֲסָדִים טובִים לְעַמּו יִשרָאֵל."
    
    mappings = get_yehi_ratzon_mappings()
    
    # Parse words
    final_words = text.replace('.', '. ').split()
    
    # Initialize structure
    data = {
        "text_name": {
            "hebrew": "וִיהִי רָצון",
            "english": "Yehi Ratzon - May It Be Your Will"
        },
        "context": "Prayer said after Birkot HaShachar (Morning Blessings)",
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
        if '.' in punctuation:
            data["sentences"][f"s{sentence_num}"] = {
                "id": f"s{sentence_num}",
                "word_ids": sentence_word_ids,
                "hebrew": ' '.join(data["words"][wid]["hebrew"] for wid in sentence_word_ids)
            }
            sentence_num += 1
            sentence_word_ids = []
        
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
    print("Building Yehi Ratzon Prayer")
    print("="*60)
    
    prayer = build_yehi_ratzon()
    
    # Save
    filename = 'data/yehi_ratzon_embedded.json'
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(prayer, f, ensure_ascii=False, indent=2)
    
    # Stats
    total = len(prayer["words"])
    with_trans = sum(1 for w in prayer["words"].values() if "translation" in w)
    with_shoresh = sum(1 for w in prayer["words"].values() if "shoresh" in w)
    unique_roots = len(set(w["shoresh"]["root"] for w in prayer["words"].values() if "shoresh" in w))
    
    print(f"\n✅ Yehi Ratzon complete:")
    print(f"   Total words: {total}")
    print(f"   Translations: {with_trans}/{total} ({100*with_trans/total:.1f}%)")
    print(f"   With shoresh: {with_shoresh}/{total} ({100*with_shoresh/total:.1f}%)")
    print(f"   Unique roots: {unique_roots}")
    print(f"   Sentences: {len(prayer['sentences'])}")
    print("="*60)

if __name__ == "__main__":
    main()
