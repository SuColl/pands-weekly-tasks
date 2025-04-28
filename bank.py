# bank.py
# This program reads in two amounts in cent, 
# adds them and returns the sum formatted in Euro.
# author: Susan Collins

# get first amount and check that it is an integer. If not, ask again.
amount1 = None
while amount1 == None:
    try:
        amount1=int(input("Enter the first amount (cent):"))
    except ValueError:
        print(f"That is not a valid amount of cent.")

#get second amount and check that it is an integer. If not, ask again.
amount2 = None
while amount2 == None:
    try:
        amount2=int(input("Enter the second amount (cent):"))
    except ValueError:
        print(f"That is not a valid amount of cent.")


##################################
# Calculate the Euro total as a float
totalEuro = (amount1 + amount2) / 100 
# print the sum in Euro
print(f"The sum of these is €{totalEuro:.2f}")
