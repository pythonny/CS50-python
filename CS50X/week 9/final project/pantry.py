from datetime import date
import json
from prettytable import PrettyTable
from prettytable.colortable import ColorTable, Themes
import sys


class Pantry:

    # __init__ runs automatically when we create a Pantry object.
    # Example: p = Pantry() > this triggers __init__.
    # 'self' refers to that exact object (so inside the class: self == p).
    # When we write self.x, we store x inside the object.
    # Because of that, self.filename and self.items stay available
    # in all other methods of the class (show_items, add_items, delete_item, etc.).
    def __init__(self, filename="pantry.json"):
        """__init__ runs automatically when a Pantry object is created."""
        # Save the filename in the object (default = "pantry.json")
        # Otherwise fiename=pantry.json won't be saved.
        self.filename = filename
        self.items = self.load_from_file()

    def load_from_file(self):
        """Opens the JSON file that stores all data of the Pantry. If the file does not exist yet a new file will be created."""
        try:
            # open file in read mode and load self.items (pantry stock)
            with open(self.filename, "r") as file:

                # Tests if there is already content in the file
                content = file.read().strip()

            # if no content we create a new, empty, item library
            if content == "":
                self.items = {}

                with open(self.filename, "w") as file:
                    # .dump writes the content of self.items to self.filename.json > json.dump(object,file pointer/place)
                    json.dump(self.items, file)

            else:
                #  We always need to match self.items with the content of pantry.json, so if we already had content in pantry.py
                # which is obtained from: content = file.read().strip() , we need self.items to match the data.
                # Self.items is the internal dictionary that this whole program uses, all changes will be written to self.items
                # later on we sync pantry.json with self.items to store the data.
                self.items = json.loads(content)

        except FileNotFoundError:
            # if json doesn't exist we create a library of self.items , which is empty at the moment and write this to a json file.
            self.items = {}

            with open(self.filename, "w") as file:
                json.dump(self.items, file)

        return self.items

    # give main_menu a default value before defining the function, so that we can change the value while calling the function.
    def show_items(self, main_menu=True):
        """Display all pantry items in colored a table format."""

        # makes sure items past expiry date won't be shown in the table
        self.auto_expire()

        if not self.items:
            pantry_empty()
            return_to_menu()
            return

        # Create table and fieldnames , use colortable theme to add colors in rows
        #https://pypi.org/project/prettytable/
        table = ColorTable()
        table.field_names = ["item", "Quantity", "Expiry Date", "Days left"]

        # product is the name of the item. self.items.keys() is all keys inside pantry.json
        # Reads as: (For each food or drink in pantry.json)
        # Each item can have multiple dictionaries > e.g. : Two milk, each with their own expiry date
        # loop through each dictionary per item and assign name to the value ( quantity, expiry, product)
        # We add a row for each batch inside this loop so all batches are included.
        # if add_row() were placed outside the loop only the last batch of each product would appear.
        # Because earlier batches would get overwritten before being added.

        for product in self.items.keys():
            for dictionary in self.items[product]:
                quantity = dictionary["quantity"]
                expiry = dictionary["expiry"]
                days_left = self.date_conversion(expiry)

                if days_left <= 1:
                    color = "\033[31m" # red

                elif 2 <= days_left <= 4: # yellow
                    color = "\033[1;33m"

                else:
                    color = "\033[32m" # green

                RESET = "\033[0m" # standard color

                # Wrap the number in color codes and reset afterwards.
                # Without RESET, the terminal keeps the color active and the rest of the table would appear colored.
                days_left_colored = f"{color}{days_left}{RESET}"
                table.add_row([product, quantity, expiry, days_left_colored])

        print(table)

        # Only if the user called for show_items through main menu
        # Otherwise we get this question inside other function as well, e.g. delete_items()
        if main_menu == True:
            # if we don't ask the user this, the program will automatically go back to the main menu, which affects the visibility. \
            # Optionally if user only wants to see his curreny pantry he can immediately close it after doing so.
            answer = input("Type 'yes' to return to the main menu or 'close' to close the program.\n").strip().lower()

            if answer.startswith("y"):
                return_to_menu()
                return

            if answer.startswith("close"):
                print("Goodbye!")
                sys.exit()

    def save_items(self):
        """Function that makes auto saving inside add_items() and auto_expire possible"""
        with open(self.filename, "w") as file:
            json.dump(self.items, file, indent=4)  # indent adds \n +4 spaces

    def add_items(self):
        """Add Items to the pantry and automatically saves them"""
        while True:
            name = input(
                "What item would you like to add to your pantry? ").capitalize().strip()

            while True:
                expiry = input(
                    "What is the expiry date of the item in (YYYY-MM-DD)? ").strip()

                try:
                    # is a built-in method in Python’s datetime module that converts a string formatted in ISO 8601 format (e.g., YYYY-MM-DD or YYYY-MM-DD HH:MM:SS) into a datetime.datetime object.
                    date.fromisoformat(expiry)
                    break
                except ValueError:
                    print("Invalid date. Date must be in (YYYY-MM-DD)")

            while True:
                try:
                    quantity = int(input("What is the quantity?"))

                    if quantity > 0:
                        break
                    else:
                        print("The quantity must be greater than zero")

                except ValueError:
                    print("Please enter a whole number above zero")

            batch = {"expiry": expiry, "quantity": quantity}

            # make an empty list for the item, we make a list so it could store multiple dictionary's (batch)
            if name not in self.items:
                self.items[name] = []

            # check if a batch has the same expiry, prevents having two dictionary's when we can add to the quantity instead
            for b in self.items[name]:
                if b["expiry"] == expiry:
                    b["quantity"] += quantity
                    break

            else:
                self.items[name].append(batch)

            self.save_items()

            print(f"added {quantity} x {name} to your pantry with an expiry date of: {expiry}")

            while True:

                restart = input("Would you like to add another item? (y/n)").lower()

                if restart.startswith("n"):
                    return_to_menu()
                    return # leave add_items completely

                elif restart.startswith("y"):
                    break # go back to most outer loop

                else:
                    print("Please type y or n")


    # doesn't work without a proper expiry input
    def date_conversion(self, expiry_input):
        """Calculates how many days are left before an item expires."""

        # datetime.date class method: returns today's date (year, month , day)
        today = date.today()

        # YYYY-MM-DD > 2025-01-01 > YEAR = "2025", MONTH =  "01", DAY = "01,"
        parts = expiry_input.split("-")
        year, month, day = int(parts[0]), int(parts[1]), int(parts[2])

        # class from datetime
        # creates a datetime.date object (year, month day)
        # This converts the 3 integers into a real date we can use for calculations
        expiry_date = date(year, month, day)

        days_left = expiry_date - today

        # .days gives us the number of whole days as an integer
        return days_left.days

    def auto_expire(self):
        """Automatically expires products in the pantry and tells the user if any products have been removed"""
        today = date.today()
        removed_messages = []  # List to inform user which items are removed from the pantry
        # Dictionary to add all the items from "keep" list in. We'll overwrite pantry.json with this
        updated_pantry = {}
        warning_messages = []  # list to inform user which items will expire today

        # we create a new list (copy) with all the keys inside self.item
        # we will go over each expiry date in the copy, and delete expired items in the original copy
        # We don't go over each expiry date in the original copy, because while we are deleting things are shifting which may result in bugs
        for product in list(self.items.keys()):
            # "keep" is a list for items that are not expired, later used to overwrite current Pantry.json
            # Create a fresh 'keep' list at the start of each product iteration (e.g., "Apple").
            # For other "products" e.g. "Milk" we want a different list, with potentially multiple dictionaries.
            keep = []
            for dictionary in self.items[product]:
                if "expiry" in dictionary:
                    # expiry (date) = string, transform into date object to compare with date.today()
                    exp = date.fromisoformat(dictionary["expiry"])
                    if exp < today:
                        removed_messages.append(
                            f"{product} with a quantity of {dictionary['quantity']} was removed from your pantry because it expired on {dictionary['expiry']}\n")

                    elif exp == today:
                        keep.append(dictionary)
                        warning_messages.append(f"{product} will expire today!\n")

                    else:
                        keep.append(dictionary)

            if keep:
                updated_pantry[product] = keep

        self.items = updated_pantry
        self.save_items()

        if removed_messages or warning_messages:

            if removed_messages:
                print(" 🗑️     Removed: ")
                # * is an operator, each item in the list will be printed seperately , with \n in between
                print(*removed_messages, sep="\n")

            if warning_messages:
                print(" ⚠️     Warnings: ")
                print(*warning_messages, sep="\n")

        else:
            print(
                "Your pantry has been analyzed. No products have expired or will expire today.")

    def empty_pantry(self):
        """Delete all items from the pantry"""

        empty = True
        while empty == True:

            if not self.items:
                pantry_empty()
                empty = False

            else:
                confirmation = False
                while confirmation == False:

                    confirm = input(
                        "Are you sure you want to empty the entire pantry? (Yes/No)\n").strip().lower()

                    if confirm.startswith("n"):
                        print("Cancelled")
                        confirmation = True

                    elif confirm.startswith("y"):
                        self.items = {}
                        self.save_items()
                        print("Pantry emptied.")
                        confirmation = True

                    else:
                        print("Please choose a valid answer")

            empty = False
        return_to_menu()

    def delete_item(self):
        """Delete individual items from Pantry"""

        if not self.items:
            pantry_empty()
            return_to_menu()
            return

        else:
            # print("\n" + "*" * 60)
            # print("\nYour current pantry: ")
            # print ("\n" + "*" * 60)
            #main_menu =  False to dodge optional code from show_items
            self.show_items(main_menu = False)

        deleting = True

        while deleting:

            item = input("Type the item name you'd like to delete,  or type 'skip' to return to the main menu\n").strip().capitalize()

            if item == "Skip":
                return_to_menu()
                return

            elif item not in self.items:
                print("Product not found, please try again.")

            elif item in self.items:
                if len(self.items[item]) == 1:
                    # there is only one dictionary (batch), since len == 1.
                    # To find the correct dictionary we need to write the corrosponding number, in this case "0".
                    # if we don't add [0] Python will send back a list, since self.items[item] is a list. Because of [0] python will send the first dictionary.
                    # We use the variable name "batch" to be consistent with add_items(self)
                    batch = self.items[item][0]
                    # Give right parameters, because these aren't global.
                    delete_amount = delete_number(batch["quantity"], item)

                    if delete_amount >= batch["quantity"]:
                        del self.items[item]

                    else:
                        batch["quantity"] -= delete_amount

                else:

                    batches = self.items[item]

                    print(f"\n{item} has multiple batches, please choose which batch you'd like to (partly) delete: ")

                    # we assign two variables: "index" and "batch" and loop through "batches" using the enumerate function.
                    # enumerate() function adds a counter to each item in a list or any other iterable, and returns a list of tuples
                    # containing the index position and the element for each element of the iterable.
                    # For example enumerate return to python:
                    # (1, {batch_dict}), (2, {batch_dict})
                    # the user never sees the numbers "1" and "2", that's why we assign "index" to those numbers.
                    # start=1 means it will start counting from 1, start=10 means it starts counting from 10.
                    for index, batch in enumerate(batches, start=1):
                        expiry = batch["expiry"]
                        quantity = batch["quantity"]
                        days_left = self.date_conversion(expiry)

                        print(f"{index}. Expiry: {expiry} | Quantity: {quantity} | Days left: {days_left}")


                    # let user choose a batch
                    while True:
                        choice = input("Please type the number of the batch you want to delete: ").strip()

                        # isdigit checks if all characters are a digit > 1,5 != isidigit > "," is not a digit
                        if choice.isdigit():
                            # despite the choice being a digit and integer we still need to convert it into a integer
                            choice = int(choice)

                            if 1 <= choice <= len(batches):
                                # choice -1 because we started counting choices from 1 (enumerate(start=1))
                                # I made this choice because it's more natural for the user to start their choice from 1
                                # however python counts from 0 onwards, so we have to subtract 1 from choices.
                                # For example if choice = 1, python will choose the second batch
                                # because the first batch is batches[0], not batch[1]
                                selected_batch = batches[choice - 1 ]
                                break

                            else:
                                print(f"Please enter an integer number between 1 and {len(batches)}.")


                        else:
                            print(f"Please enter an integer number between 1 and {len(batches)}.")

                    # for delete_number function we need "quantity", "item".
                    # We find the correct quantity, item because batches = the dictionaries of the specific item the user
                    # choice at the top of this function. The selected batch filters which number of library the user needs.
                    # This library contains the correct quantity that the user once gave in the " add_item" function
                    delete_amount = delete_number(selected_batch["quantity"], item)

                    # .remove is a builld-in python function to remove an element of a list.
                    # "batches" is a list with multiple dictionaries, "selected_batch" is one of it's dictionares.
                    # We cannot do selected_batch.remove() because the former isn't a list, but a dictionary.
                    if delete_amount == selected_batch["quantity"]:
                        batches.remove(selected_batch)

                    else:
                        selected_batch["quantity"] -= delete_amount


                # batch = self.items[item][0], this means batch = part of self.items
                # self.save_items() writes the current self.items to pantry.json
                # Because we adjusted part of self.items ( quantity ), this variable has been edited.
                # We can simply write self.items back to the json file, without saving anything to self.items manually
                self.save_items()

                # show the pantry after the user deleted an item.
                self.show_items(main_menu = False)

                # if delete_again is not True > delete_again = False
                if not delete_again():
                    return_to_menu()
                    return


# Quantity and item are 2 variables that stored inside Class pantry
# We ask questions in a loop inside delete_items function, so only in that loop we know which "quantity" and "item" to select
# For this reason we need these variables as input for this function to work properly.
def delete_number(quantity, item):
    """Asks the user how many items he would like to delete. Helpful for delete_items(self)"""
    while True:
        try:
            delete_amount = int(input(f"You currently have {quantity}  x {item} in your Pantry. How many would you like to Delete?"))
            # number must be greater than 0, but less than the actual quantity ( You can't delete more than you have)
            if 0 < delete_amount <=  quantity:
                # Return automatically ends loop
                return delete_amount

            else:
                print(f"Please choose an integer number between 1 and {quantity}")

        except ValueError:
            print(f"Please type an integer number between 1 and {quantity}")


def delete_again():
    """Asks the user whether he wants to delete an item"""
    answer = input("Would you like to delete another item?(Y/N)")
    # This is a boolean > python returns either True or false
    return answer.startswith("y")

def return_to_menu():
    """Messages before returning to main menu"""
    print("\n" + "*" * 60)
    print("\nYou will be redirected to the main menu.")
    print("\n" + "*" * 60)

def pantry_empty():
     """ Message when pantry is empty """
     print("\n" + "*" * 60 + "\n")
     print("Your pantry is already empty")

