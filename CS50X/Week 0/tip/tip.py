# Well, we’ve written most of a tip calculator for you. Unfortunately, we didn’t have time to implement two functions:

# dollars_to_float, which should accept a str as input (formatted as $##.##, wherein each # is a decimal digit), remove the leading $, and return the amount as a float. For instance, given $50.00 as input, it should return 50.0.
# percent_to_float, which should accept a str as input (formatted as ##%, wherein each # is a decimal digit), remove the trailing %, and return the percentage as a float. For instance, given 15% as input, it should return 0.15.
# Assume that the user will input values in the expected formats.


def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? ")) # can't make into float, because then we can't replace "%" later
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    dollars =  d.replace("$", "") # remove "$". Can only replace a string
    dollars = float(dollars) # make into float only after removing "$"
    return dollars


def percent_to_float(p):
    p = p.replace("%", "") # remove "%" and replace into decimals e.h. 15% > 0.15 . Can only use replace() on string.
    p = float(p) / 100 # since we had to replace % firs, we can only convert to float after this step
    return p

main()
