# In Massachusetts, home to Harvard University, it’s possible to request a vanity license plate for your car, with your choice of letters and numbers instead of random ones. Among the requirements, though, are:

# “All vanity plates must start with at least two letters.”
# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
# “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
# “No periods, spaces, or punctuation marks are allowed.”
# In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not. Assume that any letters in the user’s input will be uppercase.
# Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not. Assume that s will be a str.
# You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement).

# Rule 1: Len(plate) between 2 and 6 x
# Rule 2: Numbers must be at the end of each word
# Rule 3: First number used cannot be 0 x
# Rule 4: " ", "." or punctuation marks allowed > only allow A-Z and 0-9 x
# Rule 5: All letters must be UPPERCASE. x

def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) >= 2 and len(s) <= 6:
        if characters(s):
            return True
    return False



def characters(license):
    # make list to compare it to the rules given.
    digits = ""
    letters = ""
    not_allowed_char = ""
    license_plate = ""

    # assign each letter in the license to digits character or not allowed char.
    for char in license:
        if char.isdigit():
            digits += char
            license_plate += char

        elif char.isalpha():
            letters += char
            license_plate += char

        else:
            not_allowed_char += char
            license_plate += char

    # only letters and numbers allowed, so if len should always be 0
    if len(not_allowed_char) > 0:
        return False

    # license cant start with 0, but license is allowed to have no digits. If license has no digits and I check digits[0] I get an error
    # Thus it's important to compare both digits and digits[0] to prevend this error

    # only if the license plate includes digits,else it compare an empty variable which can give an error
    if len(digits) > 0:

        # Digits cannot start with 0.
        if digits[0] == "0":
            return False

        # Digits can only be at the end, so the number of digits should always be the same as the number of digits at the end of the license
        # counting back from the license plate using len(digits)
        if license_plate[-len(digits):] != digits:
            return False

    # Minimum 2 characters (letters)
    if len(letters) < 2:
        return False


    else:
        return True


main()
