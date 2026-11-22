#In a file called bank.py, implement a program that prompts the user for a greeting. If the greeting starts with “hello”, output $0.
#If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.



def main():
    greeting = input("Greeting: ")
    amount = value(greeting)
    print(f"${amount}")



def value(greeting):
    greeting = greeting.lower().split() # split removes all leading white spaces and splits strings into words.
    first_word = greeting[0] # since split seperates a string into words, we take the first word.
    first_letter = greeting[0][0] # from that first word we take the first letter

    if first_word.startswith("hello"): # == True we can skip
        return("0")

    elif first_letter == ("h"):
        return("20")
    else:
        return("100")



if __name__ == "__main__":
    main()

# greeting = input("Greeting: ").lower().split() # split removes all leading white spaces and splits strings into words.
# first_word = greeting[0] # since split seperates a string into words, we take the first word.
# first_letter = greeting[0][0] # from that first word we take the first letter



# if first_word.startswith("hello"): # == True we can skip
#     print("$0.")

# elif first_letter == ("h"):
#     print("$20.")
# else:
#     print("$100")
