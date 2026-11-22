from pantry import Pantry
import sys

def show_items(p):
    p.show_items()

def add_to_pantry(p):
    p.add_items()

def delete_from_pantry(p):
    p.delete_item()

def empty_the_pantry(p):
    p.empty_pantry()

def auto_expire_pantry(p):
    p.auto_expire()

def main():

    p = Pantry()
    loop = True

    print("\n" + "*" * 60 + "\n" )
    print("🍰 Welcome to your Pantry 🥛".center(55))
    print("\n" + "*" * 60 + "\n")
    print("In your Pantry you can add or delete items (food/drinks) and keep track of your stock.")
    print("Items that are past the expiry date will be deleted from your Pantry automatically.")
    print("You'll get a warning when an item expires on the given day.")
    print("Please choose one of the options below: ")
    print("\n" + "*" * 60)

    while loop == True:

        print('Type "1" for loading the content in your Pantry.')
        print('Type "2" for adding an item to your Pantry.')
        print('Type "3" for deleting an item from your Pantry.')
        print('Type "4" to empty your entire Pantry.')
        print('Type "5" to close your Pantry (items will be automatically saved as long as they are not expired).')

        answer = (input("")).strip()

        if answer == "1":
            show_items(p)
        elif answer == "2":
          add_to_pantry(p)
        elif answer == "3":
           delete_from_pantry(p)
        elif answer == "4":
            empty_the_pantry(p)
        elif answer == "5":
            print("Goodbye!")
            sys.exit()
        else:
            print("Please choose a valid answer ( Number 1 to 5).")

if __name__ == "__main__":
    main()
