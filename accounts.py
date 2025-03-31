# accounts.py
# This program reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with the character X.
# author: Susan Collins

# get input string. As the account number is described as "10-character", I assume it is alphanumeric, and cast it as a string.
account_number = str(input("Please enter a 10 digit account number: "))

# Assuming the input is valid and has 10 characters, extract the last 4 characters of the string
account_number_tail = account_number[-4:]

# print the obfuscated account number
print(f"XXXXXX{account_number_tail}")
