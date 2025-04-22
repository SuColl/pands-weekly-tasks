# program that takes a positive floating-point number as input and outputs an approximation of its square root.
# This program uses a custom function to calculate the square root, as an exercise.

# author: Susan Collins

# custom sqrt function, currently does nothing but prints a line
def sqrt(input):
    print(f"you called the sqrt function for {input}")



### Main code block ###
# No validation or error-checking yet
number = float(input("Please enter a positive floating-point number: "))

# call the custom sqrt function
sqrt(number)