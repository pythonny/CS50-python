#In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything,
# outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.

answer = input("What is the answer to the Great Question of Life, the Universe and Everything? ")
converted_answer = answer.lower().replace("-", " ").strip()

if converted_answer == "42" or converted_answer == "forty two":
    print("yes")

else:
    print("no")
