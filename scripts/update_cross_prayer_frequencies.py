#!/usr/bin/env python3
"""Update frequency_across_all_prayers for Ashrei, Aleinu, and Shema."""

import json
from collections import defaultdict

def load_prayer(name):
    with open(f'data/{name}_embedded.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def save_prayer(name, data):
    with open(f'data/{name}_embedded.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def main():
    print("Loading all three prayers...")
    ashrei = load_prayer('ashrei')
    aleinu = load_prayer('aleinu')
    shema = load_prayer('shema')

    # Count roots across all prayers
    print("Counting roots across all prayers...")
    global_root_counts = defaultdict(int)

    for prayer_data in [ashrei, aleinu, shema]:
        for word in prayer_data["words"].values():
            if "shoresh" in word and "root" in word["shoresh"]:
                global_root_counts[word["shoresh"]["root"]] += 1

    total_unique_roots = len(global_root_counts)
    total_words = sum(len(p["words"]) for p in [ashrei, aleinu, shema])

    print(f"\nCross-prayer statistics:")
    print(f"   Total words: {total_words}")
    print(f"   Unique roots: {total_unique_roots}")

    # Update each prayer with global frequency
    print("\nUpdating Ashrei with cross-prayer frequencies...")
    for word in ashrei["words"].values():
        if "shoresh" in word and "root" in word["shoresh"]:
            root = word["shoresh"]["root"]
            word["shoresh"]["frequency_across_all_prayers"] = global_root_counts[root]

    print("Updating Aleinu with cross-prayer frequencies...")
    for word in aleinu["words"].values():
        if "shoresh" in word and "root" in word["shoresh"]:
            root = word["shoresh"]["root"]
            word["shoresh"]["frequency_across_all_prayers"] = global_root_counts[root]

    print("Updating Shema with cross-prayer frequencies...")
    for word in shema["words"].values():
        if "shoresh" in word and "root" in word["shoresh"]:
            root = word["shoresh"]["root"]
            word["shoresh"]["frequency_across_all_prayers"] = global_root_counts[root]

    # Show top 10 roots
    print("\nTop 10 roots across all prayers:")
    top_roots = sorted(global_root_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    for i, (root, count) in enumerate(top_roots, 1):
        print(f"   {i}. {root}: {count}x")

    # Save all prayers
    print("\nSaving updated prayers...")
    save_prayer('ashrei', ashrei)
    save_prayer('aleinu', aleinu)
    save_prayer('shema', shema)

    print("\n✅ All prayers updated with cross-prayer frequencies!")

if __name__ == "__main__":
    main()
