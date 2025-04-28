# program that takes a positive floating-point number as input and outputs 
# an approximation of its square root.
# This program uses a custom function to calculate the square root, 
# as an exercise.

# author: Susan Collins

# v01: rough layout of program flow
# v02: added initial version of sqrt calculation
# v03: added tolerance parameter to sqrt() to tell the square root 
# calculation loop when to stop. 


# custom sqrt function, currently prints results at each step
def sqrt(input, tolerance = 0):
    # The tolerance parameter tells the function how close the final 
    # guess must be to the true root
    print(f"you called the sqrt function for {input}")

    # if the user enters a tolerance parameter of 0, the loop may never end. 
    # Therefore, in this case set tolerance to be 0.001% of the input number.
    if tolerance == 0:
        tolerance = input * 0.00001

    # choose a starting guess for the square root - roughly guessing 
    # one-tenth of the input number
    guess = input * 0.1
    difference = abs(input - (guess * guess))
    print(guess, difference, tolerance)

    # loop over the Newtonian iteration until the difference between the 
    # guess and the real root is less than the tolerance
    while difference > tolerance:
        # see README for mathematical equation
        guess = 0.5 * (guess + (input / guess)) 

        # get difference between current root guess squared amd input number
        difference = abs(input - (guess * guess))

        print(guess, difference, tolerance)


    # return the final guess
    return(guess)


### Main code block ###
number = None

while number == None:
    try: 
        number = float(
            input("Please enter a positive floating-point number: ")
            )

    # ValueError if input is blank or a non-mumeric string
    except ValueError:
        print("That was not a floating-point number.")

    # if input is negative, reset number variable and try again
    else:
        if number < 0:
            print("That's a negative number.")
            number = None


# calling the custom sqrt function with no tolerance specified
answer = sqrt(number)

# print result
print(f"The square root of {number} is {answer}")
