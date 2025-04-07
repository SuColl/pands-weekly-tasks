# accounts.py v02
# This program reads in an account number of unknown length, and outputs the account number with only the last 4 digits showing (and the leading digits replaced with the character X.)
# author: Susan Collins
# v01 assumed that a 10-digit number would be entered. 

# get input string. As the account number was originally described as "10-character", I assume it may contain both digits and letters, and cast it as a string.
account_number = str(input("Please enter an account number: "))

# get length of the input string
account_number_length = len(account_number)

# Assuming the input is valid, extract the last 4 characters of the string. If the original account number has four characters or fewer, it will output without obfuscation.
account_number_tail = account_number[-4:]

# Create a string to represent the obfuscated part of the account number (i.e. 4 characters shorter than the original account number). If the original account number has 4 characters or fewer, the obfuscated part will be an empty string.
account_number_obfuscation = "X" * (account_number_length - 4)

# print the concatenated obfuscated account number
print(f"{account_number_obfuscation}{account_number_tail}")
