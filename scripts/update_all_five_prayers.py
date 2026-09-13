#!/usr/bin/env python3
"""Update frequency_across_all_prayers for all 5 prayers."""

import json
from collections import defaultdict

PRAYERS = [
    ('ashrei', 'frequency_in_ashrei'),
    ('aleinu', 'frequency_in_aleinu'),
    ('shema', 'frequency_in_shema'),
    ('netilat_yadayim', 'frequency_in_netilat_yadayim'),
    ('asher_yatzar', 'frequency_in_asher_yatzar'),
]

def load_prayer(name):
    with open(f'data/{name}_embedded.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def save_prayer(name, data):
    with open(f'data/{name}_embedded.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def main():
    print("Loading all 5 prayers...")
    prayers_data = {}
    for name, _ in PRAYERS:
        prayers_data[name] = load_prayer(name)
        word_count = len(prayers_data[name]["words"])
        print(f"   {name}: {word_count} words")

    # Count roots across all prayers
    print("\nCounting roots across all prayers...")
    global_root_counts = defaultdict(int)

    for prayer_data in prayers_data.values():
        for word in prayer_data["words"].values():
            if "shoresh" in word and "root" in word["shoresh"]:
                global_root_counts[word["shoresh"]["root"]] += 1

    total_unique_roots = len(global_root_counts)
    total_words = sum(len(p["words"]) for p in prayers_data.values())

    print(f"\nCross-prayer statistics:")
    print(f"   Total words: {total_words}")
    print(f"   Unique roots: {total_unique_roots}")

    # Update each prayer with global frequency
    for name, freq_field in PRAYERS:
        print(f"\nUpdating {name} with cross-prayer frequencies...")
        for word in prayers_data[name]["words"].values():
            if "shoresh" in word and "root" in word["shoresh"]:
                root = word["shoresh"]["root"]
                word["shoresh"]["frequency_across_all_prayers"] = global_root_counts[root]

    # Show top 15 roots
    print("\n" + "="*60)
    print("Top 15 roots across all 5 prayers:")
    print("="*60)
    top_roots = sorted(global_root_counts.items(), key=lambda x: x[1], reverse=True)[:15]
    for i, (root, count) in enumerate(top_roots, 1):
        # Show distribution across prayers
        distribution = []
        for name, _ in PRAYERS:
            prayer_count = sum(1 for w in prayers_data[name]["words"].values()
                             if "shoresh" in w and w["shoresh"]["root"] == root)
            if prayer_count > 0:
                distribution.append(f"{name[0].upper()}:{prayer_count}")

        dist_str = " | ".join(distribution)
        print(f"   {i:2d}. {root:8s} → {count:3d}x  [{dist_str}]")

    # Show blessing formula roots (common to Netilat Yadayim and Asher Yatzar)
    print("\n" + "="*60)
    print("Blessing Formula Analysis:")
    print("="*60)
    blessing_roots = []
    for word in prayers_data['netilat_yadayim']["words"].values():
        if "shoresh" in word:
            blessing_roots.append(word["shoresh"]["root"])

    print(f"Standard blessing opening contains {len(set(blessing_roots[:7]))} unique roots:")
    for root in list(dict.fromkeys(blessing_roots[:7])):  # First 7 words
        total = global_root_counts[root]
        print(f"   {root}: {total}x across all prayers")

    # Save all prayers
    print("\n" + "="*60)
    print("Saving updated prayers...")
    for name, _ in PRAYERS:
        save_prayer(name, prayers_data[name])
        print(f"   ✓ {name}")

    print("\n✅ All 5 prayers updated with cross-prayer frequencies!")
    print("="*60)

if __name__ == "__main__":
    main()
