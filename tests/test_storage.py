import os

from utils.storage import save_data, load_data

TEST_FILE = "test_database.json"

def test_save_and_load():

    sample = {
        "users": [
            {
                "name": "Alex",
                "email": "alex@gmail.com"
            }
        ]
    }

    save_data(sample)

    loaded = load_data()

    assert loaded["users"][0]["name"] == "Alex"


def test_load_empty():

    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)

    data = {
        "users": []
    }

    save_data(data)

    loaded = load_data()

    assert "users" in loaded