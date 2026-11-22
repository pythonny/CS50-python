# Suppose that you’re in a country where it’s customary to eat breakfast between 7:00 and 8:00, lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00. Wouldn’t it be nice if you had a program that could tell you what to eat when?

# In meal.py, implement a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time.
# If it’s not time for a meal, don’t output anything at all.
# Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##. And assume that each meal’s time range is inclusive. For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.

# Structure your program per the below, wherein convert is a function (that can be called by main) that converts time, a str in 24-hour format, to the corresponding number of hours as a float.
# For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5 hours).



# Example 7:02 and 17:15
# Step 1: Split before and after ":" > "7",  "02" and "17", "15"
# step 2: Split first string into hours, and second into decimal of hours?  > "7 hours" and "2/60" >  "17 hours" and "15/60"



def main():

     # inside main function, else you've to write it at the bottom (since you've to call a function after the program has read it)
     time = convert(input("What time is it? "))

    # if time between 7 > 8 , 12  > 13 , 18 > 19
     if  7 <= time <= 8:
        print("breakfast time")
     elif 12 <= time <= 13:
        print("lunch time")
     elif 18 <= time <= 19:
        print("dinner time")
     else:
        return "it's coding time!"


def convert(time):
    """This function converts the time to a float"""
    hours = int(time.rsplit(":")[0]) # you split the hour and minute by splitting before and after ":". 0 = the first part eg 7:05 > 7
    minutes = int(time.rsplit(":")[1]) # This is the second part after ":" eg 7:05 > 5.
    return hours + (minutes / 60 ) # returns hours in a float . eg 7:30 > 7 + ( 30 / 60) = 7.5





if __name__ == "__main__":
    main()


