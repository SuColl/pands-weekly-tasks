# A program that outputs whether or not today, at the time of running, 
# is a weekday or the weekend. 
# There is no user input.

# Author: Susan Collins

# note: This weekly task seems very short and I wonder if I'm missing
# something...

# import the module datetime which allows me to access date and time objects
try:
    import datetime
except ModuleNotFoundError:
    print("This program requires the module 'datetime'.\n"
        "Please install this module and try again. \nGoodbye.")
    exit()

# Returns the day of the week as an integer, where Monday is 1 and 
# Sunday is 7. 
# I use isoweekday() for personal preference. I could also have used the 
# more standard weekday() function which returns Monday as 0 and Sunday as 6.)
weekday_number = datetime.datetime.today().isoweekday()

# if the weekday_number is 1 to 5, it is a weekday.
if weekday_number < 6:
    print("Yes, unfortunately today is a weekday.")

else:
    print("It is the weekend, yay!")