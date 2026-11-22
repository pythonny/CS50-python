# Among the fonts supported by FIGlet are those at figlet.org/examples.html.

# FIGlet has since been ported to Python as a module called pyfiglet.

# In a file called figlet.py, implement a program that:

# Expects zero or two command-line arguments:
# Zero if the user would like to output text in a random font.
# Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, and the second of the two should be the name of the font.
# Prompts the user for a str of text.
# Outputs that text in the desired font.
# If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font, the program should exit via sys.exit with an error message.
from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

# figlet.genFonts is a function in the Figlet module that shows all the avaible fonts. "avaible_fonts" will now be a list.
avaible_fonts = figlet.getFonts()


# We need to check if the len is 1 or 3, because [0] is always name of the file, so the minimum len = 1. The exersize ask for 0 or 2 inputs > len = 1 + 0 = 1 and 1 + 2 = 3.
if len(sys.argv) != 1 and len(sys.argv) != 3:
    sys.exit("Invalid usage")

# User didn't choose a font, so we create a random font.
# Len = 1 , because the sys.argv[0] is the name of the file, so len can never be less than 1.
if len(sys.argv) == 1:
    random_font = random.choice(avaible_fonts)
    #setFont is a function inside the figlet module that sets the font, in this scenario we make it random
    figlet.setFont(font=random_font)


# len 1 = name of file, len 2 = set font yes or no , len 3 = name of font
if len(sys.argv) == 3:
    # first see if sys.argv[1] is indeed -f or --font ( synonyms of eachother, meaning "I want to set a font")
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        # sys.argv[2] = name of the font, check if this font actually exists within the module.
        if sys.argv[2] in avaible_fonts:
            figlet.setFont(font=sys.argv[2])
        else:
            sys.exit("Invalid usage")

    else:
        sys.exit("Invalid usage")

# above we set the rules for command lines, which are decided before the user input
# now we start creating the user input after deciding the font.

user_input = input("Input: ")
# Output seperate from render.Text so it prints seperately
print("Output: ")
# figlet.renderText is is function inside the figlet module to render a text with the chosen font
print(figlet.renderText(user_input))
