# Lab 1 Project

Author: Chih Yuan Chan ID: 28A8CA

Contact email: cchan64@jh.edu

## 1. Overview:

This project implements a Prefix to Postfix and Prefix to Infix expression converter using a Stack ADT.

The Stack ADT is itself implemented using a Singly-Linked-List.

The program accepts a user input text file containing Prefix expressions.

An output text file is produced displaying the converted Postfix expression and any caught errors.

The Python program will be executed from the command line interface (terminal).


## 2. Running Lab1:

1. Download and install Python on your computer
2. Navigate to [this](.) directory (containing the README.md)
3. Run the program as a module: `python -m Lab1 -h`. This will print the help message.
4. Run the program as a module (with real inputs): `python -m Lab1 <some_input_file> <some_output_file>`
   a. IE: `python -m Lab1 resources/input/input.txt output.txt`

```commandline
usage: python -m Lab1 [-h] in_file out_file

positional arguments:
  in_file     Input File Pathname
  out_file    Output File Pathname

optional arguments:
  -h, --help  show this help message and exit
```

Usage statements are very formalized

| Symbol        | Meaning                                                                                                            |
|---------------|--------------------------------------------------------------------------------------------------------------------|
| [var]         | variable var is optional.                                                                                          |
| var           | variable var is required. All positional arguments are required.                                                   |
| -v, --version | This refers to a flag. One dash + one letter OR two dashes and a whole word. Some flags take one or more arguments |
| +             | This argument consumes 1 or more values                                                                            |
| *             | This argument consumes 0 or more values                                                                            |

## 3. Input and Output files:

Both input and output files are to be in .txt format only

Input files:
- 'input.txt' (This is the standard input text file provided for the lab)
- 'input_alternative.txt' (This is an alternative input file to demonstrate additional edge cases handling)
- 'input_blank.txt' (This is a blank file to demonstrate IO exception handling for blank files)

Enter 1 x Prefix expression per line in the input files with '\n' to indicate a new line. 

Whitespace may be entered but will be ignored in the interpretation of the Prefix expression.

Output will be written to the user specified output file after processing the input file.

## 4. Prefix expression formatting:

Valid Prefix expressions are to only include:
- mathematical operators 
  (+ : addition,  - : subtraction,  * : multiplication,  / : division,  $ or ^ : exponentiation)
- Note: '^' operators will be substituted with '$' exponentiation in the output file
- alphabetical operands (lower and upper case supported)

The following Prefix expression errors are accounted for:
- Illegal characters: These are characters that are not valid operators or operands
- First and last characters: First character must be a valid operator and last character must be a valid operand
- Incorrect operators: Number of operators must be one less than the number of operands

## 5. Project Package Layout:

* [Lab1/](.): The parent or "root" folder containing all of these files. 
    * [README.md](README.md):
      The guide you're reading. 
    * [Lab1](lab1): 
      This is a *module* in the *package*. There are 6 modules in total:
      * [`__init__.py`](Lab1/__init__.py) 
        This file is used to expose what functions, variables, classes, etc are exposed when scripts import this module. 
      * [`__main__.py`](Lab1/__main__.py) 
        This file is the entrypoint to the program. It handles command line arguments
      * `lab1.py` 
        This module processes input file containing Prefix expressions and outputs formatted text file in Postfix + error messages
      * `LLstack.py` 
        This module contains the Stack class and the Node class used for the singly linked list implementation
      * `check_errors.py` 
        This module contains various error checking functions used to ensure that the input Prefix expression is correct
      * `prefix_convert.py` 
        This module contains the Prefix to Postfix and Prefix to Infix conversion functions
      



