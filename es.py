# Program that reads in a text file and counts the numbers of instances 
# of the letter 'e' in the file. 
# A different letter to count mya be specified on the command line.
# The name of the text file is specified as an argument to this program.

# Author: Susan Collins

# v01: basic structure only, no error-checking yet
# v02: error checking of required module and input TXT file 
# v03: option to specify letter to count


# Library to allow the passing of command-line arguments. 
# If the module is not installed, program ends. 
try:
    import sys
except ModuleNotFoundError:
    print("This program requires the module 'sys'.\n"
        "Please install this module and try again. \nGoodbye.")
    exit()


# Function to print help message, called if there are no command-line 
# arguments specified with this program. 
# This function uses argv[0] to dynamically print the program name. 
def print_help():
    print(
        "This is a program to count the instances of the letter 'e' in a "
        "text file. \nYou may choose a different letter to count by "
        "specifying it on the command line."
        )
    print(
        f"This program should be called as: "
        f"$ python {sys.argv[0]} <FILE.TXT> <optional letter>"
        )


# Function to count the instances of a letter in a given string. 
# Returns the count as an integer.
def count_letters(string, letter):
    count = 0

    #loop through all characters in the string
    for char in string:
                
        # using lower() here so that both uppercase and lowercase 
        # letters are counted 
        if char.lower() == letter.lower():
            count+=1
    
    return(count)


# If there are no arguments on the command line, print the help message 
# and end program. argv[0] is the name of this program, so len(sys.argv) 
# will always be at least 1 when the program is run.
if len(sys.argv) < 2:
    print_help()
    exit()


# get text file name as command-line argument 
FILENAME = sys.argv[1]
print(f"filename is {FILENAME}")



# Get letter to be counted as optional command-line argument. 
# If no letter is specified, the letter 'e' is counted. 
# The count will combine uppercase and lowercase instances.
try: 
    # get letter as next command-line argument, stripped of any whitespace
    letter_to_count = sys.argv[2].strip()       

except IndexError:
    # if there is no second command-line argument, the sys.argv[2].strip() 
    # line above will fail with IndexError
    letter_to_count = 'e'                      

except NameError: 
    # if for any other reason, letter_to_count fails to have a value assigned
    letter_to_count = 'e'

else:
    # if the second command-line argument has more than one character, 
    # program ends. Single numbers are accepted.
    if len(letter_to_count) > 1:                
        print(
            f"This program can only count single letters, and you asked it "
            f"to count {letter_to_count}. \nGoodbye.")
        exit()


# declare variable to count the instances of 'e's
count = 0
# open the specified text file read-only 
try:
    with open (FILENAME, 'rt') as text_file:
        for line in text_file:

            count += count_letters(line, letter_to_count)
            
        print(
            f"Finished - there are {count} instance(s) of the letter "
            f"{letter_to_count} in the file {FILENAME} ")

# Exception if the file does not exist
except FileNotFoundError:
        print(f"Error! The file {FILENAME} does not exist.")

# Exception if the file is not a text file
except UnicodeDecodeError:
        print(f"Error! The file {FILENAME} is not a text file.")

