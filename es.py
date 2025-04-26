# Program that reads in a text file and counts the numbers of instances of the letter 'e' in the file. 
# The name of the text file is specified as an argument to this program.

# Author: Susan Collins

# v01: basic structure only, no error-checking yet
# v02: error checking for inputs

# Library to allow the passing of command-line arguments. If the module is not installed, program ends. 
try:
    import sys
except ModuleNotFoundError:
    print("This program required the module 'sys'. Please install this module and try again.")
    exit()


# Function to print help message, called if there are no command-line arguments called with this program. This function uses argv[0] to dynamically print the program name. 
def print_help():
    print(f"This is a program to count the instanced of the letter 'e' in a text file.")
    print(f"This program should be called as: $ python {sys.argv[0]} <FILE.TXT>")


# If there are no arguments on the command line, print the help message and end program. argv[0] is the name of this program, so len(sys.argv) will always be at least 1 when the program is run.
if len(sys.argv) < 2:
    print_help()
    exit()

# get text file name as command-line argument 
FILENAME = sys.argv[1]
print(f"filename is {FILENAME}")

# declare variable to count the instances of 'e's
count = 0

# open the specified text file read-only 
try:
    with open (FILENAME, 'rt') as text_file:

        for line in text_file:

            #loop through all characters in this line
            for char in range(0,len(line)):
                
                # only looking for lower-case e's here
                if line[char] == 'e':
                        
                    count+=1

            # sanity check - print the running count before each line
            # print(f"{count} - {line}")
            
        print(f"Finished - there are {count} instances of the letter e in the file {FILENAME} ")


# Exception if the file does not exist
except FileNotFoundError:
        print(f"Error! The file {FILENAME} does not exist.")

# Exception if the file is not a text file
except UnicodeDecodeError:
        print(f"Error! The file {FILENAME} is not a text file.")

