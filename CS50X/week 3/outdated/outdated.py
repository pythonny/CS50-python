# In the United States, dates are typically formatted in month-day-year order (MM/DD/YYYY), otherwise known as middle-endian order, which is arguably bad design. Dates in that format can’t be easily sorted because the date’s year comes last instead of first.
# Try sorting, for instance, 2/2/1800, 3/3/1900, and 1/1/2000 chronologically in any program (e.g., a spreadsheet). Dates in that format are also ambiguous. Harvard was founded on September 8, 1636, but 9/8/1636 could also be interpreted as August 9, 1636!

# Fortunately, computers tend to use ISO 8601, an international standard that prescribes that dates should be formatted in year-month-day (YYYY-MM-DD) order, no matter the country, formatting years with four digits, months with two digits,
# and days with two digits, “padding” each with leading zeroes as needed.

# In a file called outdated.py, implement a program that prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636, wherein the month in the latter might be any of the values in the list below:

# [
#     "January",
#     "February",
#     "March",
#     "April",
#     "May",
#     "June",
#     "July",
#     "August",
#     "September",
#     "October",
#     "November",
#     "December"
# ]

# Then output that same date in YYYY-MM-DD format. If the user’s input is not a valid date in either format, prompt the user again. Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.

# Hints
# Recall that a str comes with quite a few methods, per docs.python.org/3/library/stdtypes.html#string-methods, including split.
# Recall that a list comes with quite a few methods, per docs.python.org/3/tutorial/datastructures.html#more-on-lists, among which is index.
# Note that you can format an int with leading zeroes with code like
# print(f"{n:02}")
# wherein, if n is a single digit, it will be prefixed with one 0, per docs.python.org/3/library/string.html#format-string-syntax.


month_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


#YYYY-MM-DD computer final result
#MM/DD/YYYY user
# September 8, 1636 user input 2


while True:
    inputted_date = input("date: ").strip()

    try:
        if "/" in inputted_date:
            month_user, day_user, year_user = inputted_date.split("/")

            # In the "Check50" they wrote "October/", so we want to make sure that the input is actually a number using this format.
            try:

                # make into integers
                year_computer = int(year_user)
                month_computer = int(month_user)
                day_computer = int(day_user)

            # make sure input is a number
            except ValueError:
                continue


            # month can maximum be  12 . We do this after we made the string into intergers above.
            if month_computer > 12:
                continue

            # day can be maximum 31. We do this after we made the string into intergers above.
            if day_computer > 31:
                continue

            print(f"{year_computer}-{month_computer:02}-{day_computer:02}")
            break

        else:
            # split only at the first space > September 8, 1636 > [ "September", "8, 1636"]
            first_split = inputted_date.split(" ", 1)

            # first_split has two parts now, we take the first. The month list is title cased so we add .title(). .strip() is for optional spaces
            month = first_split[0].strip().title()

            # we want to reprompt if month is not in month_list.
            if month not in month_list:
                continue


            # we take the indext of the monthlist but add +1 because we count from 0.
            month_number = month_list.index(month)  + 1
            # we convert to 01 - 12 with "n:02" > the "0" means spaces == 0 , "2" means the minimum width is 2 numbers. so 2 becomes 02 .
            # we need to make it into an f-string because we convert an integer to a string > 02 != integer
            month_number_converted = f"{month_number:02}"

            # make sure that day and years are integer.
            try:
                # The second part of first split > " 8, 1636" > we split ","
                second_split = first_split[1].split(",")
                day = int(second_split[0])
                year = int(second_split[1])

            except ValueError:
                continue
            # day can be maximum 31.
            if day > 31:
                continue

            print(f"{year}-{month_number_converted}-{day:02}")
            break


    except:
        break


