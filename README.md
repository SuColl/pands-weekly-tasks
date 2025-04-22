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
- The custom sqrt() function uses Heron's method of calculating square roots, which is equivalent to Newton's method of finding square roots. This is an iterative process where each step gives a result that is closer to the true answer. Given a positive number $a$, for which you want to find the square root, and given a starting approximate value of the root $x_n$, the iteration is given by:


$$
x_{n+1}= \frac{1}{2} \left({x_n + \frac{a}{x_n}}\right)
$$

- considerations: how to get the start value? how many iterations to do, how to know if you're close enough?

(LaTeX formatting references: https://code.visualstudio.com/docs/languages/markdown and https://www.upyesp.org/posts/makrdown-vscode-math-notation/)