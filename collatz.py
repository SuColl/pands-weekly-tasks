# colllatz.py
# This program asks the user to input any positive integer, then repeats 
# two simple arithmetic operations on this number, after the manner of the 
# Collatz conjecture. 
# If the number is even it is divided by two, if it is odd it is multiplied 
# by three and 1 is added. 

# The program ends if/when the current value reaches 1. 
# author: Susan Collins

# Create boolean to flag the validity of the input number
valid = False


# Create loop until the input number is validated
while valid == False:

    # Get input string from user
    number = input("Please enter a positive integer: ")

    # strip whitespace from input string
    number = number.strip()

    # check input string for zero length
    if len(number) == 0:        
        print(f"That's not a positive integer, you entered nothing.")

    # check input string for 0
    elif number == "0":  
        print(f"You entered {number}, that's not a positive integer.")

    # check if input string is a negative integer
    elif (number[0]=="-" and number[1:].isdigit()):    
        print(f"You entered {number}, that's a negative integer.")

    # check input string is a float or a non-numeric string
    elif not number.isdigit():
        print(f"That's not a positive integer")

    # else mark input as valid and proceed
    else:
        valid = True


# cast number as int. I waited to do this until after the input was verified, 
# to avoid a ValueError.
number = int(number)

# print out the first number, without newlines (as specified in the weekly 
# task description)
print(number, end=" ")

# perform the Collatz operations, depending on whether the number is odd 
# or even at the end of each step. 
# Continue until the number equals 1.
while number != 1:
    # if even
    if (number % 2) == 0:
        number = int(number / 2)

    #if odd
    else:
        number = (number * 3) + 1
    
    # print the result of each step, again without newlines
    print(number, end=" ")


# Notes:
# In theory, this programme could run endlessly, if the input integer is 
# one for which the Collatz sequence does not end. The existence of such an 
# integer has not yet been proven.
# I used several if/elif/else statements to try and check the validity of 
# the input integer and avoid the program stopping due to errors. 
# There are probably better ways to handle errors / exceptions, but I don't 
# know them yet. 
