# program that takes a positive floating-point number as input and outputs an approximation of its square root.
# This program uses a custom function to calculate the square root, as an exercise.

# author: Susan Collins

# v01: rough layout of program flow
# v02: added initial version of sqrt calculation


# custom sqrt function, currently prints results at each step
def sqrt(input):
    print(f"you called the sqrt function for {input}")

    # choose a starting guess for the square root - roughly guessing one-tenth
    guess = input * 0.1
    print(guess)

    # loop over the Newtonian iteration 100 times
    for loop in range(0, 100):
        # see README for mathematical equation
        guess = 0.5 * (guess + (input / guess)) 
        print(guess)

    # return the final guess
    return(guess)


### Main code block ###
# No validation or error-checking yet
number = float(input("Please enter a positive floating-point number: "))

# call the custom sqrt function
answer = sqrt(number)

# print result
print(f"The square root of {number} is {answer}")