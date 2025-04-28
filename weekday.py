# A program that outputs whether or not today, at the time of running, 
# is a weekday or the weekend. 
# There is no user input.

# Author: Susan Collins

# note: This weekly task seems very short and I wonder if I'm missing
# something...

# import the module datetime which allows me to access date and time objects
# The try/except structure was discussed in later course lectures,
# Reference for list of exceptions:
# https://www.w3schools.com/python/python_ref_exceptions.asp
try:
    import datetime
except ModuleNotFoundError:
    print("This program requires the module 'datetime'.\n"
        "Please install this module and try again. \nGoodbye.")
    exit()

# Datetime module is briefly discussed on W3Schools, where they use the 
# datetime.datetime.now() function to return the current date and time as a 
# datetime object:
# https://www.w3schools.com/python/python_datetime.asp
# Then, in the documentation for the datetime library, 
# https://docs.python.org/3/library/datetime.html
# there are methods date.weekday() and date.isoweekday(), 
# which return the day of the week directly as an integer, 
# without the need for further parsing.
# Method datetime.date.today() returns a Date object, 
# and the method date.isoweekday() takes that Date object 
# and returns an integer.
# I also consulted a worked example using this method at
# https://www.shecodes.io/athena/10185-how-to-check-what-day-of-the-week-it-is-in-python

# Returns the day of the week as an integer, where Monday is 1 and 
# Sunday is 7. 
# I use isoweekday() for personal preference. I could also have used the 
# more standard weekday() function which returns Monday as 0 and Sunday as 6.
weekday_number = datetime.date.today().isoweekday()

# if the weekday_number is 1 to 5, it is a weekday.
if weekday_number < 6:
    print("Yes, unfortunately today is a weekday.")

else:
    print("It is the weekend, yay!")

