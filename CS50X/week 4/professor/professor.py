# One of David’s first toys as a child, funny enough, was Little Professor, a “calculator” that would generate ten different math problems for David to solve. For instance, if the toy were to display 4 + 0 = , David would (hopefully) answer with 4. If the toy were to display 4 + 1 = ,
# David would (hopefully) answer with 5. If David were to answer incorrectly, the toy would display EEE. And after three incorrect answers for the same problem, the toy would simply display the correct answer (e.g., 4 + 0 = 4 or 4 + 1 = 5).

# In a file called professor.py, implement a program that:

# Prompts the user for a level,
# . If the user does not input 1, 2, or 3, the program should prompt again.
# Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with
#  digits. No need to support operations other than addition (+).
# Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), the program should output EEE and prompt the user again, allowing the user up to three tries in total for that problem. If the user has still not answered correctly after three tries,
# the program should output the correct answer.
# The program should ultimately output the user’s score: the number of correct answers out of 10.
# Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts) the user for a level and returns 1, 2, or 3, and generate_integer returns a randomly generated non-negative integer with level digits or raises a ValueError if level is not 1, 2, or 3:

import random


def main():
    # User chooses level
    level = int(get_level())

    # life points and score outside the loop so it doesn't reset each time
    life_points = 3
    score = 0

    # program wants 10 random x + y questions  using the generate_integer function
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y

        # max 3 lifes, so we make a loop.
        while life_points > 0:
            try:
                guess = int(input(f"{x} + {y} = "))
                # we want to break the "while" loop, to go back to the "for" loop when the answer is correct.
                if guess == answer:
                    score += 1
                    break
                # points = correct answers - wrong answers. We have 3 lives, so we lose a live each time as well.
                elif guess != answer:
                    life_points -= 1
                    score -= 1
                    print("EEE")

            # same as a wrong guess
            except ValueError:
                life_points -= 1
                score -= 1
                print("EEE")

            # give the correct answer inside the loop when the user guesses wrong 3 times, else it will have a new value for x, y and answer.
            if life_points == 0:
                print(f"{x} + {y} = {answer}")

    # outside the loop, else it will print the score multiple times
    if life_points > 0:
            print(f"score: {score}")

# level should be 1-3
def get_level():
    while True:
        try:

            level = int(input("Level: "))

            # Range 1, 4 = 1-3, the last doesn't count. If the level is not 1-3 it will reprompt the user
            if level not in range(1, 4):
                continue
            else:
                return level
        # if user didn't write an integer it will reprompt
        except ValueError:
            continue



# Idk exactly what the diff between each level is so I made up 3 levels. Each level adds a digit.
# using the randint function I can create a random integer (lower range, highest range)
def generate_integer(level):

    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100,999)


if __name__ == "__main__":
    main()
