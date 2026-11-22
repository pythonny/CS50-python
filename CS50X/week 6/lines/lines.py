# Lines of Code
# One way to measure the complexity of a program is to count its number of lines of code (LOC), excluding blank lines and comments. For instance, a program like

# # Say hello

# name = input("What's your name? ")
# print(f"hello, {name}")
# has just two lines of code, not four, since its first line is a comment, and its second line is blank (i.e., just whitespace). That’s not that many, so odds are the program isn’t that complex.
# Of course, just because a program (or even function) has more lines of code than another doesn’t necessarily mean it’s more complex. For instance, a function like

# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
# isn’t really twice as complex as a function like

# def is_even(n):
#     return n % 2 == 0
# even though the former has (more than) twice as many lines of code. In fact, the former might arguably be simpler if it’s easier to read! So lines of code should be taken with a grain of salt.

# Even so, in a file called lines.py, implement a program that expects exactly one command-line argument, the name (or path) of a Python file, and outputs the number of lines of code in that file, excluding comments and blank lines.
# If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .py, or if the specified file does not exist, the program should instead exit via sys.exit.

# Assume that any line that starts with #, optionally preceded by whitespace, is a comment. (A docstring should not be considered a comment.) Assume that any line that only contains whitespace is blank.
import sys


def main():
    if len(sys.argv) != 2: # command-line can only have 1 argument > len == 2 (name file + argument)
        sys.exit(1) # Check50 said sys.exit should by anything but 0

    elif not sys.argv[1].endswith(".py"): # File should be a python file > endswith.py
        sys.exit(1)

    try:
         with open(sys.argv[1]) as file: # With open, means open and close a certain file, in this case the first argument.
            count = 0 # We have to count the lines, so we start with 0 before the loop.
            for line in file: # Since python reads from top to down, it will automatically read line by line.

                line = line.lstrip() # We remove all spaces from the left for the next step.

                if line.startswith("#"): # Comments are not counted, so we don't count anything that starts with "#"
                    continue

                if line.strip() == "": # We remove spaces from both left and right, empty lines are not counted.
                     continue

                count += 1 # if line is not empty or not a comment we add +1 to the count.

         print(count)


    except  FileNotFoundError: # if the argument, in this case the file the user wants to read is not found > error
            sys.exit(1)

main()
