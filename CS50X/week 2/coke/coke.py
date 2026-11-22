# Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

# In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due.
# Once the user has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.

# amount due out of the loop
amount_due = 50

# keep asking for money as long as there's an amount due
while amount_due > 0:

    coins = int(input("Insert coin: "))

# match function as learned in week 1.
    match coins:
        case  25 | 10 | 5:
            amount_due -= coins
            # only show anmount due if > 0 because if  <= 0 we'll print "change" outside the loop.
            if amount_due > 0:
                print(f"Amount due: {amount_due}")
        # case _: is the same as else
        case _:
            print(f"Amount due: {amount_due}")


# Change = equal to the amount overpaid. Abs make a number absolute . EG coins : 25 10 25 , amount_due = -10 > change = +10
change = abs(amount_due)
print(f"Change owed: {change}")


