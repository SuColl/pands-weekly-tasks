# Program that reads in a text file and counts the numbers of instances of the letter 'e' in the file. 
# The name of the text file is specified as an argument to this program.

# Author: Susan Collins

# v01: basic structure only, no error-checking yet

# Library to allow the passing of command-line arguments
import sys

# get text file name as command-line argument 
FILENAME = sys.argv[1]
print(f"filename is {FILENAME}")

# declare variable to count the instances of 'e's
count = 0

# open the specified text file read-only - assuming it exits, and it a text file
with open (FILENAME, 'rt') as f:

    for line in f:

        for char in range(0,len(line)):
            
            # only looking for lower-case e's here
            if line[char] == 'e':

                count+=1

        # sanity check - print the running count before each line
        # print(f"{count} - {line}")
        
        

print(f"Finished - there are {count} instances of the letter e in the file {FILENAME} ")