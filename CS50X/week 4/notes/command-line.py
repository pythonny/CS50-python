import sys

# sys.argv is a list of  command-lines thats passed to my python script ( code command-line.py xxx)
# [0] is the name of the file
# [1] is the first input , for example: python command-line.py Donny outputs: "Hello, my name is Donny".
# print("hello, my name is", sys.argv[1])


# we need to let the user know when he didn't enter a correct Value:
# len should always be 2 because [0] = system name , and [1] = first input, in this example the name of the user
# sys.exit stops the program

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments")

print("Hello, my name is", sys.argv[1])

# basically a loop [1:] means from the 2nd to the end
for arg in sys.argv[1:]:
    print("Hello, my name is", arg)
