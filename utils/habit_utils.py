import json
import os

DATA_FILE = "data/habits.json"


def load_habits():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []


def save_habits(habits):
    with open(DATA_FILE, "w") as f:
        json.dump(habits, f, indent=4)