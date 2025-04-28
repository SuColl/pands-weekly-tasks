# Programming and Scripting Weekly Tasks
author: Susan Collins

Description of this repository:  
A collection of submitted exercises for the Programming and Scripting Module, part of the Higher Diploma in Data Analytics, at Atlantic Technological University, Ireland, Spring 2025.

 Developed using [python](https://www.python.org/) v3.12.7  
 Modules used in these programs:  
- [NumPy](https://numpy.org)
- [MatPlotLib](https://matplotlib.org/) 
- [Sys](https://docs.python.org/3/library/sys.html)
- [DateTime](https://docs.python.org/3/library/datetime.html)

----------------------------------------------------------------------
## Week 01 Task: helloworld.py
This program prints "Hello, World!" to the terminal.

### Expected Output
```
$ python helloworld.py
Hello World!
```

----------------------------------------------------------------------
## Week 02 Task: bank.py
This program prompts the user to input two money amounts (in cent.) The program will then:
1. Add the two amounts
2. Print out the answer in a human readable format, with a euro sign and decimal point between the euro and cent of the amount 

### Expected Output
```
$ python bank.py
Enter the first amount (cent):jdfnlsdnf
That is not a valid amount of cent.
Enter the first amount (cent):2222.444
That is not a valid amount of cent.
Enter the first amount (cent):5023
Enter the second amount (cent):-456
The sum of these is €45.67
```

### Notes on my approach
- The program checks that the inputs are integers. Negative integers are permitted.

- I initialise the input variables as None so that once they have a value assigned, the expression `var == None` will always evaluate as False. 
If the input variables were initialised as boolean False, then with an input integer of 0 the expression `var == False` would evaluate as True.

- My initial method for calculating the Euro amount produced an inaccurate result if the sum of the inputs was negative, due to the floor operator rounding down. My final code uses another method.

```python
##################################
# Initial program method - now removed 
# Arithmetically calculates the number of whole euro 
# and the number of remaining cents separately.
wholeEuro = (amount1 + amount2) // 100
remainingCent = (amount1 + amount2) - (wholeEuro * 100)
print(f"(Method 1): The sum of these is €{wholeEuro}.{remainingCent:02d}")
# This code produces inaccurate results.
```

### Research and Sources
On the None type: [GeeksForGeeks: Declare variable without value](https://www.geeksforgeeks.org/declare-variable-without-value-python/)  
Floor division discussion: [StackOverflow: Floor division with negative number](https://stackoverflow.com/questions/37283786/floor-division-with-negative-number)

----------------------------------------------------------------------
## Week 03 Task: accounts.py
This program reads in an alpha-numeric account number, and outputs the account number with only the last 4 digits showing (and the preceding digits replaced with Xs).

If the account number has 4 digits or fewer, it is output without obfuscation.

### Expected Output
```
$ python accounts.py
Please enter an account number: 
You entered nothing. Try again.
Please enter an account number: 45362*! 
Please only enter alphanumeric characters (Aa-Zz, 0-9)
Please enter an account number: Abcde324552jkl
XXXXXXXXXX2jkl
```

### Notes on my approach
- The account number can contain both numbers and letters, but not spaces.
- The program rejects user input if it is an empty string.
- I assume that the input account number should be alphanumeric, i.e. no special characters like %*^&. I use the string method `isalnum()` to check this, and reject input that contains special characters.

### Research and Sources
Check if string is alphanumeric: [W3Schools: Python String isalnum() Method](https://www.w3schools.com/python/ref_string_isalnum.asp)

----------------------------------------------------------------------
## Week 04 Task: collatz.py
This program asks the user to input any positive integer, then repeats two simple arithmetic operations on this number, after the manner of the Collatz conjecture. If the number is even it is divided by two, if it is odd it is multiplied by three and 1 is added. The program ends if/when the current value reaches 1. 

This program performs some simple checks on the user input; if the input is not a positive integer, it requests another input.

### Expected Output
```
$ python collatz.py
Please enter a positive integer: 
That's not a positive integer, you entered nothing.
Please enter a positive integer: 22.345
That's not a positive integer
Please enter a positive integer: spam
That's not a positive integer
Please enter a positive integer: -12
You entered -12, that's a negative integer.
Please enter a positive integer: 27
27 82 41 124 62 31 94 47 142 71 214 107 322 161 484 242 121 364 182 91 274 137 412 206 103 310 155 466 233 700 350 175 526 263 790 395 1186 593 1780 890 445 1336 668 334 167 502 251 754 377 1132 566 283 850 425 1276 638 319 958 479 1438 719 2158 1079 3238 1619 4858 2429 7288 3644 1822 911 2734 1367 4102 2051 6154 3077 9232 4616 2308 1154 577 1732 866 433 1300 650 325 976 488 244 122 61 184 92 46 23 70 35 106 53 160 80 40 20 10 5 16 8 4 2 1 
```

### Notes on my approach
For this program, as input error-checking I use a series of if/elif/else statements to check that the input is a positive integer. 
- `len(number) == 0` evaluates True if the input is an empty string
- `number == "0"` evaluates True if the the input is zero
- `number[0]=="-" and number[1:].isdigit())` evaluates True if the input is a negative integer
- `not number.isdigit()` evaluates True if the input is a float or a non-numeric string

Only once all these checks are passed do I cast the input as an integer, to avoid a ValueError. 
I wrote this if/elif/else approach before I had learned to use the try/except blocks, and I have left it here as it is perfectly functional for this program, and I may want to use these evaluations again. 

### Research and Sources
Blog post on using isdigit() vs isnumeric() vs isdecimal(), which also reminded me to strip whitespace from the input: [miguendes.me: How to Choose Between isdigit(), isdecimal() and isnumeric() in Python](https://miguendes.me/python-isdigit-isnumeric-isdecimal)

Follow-up reading: [W3Schools: Python String isdecimal() Method](https://www.w3schools.com/python/ref_string_isdecimal.asp), [w3Schools: Python String isdigit() Method](https://www.w3schools.com/python/ref_string_isdigit.asp), [W3Schools: Python String isnumeric() Method](https://www.w3schools.com/python/ref_string_isnumeric.asp)

Handy method of slicing the negative sign off a negative integer, and using isdigit() to validate the rest, mentioned on [StackOverflow: "How do I check if a string is a negative number before passing it through int()?"](https://stackoverflow.com/a/78912188)


----------------------------------------------------------------------
## Week 05 Task: weekday.py
This program outputs whether or not today (at the time of running) is a weekday. There is no user input.

### Module required
[DateTime](https://docs.python.org/3/library/datetime.html)

### Expected Output if called on Monday through Friday:
```
$ python weekday.py 
Yes, unfortunately today is a weekday.
```
### Expected Output if called on Saturday or Sunday:
```
$ python weekday.py 
It is the weekend, yay!
```

### Notes on my approach
I used the isoweekday() function in this program because it's my personal preference, and also because of my abiding love and respect for the [International Organization for Standardization](https://www.iso.org/home.html). It also made the coding easier.

### Research and Sources
[W3Schools: Python Datetime](https://www.w3schools.com/python/python_datetime.asp)

[Python documentation: datetime — Basic date and time types](https://docs.python.org/3/library/datetime.html)

lovely deep blogpost about datetime: [Towards Data Science: Time Travel Made Easy: A Comprehensive Guide to Python Datetime](https://towardsdatascience.com/time-travel-made-easy-a-comprehensive-guide-to-python-datetime-326dd1c57391/)


----------------------------------------------------------------------
## Week 06 Task: squareroot.py
This program takes a positive floating-point number as input and outputs an approximation of its square root, using a custom sqrt() function, as an exercise in creating functions. 

### Expected Output 
```
$ python squareroot.py
Please enter a positive floating-point number: eggs
That was not a floating-point number.
Please enter a positive floating-point number: -22.4
That's a negative number.
Please enter a positive floating-point number: 4.16
You called the sqrt function for 4.16
The square root of 4.16 is 2.040
```

### Notes on my approach
- The input function rejects non-numeric and negative input.
- The custom sqrt() function uses Newton's method of finding square roots. This is an iterative process where each step gives a result that is closer to the true answer. Given a positive number $a$, for which you want to find the square root, and given a starting approximate value of the root $x_n$, the iteration is given by:

$$
x_{n+1}= \frac{1}{2} \left({x_n + \frac{a}{x_n}}\right)
$$

- I use a value of 10% of the input float as a starting guess for the square root

- Stopping the loop: Initially I hard-coded the loop to run the above equation 100 times, but this is often unnecessary. Ideally I would like the loop to stop when it has found the correct answer, but because the comparison of floats can be inexact, the loop may not ever stop. So, I added a tolerance parameter to the `sqrt()` function that indicates how close to the true answer the calculated answer must be to be considered 'correct' and end the loop. (The custom `sqrt()` function in this program can accept a different tolerance parameter at the time of calling, but I do not use that functionality in the main body of this program.)

### Research and Sources

On the inherent imprecision of comparing floats: [GeeksForGeeks: Comparing Floating Points Number for Almost-Equality in Python](https://www.geeksforgeeks.org/comparing-floating-points-number-for-almost-equality-in-python/)

Newton's method: [Wikipedia: Use of Newton's method to compute square roots](https://en.wikipedia.org/wiki/Newton%27s_method#Examples)

LaTeX in Markdown formatting references: [VisualStudio.com: Markdown and Visual Studio Code](https://code.visualstudio.com/docs/languages/markdown)
and [upyesp Blog: Cheat Sheet: Adding Math Notation to Markdown](https://www.upyesp.org/posts/makrdown-vscode-math-notation/)

----------------------------------------------------------------------
## Week 07 Task: count_es.py and es.py
**Please Note: I started developing this program as count_es.py, and after the first commit, I renamed it to es.py. Unfortunately, GitHub sees these as two files with separate histories.**

This program reads in a text file and outputs the number of e's it contains. The filename is supplied as an argument on the command line.   
This program will alert if the specified file does not exist or the file is not a text file.
This program will print help text if there is no filename specified.

### Module required
[Sys](https://docs.python.org/3/library/sys.html)

### Additional features 
- I added an option to specify a different character to be counted on the command-line, 
as `$ python es.py <FILE.TXT> <optional letter>`. Only a one-character argument will be accepted.
- This program will count both lowercase and uppercase instances of e (or any other letter specified) and provide the combined total.

### Expected Output
```
# Calling this program with a valid text file
$ python es.py pride_and_prejudice.txt
filename is pride_and_prejudice.txt
Finished - there are 74451 instance(s) of the letter e in the file pride_and_prejudice.txt 

# Calling this program with a valid text file and specifying a single character to count
$ python es.py pride_and_prejudice.txt t
filename is pride_and_prejudice.txt
Finished - there are 50837 instance(s) of the letter t in the file pride_and_prejudice.txt 

# Calling this program with a valid text file and specifying multiple letters to count
$ python es.py pride_and_prejudice.txt xyzzy
filename is pride_and_prejudice.txt
This program can only count single letters, and you asked it to count xyzzy. 
Goodbye.

# Calling this program with no file specified prints help information
$ python es.py
This is a program to count the instances of the letter 'e' in a text file. 
You may choose a different letter to count by specifying it on the command line.
This program should be called as: $ python es.py <FILE.TXT> <optional letter>

# Calling this program with a file that does not exist prints a relevant text message
$ python es.py file_not_existing.txt
filename is file_not_existing.txt
Error! The file file_not_existing.txt does not exist.

# Calling this program with a file that is not a text file prints a relevant text message
$ python es.py testbin.bin
filename is testbin.bin
Error! The file testbin.bin is not a text file.

```

### Notes on my approach
Error handling: I found the correct names of exceptions for this program by trial and error. 
- importing a module that had not been installed throws a `ModuleNotFoundError`.
- trying to open a file which does not exist throws a `FileNotFoundError`.
- attempting to open a binary file as a text file throws a `UnicodeDecodeError`.  

### Research and Sources
Txt files for development and testing were downloaded from [Project Gutenberg](www.gutenberg.org), these text files have been added to `.gitignore` so they will not be pushed to GitHub.

Tutorial on passing command-line arguments to a Python program: [tutorialspoint.com: Python - Command-Line Arguments](https://www.tutorialspoint.com/python/python_command_line_arguments.htm)

Terminating a program (sys.exit()): [StackOverflow: How do I terminate a script?](https://stackoverflow.com/a/73673)

Error Handling: W3schools on try/except/else/finally: [W3Schools: Python Try Except](https://www.w3schools.com/python/python_try_except.asp#gsc.tab=0)

W3schools list of Python built-in exceptions: [W3Schools:Python Built-in Exceptions](https://www.w3schools.com/python/python_ref_exceptions.asp)

----------------------------------------------------------------------
## Week 08 Task: plottask.py
This program creates a plot that displays:
- a histogram of a normal distribution of 1000 values with a mean of 5 and standard deviation of 2, 
- the function  h(x)=x³ in the range 0 to 10,   

on one set of axes.
A copy of the image of the plot (histogram_and_cube_function.png) is also in the repository.

### Modules required
- [NumPy](https://numpy.org)
- [MatPlotLib](https://matplotlib.org/) 

### Additional features
- I dynamically set my histogram bins to be of size 1 and centred on each integer value. Code to generate a bin limit range using `numpy.arange()` was suggested by [this StackOverflow answer](https://stackoverflow.com/a/12176344).
- I added a secondary y-axis for the cubic function. As the maximum value of the histogram is approximately 200, and the value of the cubic function is 1000 at x=10, they do not display well on the same vertical scale. 

### Expected Output
This program generates a PNG image showing the requested histogram and cube function.
![](histogram_and_cube_function.png)

### Research and Sources
**Using numpy.random.Generator().normal**  
The NumPy documentation states that the RandomState function used in lectures has been superseded by the Generator method.
The method to generate the normally-distributed data points for this program was taken from https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.normal.html

**Plotting a second function on the same plot using a secondary y-axis**  
I followed this worked example, which let me create a twinned second Axes for the plot:
[MatPlotLib.org:Plots with different scales](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/two_scales.html)  
Plotting a combined legend for both functions required calling `figure.legend()` ([documented here](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.legend.html)), and using a `bbox_to_anchor` parameter to position the legend properly (method taken from [StackOverflow comment](https://stackoverflow.com/a/47370214))

**Superscript on plot axis labels**   
I wanted to display x^3 as x³ in my plot title and labels.  
A [GeeksForGeeks post](https://www.geeksforgeeks.org/how-to-print-superscript-and-subscript-in-python/) offered a way to insert Unicode directly into an f-string. This would work if I was using a fixed power of x, but I am using the variable 'index' to represent the power and I would like the plot title to change dynamically if this variable changes. 
The MathPlotLib documentation states that MathPlotLib supports a subset of TeX markup called [MathText](https://matplotlib.org/stable/users/explain/text/mathtext.html), so I can use that to apply superscript formatting to the variable value in my chart title.  
With index=3, `title="plot of $y=x^{index}$"`  renders as: plot of $y=x^3$

Note that I haven't had to use curly braces in the TeX expression itself; if I did, I would have to double-brace to avoid Python interpreting them as f-string variables. Through trial-and-error, I find that:  
With index=3, `title="plot of $y=x^{{5+{index}}}$"` renders as: plot of $y=x^{5+3}$

**Superscript in markdown**  
I then had to research a way to insert x³ this README.md file!  
Pure markdown does not have a superscript or subscript syntax.   
This [StackOverflow post](https://stackoverflow.com/questions/15155778/superscript-in-markdown-github-flavored) suggested some other solutions: 
1. Embedded HTML tags: `x<sup>3</sup>` displays as x<sup>3</sup> 
2. Embedded LaTeX: `$x^{3}$`  displays as $x^{3}$ 
3. Directly typing x³ as Unicode works, and leaves the raw Markdown file more readable.

----------------------------------------------------------------------
# General Research / Reading / Notes

## Research notes on Python style conventions
The [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/) outlines coding conventions for the Python standard library, which are commonly adopted as general style standards. In this repo I am adhering to:
- "Limit all lines to a maximum of 79 characters." (avoids the default wrapping in most tools)
- "Function names should be lowercase, with words separated by underscores as necessary to improve readability." 

### Other reading on this topic
[Python Morsels: Breaking up long lines of code in Python](https://www.pythonmorsels.com/breaking-long-lines-code-python/)  
[GeeksForGeeks: Python – Multi-Line Statements](https://www.geeksforgeeks.org/python-multi-line-statements/)

## Research notes on good git commit practices and commit messages
I have not consistently used any particular git commit message convention in these weekly tasks, but I am slowly starting to incorporate the advice from the sources below. 

There are many, _many_ articles and blog posts on what comprises a 'good' Git commit message. Some I have read:
- [freeCodeCamp(2019): How to Write Good Commit Messages: A Practical Git Guide](https://www.freecodecamp.org/news/writing-good-commit-messages-a-practical-guide/)
- [Kelvin Romero @Medium(2023): Writing good commit messages](https://kelvinromero.medium.com/writing-good-commit-messages-527679b1babb)
- [Hashnode(2019): Which commit message convention do you use at work?](https://hashnode.com/post/which-commit-message-convention-do-you-use-at-work-ck3e4jbdd00zyo4s1h7mc7e0g)
- [Tim Pope(2008): A Note About Git Commit Messages](https://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html)

Common advice from these writers include:
- Using a separate subject line (concise, approx 50 characters) and optional body text (longer description)
- ["Atomic Commits"](https://sparkbox.com/foundry/atomic_commits_with_git), i.e. each commit represents one small, complete, independent chunk of work. This chunk should be large enough to contain a complete change, ideally with the codebase working both before and after the change, and also small enough that it can be described/understood easily and it represents only one change. If multiple changes are represented in one commit, it would be more difficult to track the history of the changes or their separate effects on the code. 
- Using the imperative tense of verbs. This convention seems to be a combination of (a) in English, verbs in this tense are usually shorter than in other tenses, (b) Git itself uses the imperative when it creates messages, so you might as well match. 

Many people explicitly follow the [Conventional Commits](https://www.conventionalcommits.org/en/about/) standard. This is a very detailed standard which is designed to allow the use of automated tools to parse and analyse the commit history. The full standard is not useful for me at this time, but one prominent feature which I have begun to use is the inclusion of a keyword at the start of each commit message to indicate the type of change, e.g.:
- feat: add a new feature
- fix: fix a bug
- docu: amend documentation

This is useful when looking back at past changes in the log, and it also reinforces the practice of only doing one type of change in each commit. 

----------------------------------------------------------------------
### End of README