#In a file called bank.py, implement a program that prompts the user for a greeting. If the greeting starts with “hello”, output $0.
# If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.

greeting = input("Greeting: ").lower().split() # split removes all leading white spaces and splits strings into words.
first_word = greeting[0] # since split seperates a string into words, we take the first word.
first_letter = greeting[0][0] # from that first word we take the first letter



if first_word.startswith("hello"): # == True we can skip
    print("$0")

elif first_letter == ("h"):
    print("$20")
else:
    print("$100")





#  previous function, this worked well, but didn't have the correct output when the user typed "Hello," , because "Hello" != "Hello,"
#https://www.w3schools.com/python/ref_string_startswith.asp
# .startswith() is prevends this error

# if greeting[0] == "hello":
#     print("$0.")

# elif greeting[0][0] == "h":
#     print("$20.")
# else:
#     print("$100.")


