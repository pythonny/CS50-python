# Suppose that you’re in the habit of making a list of items you need from the grocery store.

# In a file called grocery.py, implement a program that prompts the user for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program).
# Then output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item. No need to pluralize the items. Treat the user’s input case-insensitively.

# Create an empty grocery list to add upon

# make a grocery dictionary instead of a list. Because with a dictionary we can give values. eg. if input == milk, milk > 2 MILK with dictionary instead of MILK MILK with list
grocery_dictionary = {}

# create a loop because we want to keep adding to the list untill the user presses CTRL + D
while True:
    try:
        item = input()
        # grocery_dictionary.get(item, 0) does two things:
        # 1. Looks up 'item' in the dictionary
        # 2. Returns 0 if item doesn't exist, or returns current count if it does
        # Then we add 1 to whatever get() returned
        # Example:
        # First time "banana": 0 + 1 = 1
        # Second time "banana": 1 + 1 = 2
        grocery_dictionary[item] = grocery_dictionary.get(item, 0) + 1

    # EOFError == CTRL D > end of file error
    except EOFError:
        # sorted will sort the keys alphabatically.
        # {grocery_dictionary[food]} will give the number of that food in the dictionary, so we rewrite that word with .upper() because thats demanded by the problem
        for food in sorted(grocery_dictionary):
            print(f"{grocery_dictionary[food]} {food.upper()}")
        # stops the program
        break
