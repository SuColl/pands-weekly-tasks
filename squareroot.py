# program that takes a positive floating-point number as input and outputs 
# an approximation of its square root.
# This program uses a custom function to calculate the square root, 
# as an exercise.

# author: Susan Collins

# v01: rough layout of program flow
# v02: added initial version of sqrt calculation
# v03: added tolerance parameter to sqrt() to tell the square root 
# calculation loop when to stop. 
# v04: moved input to read_in_positive_float() and added input checks. 


# custom sqrt function, currently prints results at each step
def sqrt(input, tolerance = 0):
    # The tolerance parameter tells the function how close the final 
    # guess must be to the true root
    print(f"You called the sqrt function for {input}")

    # if the user enters a tolerance parameter of 0, the loop may never end. 
    # Therefore, in this case set tolerance to be 0.00001% of the input 
    # number.
    if tolerance == 0:
        tolerance = input * 0.0000001

    # choose a starting guess for the square root - roughly guessing 
    # one-tenth of the input number
    guess = input * 0.1
    difference = abs(input - (guess * guess))

    # loop over the Newtonian iteration until the difference between the 
    # guess and the real root is less than the tolerance
    while difference > tolerance:
        # see README for mathematical equation
        guess = 0.5 * (guess + (input / guess)) 

        # get difference between current root guess squared amd input number
        difference = abs(input - (guess * guess))

    # return the final guess
    return(guess)


# Function to read in and validate positive float from user
def read_in_positive_float():
    # initialise input variable as NoneType
    number = None

    while number == None:
        try: 
            number = float(
                input("Please enter a positive floating-point number: ")
                )

        # ValueError if input is blank or a non-numeric string
        except ValueError:
            print("That was not a floating-point number.")

        # if input is negative, reset number to None and try again
        else:
            if number < 0:
                print("That's a negative number.")
                number = None

    # Return the positive float.
    return(number)


### Main code block ###
# read in input number from user
number = read_in_positive_float()

# calling the custom sqrt function with no tolerance specified
answer = sqrt(number)

# print result, rounded to 3 decimal places
print(f"The square root of {number} is {answer:.3f}")
