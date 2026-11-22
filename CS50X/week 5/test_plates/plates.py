def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    if len(plate) >= 2 and len(plate) <= 6:
        if characters(plate):
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


if __name__ ==  "__main__":
    main()
