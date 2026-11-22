import pytest
from datetime import date
from seasons import date_conversion
from seasons import number_to_words

def test_date():
    assert date_conversion("2020-11-01") == date (2020, 11, 1)

def test_date_format():
    with pytest.raises(SystemExit):
        date_conversion("29-03-1995")


# number to words
def test_number_to_words():
    assert number_to_words(100000) == "one hundred thousand"
