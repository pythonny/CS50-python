# Python already supports math, whereby you can write code to add, subtract, multiply, or divide values and even variables. But let’s write a program that enables users to do math, even without knowing Python.

# In a file called interpreter.py, implement a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place. Assume that the user’s input will be formatted as x y z, with one space between x and y and one space between y and z, wherein:

# x is an integer
# y is +, -, *, or /
# z is an integer
# For instance, if the user inputs 1 + 1, your program should output 2.0. Assume that, if y is /, then z will not be 0.

# Note that, just as python itself is an interpreter for Python, so will your interpreter.py be an interpreter for math!



# IMPORTANT: I realize that this system isn't functional, but it's good enough for the scope of this exercize.

# split the Expression into seperate strings
expression = input("Expression: ").split()

# Convert the first string into a float
x = float(expression[0])
# convert the last string into a float
z = float(expression[2])
# The operator that we'll use to calculate x and z
y = expression[1]


# Create a function to perform the correct calculation
def calculator():
     if y == "+":
          return x + z
     elif y == "/":
        return x / z
     elif y == "-":
         return x - z
     elif y == "*":
        return x * z

# print the result
print(calculator())

