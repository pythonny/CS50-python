# It’s not uncommon, in English, at least, to say “um” when trying to, um, think of a word. The more you do it, though, the more noticeable it tends to be!

# In a file called um.py, implement a function called count that expects a line of text as input as a str and returns, as an int, the number of times that “um” appears in that text, case-insensitively,
#  as a word unto itself, not as a substring of some other word. For instance, given text like hello, um, world, the function should return 1. Given text like yummy, though, the function should return 0.

# Structure um.py as follows, wherein you’re welcome to modify main and/or implement other functions as you see fit, but you may not import any other libraries. You’re welcome, but not required, to use re and/or sys.

# Either before or after you implement count in um.py, additionally implement, in a file called test_um.py, three or more functions that collectively test your implementation of count thoroughly,
# each of whose names should begin with test_ so that you can execute your tests with:






import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    # re.findall searches for all matches in a string, and places this in a list
    #\b is word boundary > a-z, A-Z, 0-9 or _
    # if one of the word boundary's above is in place of \b it won't count.
    # For example: _um. > doesn't count because "_" is a word boundary
    # ?um? > counts because "?" isn't a word boundary
    # yummy > doesnt count because "y" and "m" are a word boundary
    match = re.findall(r"\bum\b",s, re.IGNORECASE)
    return len(match)





if __name__ == "__main__":
    main()
