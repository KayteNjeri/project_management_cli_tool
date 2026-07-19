import json
import os

FILE = "data/database.json"

# Loads project data from the JSON file
def load_data(filename=FILE):
    if not os.path.exists(filename):
        return {"users": []}

    try:
        with open(filename, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return {"users": []}

# Saves application data to the JSON file
def save_data(data, filename=FILE):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)