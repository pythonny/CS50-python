
# This will try a risky code, because the user needs to enter an integer; increased chance of wrong input.
try:
    x = int(input("What is x? "))

# If ValueError, in this case x != integer
except ValueError:
    print("x is not an interger")

# if ValueError not the case
else:
    print(f"x is {x}")


# Same as before, but now it will loop untill the user enters a correct input
while True:

    try:
        x = int(input("What is x? "))

    except ValueError:
        print("x is not an interger")


    else:
        break

print(f"x is {x}")


# Same, but you immedately return x if True ( if you've a main function)

def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:

        try:
            return int(input("What is x? "))

    # pass just skips, and then you go back to try,
        except ValueError:
            pass

