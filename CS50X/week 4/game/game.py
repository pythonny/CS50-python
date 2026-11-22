# Guessing Game
# I’m thinking of a number between 1 and 100…

# What is it?
# In a file called game.py, implement a program that:

# Prompts the user for a level,
# . If the user does not input a positive integer, the program should prompt again.
# Randomly generates an integer between 1 and
# , inclusive, using the random module.
# Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
# If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
# If the guess is larger than that integer, the program should output Too large! and prompt the user again.
# If the guess is the same as that integer, the program should output Just right! and exit.
import random

# make a loop, because we keep asking untill the input = integer and > 0
# break = end loop, continue = re-loop
while True:
    try:
        # max_number == Level ( level is N of random range 1, N)
        max_number = int(input("Level: "))
        if max_number > 0:
            break

    except ValueError:
        continue


def game():

    while True:
        # We try integer first so that we can create exceptions (non integer number aka ValueError)
        try:
            guess = int(input("Guess: "))

            # range is 1 , N ( level chosen), so the guess should also be > 0 
            if guess <=  0:
                continue
            if guess < number:
                print("Too small!")
            elif guess > number:
                print("Too large!")
            else:
                print("Just right!")
                break
        except ValueError:
            continue

# randrange is a function inside the random module. It doesn't include the last number, that's why max_number + 1
# we can write this after the game() function, because the file reads everything untill it reads "game()" at the end of the file, so it crosses {number}.
number = random.randrange(1, max_number + 1)

game()
