# Perhaps the most popular place for pizza in Harvard Square is Pinocchio’s Pizza & Subs, aka Noch’s, known for its Sicilian pizza, which is “a deep-dish or thick-crust pizza.”

# Students tend to buy pizza by the slice, but Pinocchio’s also has whole pizzas on its menu too, per this CSV file of Sicilian pizzas, sicilian.csv, below:

# Sicilian Pizza,Small,Large
# Cheese,$25.50,$39.95
# 1 item,$27.50,$41.95
# 2 items,$29.50,$43.95
# 3 items,$31.50,$45.95
# Special,$33.50,$47.95
# See regular.csv for a CSV file of regular pizzas as well.

# Of course, a CSV file isn’t the most customer-friendly format to look at. Prettier might be a table, formatted as ASCII art, like this one:

# +------------------+---------+---------+
# | Sicilian Pizza   | Small   | Large   |
# +==================+=========+=========+
# | Cheese           | $25.50  | $39.95  |
# +------------------+---------+---------+
# | 1 item           | $27.50  | $41.95  |
# +------------------+---------+---------+
# | 2 items          | $29.50  | $43.95  |
# +------------------+---------+---------+
# | 3 items          | $31.50  | $45.95  |
# +------------------+---------+---------+
# | Special          | $33.50  | $47.95  |
# +------------------+---------+---------+
# In a file called pizza.py, implement a program that expects exactly one command-line argument, the name (or path) of a CSV file in Pinocchio’s format, and outputs a table formatted as ASCII art using tabulate,
# a package on PyPI at pypi.org/project/tabulate. Format the table using the library’s grid format. If the user does not specify exactly one command-line argument,
# or if the specified file’s name does not end in .csv, or if the specified file does not exist, the program should instead exit via sys.exit.

# Hints
# Recall that the csv module comes with quite a few methods, per docs.python.org/3/library/csv.html, among which are reader,
# per docs.python.org/3/library/csv.html#csv.reader, and DictReader, per docs.python.org/3/library/csv.html#csv.DictReader.
# Note that open can raise a FileNotFoundError, per docs.python.org/3/library/exceptions.html#FileNotFoundError.
# Note that the tabulate package comes with just one function, per pypi.org/project/tabulate. You can install the package with:

# TODO 1: add CSV file of Sicilian pizza and regular pizza menu to same folder
# TODO 2: if user does not add 1 command-line or the filename does not end in .csv or doesn't exist > sys.ext
# TODO 3: install and import tabulate package
# TODO 4: Read the file that's requested by command-line 1
# TODO 5: Output the requested file using the tabulate table

import csv
import sys
from tabulate import tabulate


def main():

    if len(sys.argv) != 2: # 1 commandline ==  len 2( name python file + name csv file)
        sys.exit(1)

    filename = sys.argv[1] # file name is the first argument which is 1, because 0 is the name of this python file
    if not filename.endswith(".csv"): # file name should always end with .csv
         sys.exit(1)


    try:
        with open(filename) as file: # with opens en closes the file

            file_read = csv.DictReader(file)
            # DictReader yields one dictionary per CSV row.
            # The first line of the CSV (the header) becomes the keys for those dictionaries.


            print(tabulate(file_read, headers="keys", tablefmt="grid")) # file_read in tabulate, the keys of file_read will become the headers of the table (kolomtitels), the tableformat = "grid" , see documentation for different formats.


    except FileNotFoundError:
            sys.exit(1)



main()


