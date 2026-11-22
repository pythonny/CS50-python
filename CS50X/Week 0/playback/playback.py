#In a file called playback.py, implement a program in Python that prompts the user for input and then outputs that same input, replacing each space with ... (i.e., three periods).

user_input = input().split()

for word in range(len(user_input)):
    if word < len(user_input) - 1: # add -1 because len = 3, but python starts counting from 0.
        print(user_input[word], end="...") # add "..." except for the last word
    else:
        print(user_input[word])

