# In Season 5, Episode 23 of NUMB3RS, a supposed IP address appears on screen, 275.3.6.28, which isn’t actually a valid IPv4 (or IPv6) address.

# An IPv4 address is a numeric identifier that a device (or, on TV, hacker) uses to communicate on the internet, akin to a postal address in the real world, typically formatted in dot-decimal notation
# as #.#.#.#. But each # should be a number between 0 and 255, inclusive. Suffice it to say 275 is not in that range! If only NUMB3RS had validated the address in that scene!

# In a file called numb3rs.py, implement a function called validate that expects an IPv4 address as input as a str and then returns True or False, respectively, if that input is a valid IPv4 address or not.

# Structure numb3rs.py as follows, wherein you’re welcome to modify main and/or implement other functions as you see fit, but you may not import any other libraries. You’re welcome, but not required, to use re and/or sys.

# Either before or after you implement validate in numb3rs.py, additionally implement, in a file called test_numb3rs.py, two or more functions that collectively test your implementation of validate thoroughly,
# each of whose names should begin with test_ so that you can execute your tests with:

# pytest test_numb3rs.py


import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # IP displayed as #.#.#.#. with each number being 0-255
    # we can use ip.split, because ip is a variable of validate(ip)
    parts = ip.split(".")

    # #.#.#.#. = len 4
    # this also checks whether the IP-adress starts with a number and ends with a "."
    # ip: 1.2.3.4. > ["1", "2", "3", "4", ""] > len 5 > false, but later also isdigit() fails
    # ip: ".1.2.3.4" > ["", "1", "2", "3", "4"] > len 5 > false, but later also isdigit() fails
    if len(parts) != 4:
        return False

    # each number should be a digit
    for number in parts:
        if not number.isdigit():
            return False
        # digit should be between 0 and 255
        if int(number) < 0 or int(number) > 255:
            return False

    else:
        return True


if __name__ == "__main__":
    main()
