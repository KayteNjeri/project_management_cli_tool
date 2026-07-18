import json
import os

FILE = "data/database.json"

def load_data():
    if not os.path.exists(FILE):
        return {"users": []}

    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, FeleNotFoundError):
        return {"users": []}

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)