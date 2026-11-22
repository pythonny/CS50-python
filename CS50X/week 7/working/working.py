# Whereas most countries use a 24-hour clock, the United States tends to use a 12-hour clock. Accordingly, instead of “09:00 to 17:00”,
# many Americans would say they work “9:00 AM to 5:00 PM” (or “9 AM to 5 PM”), wherein “AM” is an abbreviation for “ante meridiem” and “PM” is an abbreviation for “post meridiem”, wherein “meridiem” means midday (i.e., noon).

# Conversion Table
# In a file called working.py, implement a function called convert that expects a str in any of the 12-hour formats below and returns the corresponding str in 24-hour format (i.e., 9:00 to 17:00).
# Expect that AM and PM will be capitalized (with no periods therein) and that there will be a space before each. Assume that these times are representative of actual times, not necessarily 9:00 AM and 5:00 PM specifically.

# 9:00 AM to 5:00 PM
# 9 AM to 5 PM
# 9:00 AM to 5 PM
# 9 AM to 5:00 PM
# Raise a ValueError instead if the input to convert is not in either of those formats or if either time is invalid (e.g., 12:60 AM, 13:00 PM, etc.). But do not assume that someone’s hours will start ante meridiem
# and end post meridiem; someone might work late and even long hours (e.g., 5:00 PM to 9:00 AM).

# Structure working.py as follows, wherein you’re welcome to modify main and/or implement other functions as you see fit, but you may not import any other libraries. You’re welcome, but not required, to use re and/or sys.

import re
import sys

time_conversion = {
    "12AM": "00",
    "1AM": "01",
    "2AM": "02",
    "3AM": "03",
    "4AM": "04",
    "5AM": "05",
    "6AM": "06",
    "7AM": "07",
    "8AM": "08",
    "9AM": "09",
    "10AM": "10",
    "11AM": "11",
    "12PM": "12",
    "1PM": "13",
    "2PM": "14",
    "3PM": "15",
    "4PM": "16",
    "5PM": "17",
    "6PM": "18",
    "7PM": "19",
    "8PM": "20",
    "9PM": "21",
    "10PM": "22",
    "11PM": "23"
}


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # ?P<> = group name
    # \d{} = digit in range
    # :? = optional ":"
    # \s? = optional space
    # | = or
    # .*? = optional any character, 0 or more repitions
    pattern = r"(?P<time_1>\d{1,2}:?\d{0,2})\s?(?P<zone_1>AM|PM) to (?P<time_2>\d{1,2}:?\d{0,2})\s?(?P<zone_2>AM|PM)"
    match = re.search(pattern, s, re.IGNORECASE)

    if not match:
        raise ValueError

    # link groupnames to variables
    time_1 = match.group("time_1")
    zone_1 = match.group("zone_1")
    time_2 = match.group("time_2")
    zone_2 = match.group("zone_2")

    # split hours and minutes, so that we later can convert the time zones > 1 am = 01:00 , 1 pm = 13:00
    if ":" in time_1:
        hour_1, minute_1 = time_1.split(":")
        hour_1 = int(hour_1)
        minute_1 = int(minute_1)
    else:
        hour_1, minute_1 = int(time_1), 0 # if no ":" means "whole hour", so zero minutes > 1 PM > 13:00

    if ":" in time_2:
        hour_2, minute_2 = time_2.split(":")
        hour_2 = int(hour_2)
        minute_2 = int(minute_2)
    else:
        hour_2, minute_2 = int(time_2), 0


    # Validate proper range
    if not 1 <= hour_1 <= 12:
        raise ValueError
    if not 0 <= minute_1 <= 59:
        raise ValueError
    if not 1 <= hour_2 <= 12:
        raise ValueError
    if not 0 <= minute_2 <= 59:
        raise ValueError

    # time conversion using the dictionary
    conversion_1 = time_conversion[f"{hour_1}{zone_1}"]
    conversion_2 = time_conversion[f"{hour_2}{zone_2}"]

    # combine time conversion + minutes , :02d = 2 decimals ( 13:00 not 13:0)
    return f"{conversion_1}:{minute_1:02d} to {conversion_2}:{minute_2:02d}"



if __name__ == "__main__":
    main()
