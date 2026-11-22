from pantry import Pantry
from project import show_items, empty_the_pantry, auto_expire_pantry
import json

# os is a built-in python module for interacting with the operating system ( files, folders , file paths etc)
# It's needed for this test because everytime we need to delete the test_file from the file path
import os

def test_save_and_load():
    """ Test if code can make a new file .json file, and save new data to that .json file"""

    # make a new test file so we don't overwrite pantry.json
    test_file = "test_pantry.json"

    # if the test fille already exists, we'll delete it. otherwise we can't test.
    # for example we add milk in the test, but if milk was already in the file
    # the test will still pass, not because adding milk worked, but because it was already there.
    if os.path.exists(test_file):
        os.remove(test_file)

    # We make the same pantry object, but use a different file
    p = Pantry(test_file)

    # manually add milk in the items
    p.items = {
        "Milk": [
            {"expiry": "2100-01-01", "quantity": 2}
        ]
    }
    # using the save function to this if it works
    p.save_items()

    # The save function will save p.items in the test file
    # Now we need to open it and save the content in a variable (data)
    with open(test_file) as f:
        data = json.load(f)

    # check if all data is correct
    assert "Milk" in data
    assert data["Milk"][0]["expiry"] == "2100-01-01"
    assert data["Milk"][0]["quantity"] == 2

def test_auto_expire():

    test_file = "test_auto_expire.json"

    if os.path.exists(test_file):
        os.remove(test_file)

    p = Pantry(test_file)

    # Cheese is expired, ham in future
    p.items ={
        "Cheese": [
            {"expiry": "2000-01-01", "quantity": 10}
        ],
        "Ham": [
            {"expiry": "3000-01-01", "quantity": 10}
        ]
    }

    p.save_items()
    p.auto_expire()

    with open(test_file) as f:
        data = json.load(f)

    # cheese should expire since expiry date == year 2000
    # Ham should not expire because expiry date == year 3000
    assert "Cheese" not in data
    assert "Ham" in data

def test_show_pantry_returns_none():
    """ Test if show_items runs and returns none if the file is empty"""
    test_file = "test_show.json"
    p = Pantry(test_file)
    result = show_items(p)
    assert result is None

def test_empty_the_pantry(monkeypatch):
    """ Tests if emptying the pantry works"""
    test_file = "test_empty.json"
    p = Pantry(test_file)
    p.items = ["milk"]

    # automatically set default input to "yes", since empty pantry asks for a confirmation
    monkeypatch.setattr('builtins.input', lambda _: 'yes')
    empty_the_pantry(p)
    assert p.items == {}
