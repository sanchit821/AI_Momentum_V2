import json
import os

DATA_FILE = "data/mood.json"


def load_moods():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []


def save_moods(moods):
    with open(DATA_FILE, "w") as f:
        json.dump(moods, f, indent=4)