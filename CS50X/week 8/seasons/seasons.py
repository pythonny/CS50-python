# Assuming there are 365 days in a year, there are 365 ×24 ×60 =525,600 minutes in that same year (because there are 24 hours in a day and 60 minutes in an hour).
# But how many minutes are there in two or more years? Well, it depends on how many of those are leap years with 366 days, per the Gregorian calendar, as some of them could have 1 ×24 ×60 =1,440 additional minutes.
# In fact, how many minutes has it been since you were born? Well, that, too, depends on how many leap years there have been since! There is an algorithm for such, but let’s not reinvent that wheel. Let’s use a library instead.

#  Fortunately, Python comes with a datetime module that has a class called date that can help, per docs.python.org/3/library/datetime.html#date-objects.

# In a file called seasons.py, implement a program that prompts the user for their date of birth in YYYY-MM-DD format and then sings prints how old they are in minutes, rounded to the nearest integer,
# using English words instead of numerals, just like the song from Rent, without any and between words. Since a user might not know the time at which they were born, assume, for simplicity,
# that the user was born at midnight (i.e., 00:00:00) on that date. And assume that the current time is also midnight. In other words,
# even if the user runs the program at noon, assume that it’s actually midnight, on the same date. Use datetime.date.today to get today’s date, per docs.python.org/3/library/datetime.html#datetime.date.today.

# Structure your program per the below, not only with a main function but also with one or more other functions as well:

# You’re welcome to import other (built-in) libraries, or any that are specified in the below hints. Exit via sys.exit if the user does not input a date in YYYY-MM-DD format. Ensure that your program will not raise any exceptions.

# Either before or after you implement seasons.py, additionally implement, in a file called test_seasons.py, one or more functions that test your implementation of any functions besides main in seasons.py
# thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

# pytest test_seasons.py




from datetime import date
import sys
import inflect



def main():
    # Ask birthyear in (YYY-MM-DD)
    birthyear = date_conversion(input("Date of Birth: "))

    #calculate the amount of minutes that someone is alive for
    total_minutes = minutes(birthyear)

    # transfrom number to words
    words = number_to_words(total_minutes)

    # First word needs a capital + minutes at the end
    print(f"{words.capitalize()} minutes")



def date_conversion(d):
    # return a date object from datetime module from a date of birth for example "YYYY-MM-DD"
    # for example 2019-12-04 - datetime.date(2019, 12, 4)

    try:
        return date.fromisoformat(d)

    except ValueError:
        # wrong format or impossible date
        sys.exit("Invalid date")

# calculate the amount of minutes between day of birth and today
def minutes(birthyear):
    # class method inside date module to retrieve the day today
    today = date.today()

    # substract birthyear from today to see how many days we are alive
    # we need to use .days to get an integer, otherwise we get a "timedelta object" which is part of the datetime module
    # a timedelta object looks for example like ( days = 5059, seconds = 0), but if we add ".days" we get an integer > 5059
    days_alive = (today - birthyear).days

    # return the amount of minutes (60*24) = 1440 minutes per day
    return days_alive * 1440


def number_to_words(n):
    # Inflect is a Python module that helps with English words:
    # - Generate plurals: "cat" -> "cats"
    # - Generate singular nouns: "cars" -> "car"
    # - Create ordinals: 1 -> "first", 2 -> "second"
    # - Pick correct indefinite articles: "apple" -> "an apple", "car" -> "a car"
    # - Convert numbers to words: 1440 -> "one thousand, four hundred forty"
    # https://pypi.org/project/inflect/

    # this calls the module
    p = inflect.engine()

    # p.number_to_words(count), count is the amount of minutes in this case
    # The parameter andword="" removes the word "and" from numbers.
    # Example:
    #   p.number_to_words(101)          -> "one hundred and one"
    #   p.number_to_words(101, andword="") -> "one hundred one"
    # CS50's Seasons spec requires output without "and".
    answer = p.number_to_words(n, andword="")

    return answer



if __name__ == "__main__":
    main()
