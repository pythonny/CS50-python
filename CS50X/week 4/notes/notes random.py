# random is a module you can import. This way we import everything from Random.
import random

# you can call "head" or "tails" anything you want. In this case we simulate a coin toss.
# Syntax : Start with () like any function, use [] to make a list, each item within "" or ''
coin = random.choice(["heads", "tails"])
print(coin)

# secondly you can import a specific function from any module.
# now we can write "choice" instead of "random.choice"
# from random import choice
# coin = choice(["heads", "tails"])
# print(coin)

# choose a random integer between 1 and 10
number = random.randint(1, 10)
print(number)

# use random.shuffle(x) , it can shuffle a list.
cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)
