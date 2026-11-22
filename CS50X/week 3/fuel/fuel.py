# Fuel gauges indicate, often with fractions, just how much fuel is in a tank. For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank is 50% full, and 3/4 indicates that a tank is 75% full.

# In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank.
#  If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. And if 99% or more remains, output F instead to indicate that the tank is essentially full.

# If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.


# main function, at first I had the print function in the calculator but this resulted in a never ending loop.
def main():
    fraction = calculator("Fraction: ")
    print(fraction)




# prompt basically copies ("Fraction: ") from the main function
def calculator(prompt):
    # Can only use "continue" in a While loop. It was important to be able to use the function "continue", because the calculator had to restart if the user chose a wrong input.
    while True:
        try:
            fraction = input(prompt).split("/") # eg. 1/2 . we split anything before and after "/"
            x = int(fraction[0]) # the first number after the split == "x"
            y = int(fraction[1]) # the second number after the split == "y"

            if x > y: # if x > y the calculator will restart, because x can only be equal to y, never more in a fuel gauge.
                continue

            fuel_percentage = round((x / y ) * 100)

            if fuel_percentage <= 1:
                return "E"
            elif fuel_percentage >= 99:
                return "F"
            else:
                return(f"{fuel_percentage}%")

        # Value errors after try, otherwise the program can already restart before all the if functions are tried.
        except ValueError:
            continue

        except ZeroDivisionError:
            continue



if __name__ == "__main__":
    main()



# try:
#     ...
# except ValueError:
#     ...
# except ZeroDivisionError:
#     ...
