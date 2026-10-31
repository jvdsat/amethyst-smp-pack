import os
import json
import tomllib
import requests
import sys


def load_cache(cache_file):

    try:
        if os.path.exists(cache_file) and os.path.getsize(cache_file) > 0:
            with open(cache_file, "r", encoding="utf-8") as f:
                return json.load(f)

        else:
            return {}

    except Exception as e:
        sys.exit(f"Error reading cache file: {e}")


def save_cache(cache, cache_file):
    try:
        with open(cache_file, "w", encoding="utf-8") as f:
            json.dump(cache, f, indent=4)
    except Exception as e:
        sys.exit(f"Error saving cache file: {e}")


def get_modrinth_categories(mod_id):
    """Fetches categories for a mod from the Modrinth API."""
    url = f"https://api.modrinth.com/v2/project/{mod_id}"
    headers = {"User-Agent": "PackwizMarkdownSorter/1.0 (contact@example.com)"}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data.get("categories", [])
    except Exception as e:
        print(f"Error fetching data for {mod_id}: {e}")
    return ["uncategorized"]


def main():

    mods_dir = "packwiz/mods"
    modlist_file = "MODLIST.md"
    cache_file = "scripts/mod_cache.json"

    category_map = {
        "adventure": "Adventure & Content",
        "worldgen": "World Generation",
        "storage": "Storage & Inventory",
        "technology": "Technology",
        "magic": "Magic",
        "decoration": "Decoration",
        "equipment": "Equipment & Weapons",
        "food": "Food & Farming",
        "quality": "Quality of Life",
        "utility": "Utilities",
        "optimization": "Performance",
        "servermanagement": "Server Management",
        "library": "Libraries & APIs",
        "uncategorized": "Uncategorized",
    }

    cache = load_cache(cache_file)
    cache_updated = False

    categorized_mods = {name: [] for name in category_map.keys()}

    for filename in os.listdir(mods_dir):
        if filename.endswith(".toml"):
            file_path = os.path.join(mods_dir, filename)

            with open(file_path, "rb") as f:
                try:
                    data = tomllib.load(f)
                except Exception as e:
                    print(f"Failed to open {filename}: {e}")
                    continue

            mod_name = data.get("name", filename.replace(".toml", ""))

            # Create an update data variable for the mod ID
            update_data = data.get("update", {})

            # For modrinth mods
            mod_id = None
            if "modrinth" in update_data:
                mod_id = str(update_data["modrinth"].get("mod-id"))

            # For curseforge mods
            if "curseforge" in update_data:
                mod_id = str(data["update"]["curseforge"]["file-id"])

            categories = []

            if not mod_id:
                print(f"No mod id found for {mod_name}")
                continue

            # Check cache for mod, otherwise check modrinth
            if mod_id in cache:
                categories = cache.get(mod_id, {}).get("categories", [])
            else:
                print(f"Fetching categories from: {mod_name}")
                categories = get_modrinth_categories(mod_id)
                cache[str(mod_id)] = {"name": mod_name, "shortname": filename.replace(".pw.toml", ""), "categories": categories}
                cache_updated = True

            first_category = categories[0] if len(categories) > 0 else ["uncategorized"]

            if str(first_category) in categorized_mods:
                categorized_mods[first_category].append(mod_name)
            else:
                categorized_mods["uncategorized"].append(mod_name)

    with open(modlist_file, "w", encoding="utf-8") as md:
        md.write("# Amethyst Server Modlist \n\n")
        md.write(f"Total mods: {len(cache)} \n\n")

        for category, mods in categorized_mods.items():
            if mods:
                md.write(f"## {category_map.get(category)}\n\n")
                for mod in sorted(mods):
                    md.write(f"* {mod}\n")
                md.write("\n")

    # Save cache for new edits
    if cache_updated:
        save_cache(cache, cache_file)
        print(f"Updated {cache_file}")
    else:
        print(f"Updated {modlist_file}")


if __name__ == "__main__":
    main()
