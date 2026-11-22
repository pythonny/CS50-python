import pytest
from numb3rs import validate

def test_len():
    assert validate("3.3.3") == False
    assert validate("3.3.3.3.3") == False
    assert validate("3.3.3.3") == True
    assert validate(".3.3.3.3") == False
    assert validate("3.3.3.3.") == False

def test_digit():
    assert validate("a.a.a.a") == False
    assert validate("1.2.3.b") == False
    assert validate("100.100.100.100") == True


def test_range():
    assert validate("275.3.6.28") == False
    assert validate("-1.3.6.28") == False
    assert validate("0.255.1.1") == True
