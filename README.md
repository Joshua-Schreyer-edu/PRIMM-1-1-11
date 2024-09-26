# PRIMM: 1+1 = 11?

## Predict
Answer the following questions *without running the repo**.

1. What does this program output?
    > The program outputs an equation of the sum of two numbers inputted by the user.

2. If the user intended on outputting the sum of two numbers, does this program accomplish the purpose? Why/why not?
    > Yes, because the program outputs the sum of two numbers. It also outputs the equation used to calculate the sum.

## Run
Run the program. 

1. What does the program output. Refer to what numbers you entered and what you got back.
    > I entered "4" and "7".
    > I got back "47".


## Investigate
1. Add a single-line comment above each major chunk of code to explain what is happening.
2. Read about the concept of [string concatenation](https://www.w3schools.com/python/gloss_python_string_concatenation.asp). Explain in your own words below what it is and how it relates to this program.
    > String concatenation is the conjoining of two or more strings. It relates to this program because the two numbers are concatenated, not added.

3. Read about the [`int()`](https://www.w3schools.com/python/ref_func_int.asp) and [`float()`](https://www.w3schools.com/python/ref_func_float.asp) functions in Python. What do they do? How can they help this program?
    > They convert a value(in the form of a string) to the given data type in respect to the function(`float()` converts it to a floating point number).
    > They can help with the program because the value received by the user from the `input()` function is a string, and these can convert them to integers or floating point numbers.

## Modify
1. Change the program using what you learned so that it adds two numbers you enter.
2. Try entered a non-numeric value. What happens? What kind of error is this (refer to our error types).
    > The program errors out.
    > The error is a runtime error, because the code is syntaxically correct, but you cannot convert a string(like "hello world") to an integer.

## Make
1. Add more lines of code to perform other math operations with the numbers you entered and print out the results. Try the following operators. 
    - `-`
    - `*`
    - `**`
    - `/`
    - `//`
    - `**`
    - `%`

2. Can you figure out what they do without looking them up? You might need to enter multiple numbers to figure it out. Fill in the table below.

| Operator | Meaning |
|  :---:    |   :---:   |  
|   `+`    | Addition |
|   `-`    | Subtraction |
|   `*`    | Multiplication |
|   `/`    | Division |
|   `//`    | Division rounded down if decimal |
|   `**`    | Exponent(to the power of __) |
|   `%`    | Modulus(remainder of division) |

