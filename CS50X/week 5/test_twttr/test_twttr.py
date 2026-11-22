# Testing my twttr
# In a file called twttr.py, reimplement Setting up my twttr from Problem Set 2, restructuring your code per the below, wherein shorten expects a str as input and returns that same str but with all vowels (A, E, I, O, and U) omitted,
# whether inputted in uppercase or lowercase.

# def main():
#     ...


# def shorten(word):
#     ...


# if __name__ == "__main__":
#     main()
# Then, in a file called test_twttr.py, implement one or more functions that collectively test your implementation of shorten thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

# pytest test_twttr.py

# import the shorten function from the file, because the shorten decides the ouput in this case.
from twttr import shorten

# Assert keyword tests whether a certain input results in a certain output
def test_letters():
    assert shorten("twitter") == "twttr"
    assert shorten ("harvard") == "hrvrd"

def test_numbers():
    assert shorten ("123") == "123"
    assert shorten ("onetwo3") == "ntw3"

def test_capitals():
    assert shorten("TWITTER") == "TWTTR"

def test_punctuation():
    assert shorten("@twitter!") == "@twttr!"
