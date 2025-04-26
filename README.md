# Programming and Scripting Weekly Tasks
author: Susan Collins

Description of this repo: A collection of submitted exercises for the Programming and Scriping Module, part of The Higher Diploma in Data Analytics course at the Atlantic Technological University, Ireland, Spring 2025.

 - Developed using python v3.12.7

## Week 02 Task: bank.py
This program will prompt the user and read in two money amounts (in cent.) The program will then:
1. Add the two amounts
2. Print out the answer in a human readable format, with a euro sign and decimal point between the euro and cent of the amount 

## Week 03 Task: accounts.py
This program reads in an alpha-numeric account number, and outputs the account number with only the last 4 digits showing (and the preceding digits replaced with Xs).
- If the account number has 4 digits or fewer, it is output without obfuscation.

## Week 04 Task: collatz.py
This program asks the user to input any positive integer, then repeats two simple arithmetic operations on this number, after the manner of the Collatz conjecture. If the number is even it is divided by two, if it is odd it is multiplied by three and 1 is added. The program ends if/when the current value reaches 1. 
- this program performs some simple checks on the user input; if the input is not a positive integer, it requests another input.
- future development proposed: (1) allow user to enter a special string to stop the program? (2) count the number of steps the integer takes to reach 1? (3) compare this result to nearby integers?

## Week 05 Task: weekday.py
This program outputs whether or not today (at the time of running) is a weekday. There is no user input.
I used the isoweekday() function in this program because it's my personal preference, and also because of my abiding love and respect for the [International Organization for Standardization](https://www.iso.org/home.html). It also made the coding easier.

Expected output if called on Monday through Friday:
```
$ python weekday.py 
Yes, unfortunately today is a weekday.
```
Expected output if called on Saturday or Sunday:
```
$ python weekday.py 
It is the weekend, yay!
```

## Week 06 Task: squareroot.py
This program takes a positive floating-point number as input and outputs an approximation of its square root, using a custom sqrt() function, as an exercise in creating functions. 
- The custom sqrt() function uses Newton's method of finding square roots. This is an iterative process where each step gives a result that is closer to the true answer. Given a positive number $a$, for which you want to find the square root, and given a starting approximate value of the root $x_n$, the iteration is given by:


$$
x_{n+1}= \frac{1}{2} \left({x_n + \frac{a}{x_n}}\right)
$$

 - Stopping the loop: Initially I ran the interation loop 100 times, but this is often unnecessary. Ideally I would like the loop to stop when it has found the correct answer, but because the comparison of floats can be inexact, the loop may not ever stop. So, I added a parameter to the sqrt() function that indicates how close to the true answer the calculated answer must be to be considered 'correct' and end the loop. 

- considerations: how to get the start value?

Comparing Floats: https://www.geeksforgeeks.org/comparing-floating-points-number-for-almost-equality-in-python/

Newton's method: https://en.wikipedia.org/wiki/Newton%27s_method#Examples

LaTeX formatting references: https://code.visualstudio.com/docs/languages/markdown and https://www.upyesp.org/posts/makrdown-vscode-math-notation/


# Week 07 Task: count_es.py
>Instructions: Write a program that reads in a text file and outputs the number of e's it contains. Think about what is being asked here, document any assumptions you are making.  
>The program should take the filename from an argument on the command line. I have not shown you how to do this, you need to look it up.  
>Marks will be given for dealing with errors eg no argument, filename that does not exist, or is not a text file.

Txt files for development were downloaded from [Project Gutenberg](www.gutenberg.org), these text files have been added to `.gitignore` so they will not be pushed to GitHub.

Tutorial on passing command-line arguments to a Python program: https://www.tutorialspoint.com/python/python_command_line_arguments.htm


# Week 08 Task: plottask.py
>Instructions: Write a program called plottask.py that displays:
>    a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
>   and a plot of the function  h(x)=x3 in the range 0 to 10, 
>on the one set of axes.
>Some marks will be given for making the plot look nice (legend etc).
>Please put a copy of the image of the plot (.png file) into the repository

The NumPy documentation states that the RandomState function used in lectures has been superseded by the Generator method.
The method to generate the normally-distributed datapoints for this program was taken from https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.normal.html



# Notes on git commit messages
I have not consistently used any particular git commit message convention in these weekly tasks, but I am slowly starting to incorporate the advice from the sources below. 

There are many, **many** articles and blog posts on what comprises a 'good' Git commit message:
 - [freeCodeCamp(2019): How to Write Good Commit Messages: A Practical Git Guide](https://www.freecodecamp.org/news/writing-good-commit-messages-a-practical-guide/)
 - [Kelvin Romero @Medium(2023): Writing good commit messages](https://kelvinromero.medium.com/writing-good-commit-messages-527679b1babb)
 - [Hashnode(2019): Which commit message convention do you use at work?](https://hashnode.com/post/which-commit-message-convention-do-you-use-at-work-ck3e4jbdd00zyo4s1h7mc7e0g)
 - [Tim Pope(2008): A Note About Git Commit Messages](https://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html)

Common advice from these writers include:
 - separate subject line (concise, approx 50 characters) and optional body text (longer description)
 - ["Atomic Commits"](https://sparkbox.com/foundry/atomic_commits_with_git), i.e. each commit repesents one small, complete, independent chunk of work. This chunk should be large enough to contain a complete change, ideally with the codebase working both before and after the change, and also small enough that it can be described/understood easily and it represents only one change. If multiple changes are represented in one commit, it would be more difficult to track the history of the changes or their separate effects on the code. 
  - Using the imperative tense of verbs. This convention seems to be a combination of (a) in English, verbs in this tense are usually shorter than in other tenses, (b) Git itself uses the imperative when it creates messages, so you might as well match. 

 Many people explicitly follow the [Conventional Commits](https://www.conventionalcommits.org/en/about/) standard. This is a very detailed standard which is designed to allow the use of automated tools to parse and analyse the commit history. The full standard is not useful for me at this time, but one prominent feature which I have begun to use is the inclusion of a keyword at the start of each commit message to indicate the type of change, e.g.:
 - feat: add a new feature
 - fix: fix a bug
 - docu: amend documentation

 This is useful when looking back at past changes in the log, and it also reinforces the practice of only doing one type of change in each commit. 
