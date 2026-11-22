from um import count
import pytest

def test_wordboundary():
    assert count("um hello mr umbrella") == 1
    assert count("Eating a bum with an umami flavour underneath an Umbrella is umbearable") == 0
    assert count("um?") == 1


def test_regular(): # test if it works as exptected
    assert count("um") == 1
    assert count("um um um um um um") == 6

def test_case_insensitive():
    assert count("UM, Um, um, uM") == 4

