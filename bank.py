# bank.py
# This program reads in two amounts in cent, adds them and returns the sum formatted in Euro.
# author: Susan Collins

#get first amount (Assumes valid input)
amount1=int(input("Enter the first amount (cent):"))

#get second amount (Assumes valid input)
amount2=int(input("Enter the second amount (cent):"))

##################################
# Method 1 - arithmetically calculate the number of whole euro and the number of remaining cents separately.
wholeEuro = (amount1 + amount2) // 100
remainingCent = (amount1 + amount2) - (wholeEuro * 100)
print(f"(Method 1): The sum of these is €{wholeEuro}.{remainingCent}")

##################################
# Method 2 - calculate the Euro total as a float
totalEuro = (amount1 + amount2) / 100 
# print the sum in Euro
print(f"(Method 2): The sum of these is €{totalEuro:.2f}")
