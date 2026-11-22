# Fuel gauges indicate, often with fractions, just how much fuel is in a tank. For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank is 50% full, and 3/4 indicates that a tank is 75% full.

# In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank.
#  If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. And if 99% or more remains, output F instead to indicate that the tank is essentially full.

# If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.


# main function, at first I had the print function in the calculator but this resulted in a never ending loop.
def main():

    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))


def convert(fraction):
    fraction = fraction.split("/")  # eg. 1/2 . we split anything before and after "/"
    x = int(fraction[0]) # the first number after the split == "x"
    y = int(fraction[1]) # the second number after the split == "y"

    if y == 0:
        raise ZeroDivisionError

    if x > y:
        raise ValueError

    if x < 0 or y < 0:
         raise ValueError

    return round((x / y ) * 100)


def gauge(percentage):

      if percentage <= 1:
            return "E"
      elif percentage >= 99:
            return "F"
      else:
            return(f"{percentage}%")


if __name__ == "__main__":
    main()

