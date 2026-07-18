import os

from utils.storage import save_data, load_data


TEST_FILE = "tests/test_database.json"


def test_save_and_load():

    sample = {
        "users": [
            {
                "name": "Alex",
                "email": "alex@gmail.com"
            }
        ]
    }

    save_data(sample, TEST_FILE)

    loaded = load_data(TEST_FILE)

    assert loaded == sample

    os.remove(TEST_FILE)


def test_missing_file():

    loaded = load_data("does_not_exist.json")

    assert loaded == {"users": []}