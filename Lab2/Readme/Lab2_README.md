# Lab 2 Project

Author: Chih Yuan Chan ID: 28A8CA

Contact email: cchan64@jh.edu

## 1. Overview:

This project implements a Prefix to Postfix expression converter using recursion.

The program accepts a user input text file containing Prefix expressions.

An output text file is produced displaying the converted Postfix expression and any caught errors.

The Python program will be executed from the command line interface (terminal).

Enhancements:

- Integer prefix expressions will be evaluated to return the mathematical result.
- For demonstrative purposes, users can elect to process Prefix to Postfix by building an expression tree and traversing 
  the tree. "-t" or "--tree" to be nominated on the command line (see "Running Lab2" below). Identical output to direct 
  recursive approach demonstrates the equivalence of both approaches. 


## 2. Running Lab2:

1. Download and install Python on your computer
2. Navigate to [this](.) directory (containing the README.md)
3. Run the program as a module: `python -m Lab2`. 
4. Run the program as a module (with real inputs): `python -m Lab2 [-h] [-t] <some_input_file> <some_output_file>`
   (i.e `python -m Lab2 resources\input\Input.txt resources\output\output.txt`)


```commandline
usage: python -m Lab2 [-h] [-t] in_file out_file

positional arguments:
  in_file     Input File Pathname
  out_file    Output File Pathname

optional arguments:
  -h, --help  show this help message and exit
  -t, --tree  build expression tree and traverse tree to process prefix to postfix
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
- 'Input.txt':  This is the standard input text file provided for the lab
- 'Input_alternative1.txt':  This is an alternative input file to demonstrate additional edge cases handling
- 'Input_alternative2.txt':  This is an alternative input file containing integer prefix expressions only. (NOTE: 
   This input file can only be processed by direct recursion i.e. "-t" or "--tree" expression tree option is NOT 
   permitted.)
- 'Input_blank.txt':  This is a blank file to demonstrate IO exception handling for blank files

Enter 1 x Prefix expression per line in the input files with '\n' to indicate a new line. 

Whitespace may be entered but will be ignored in the interpretation of the Prefix expression.

Output will be written to the user specified output file after processing the input file.

Output files:
- 'Output.txt':   Output text file based on 'Input.txt' by direct recursion per standard lab requirement
- 'Output1.txt':   Alternative output text file using 'Input_alternative1.txt' to demonstrate 
   additional edge case handling using direct recursion
- 'Output2.txt':   Alternative output text file using 'Input_alternative2.txt' to demonstrate 
  evaluation of integer expression using direct recursion
- 'Output_tree.txt':   Output text file based on 'Input.txt' using expression tree
- 'Output_tree_1.txt':   Output text file for 'Input_alternative1.txt' to show edge case handling using expression tree

## 4. Prefix expression formatting:

Valid Prefix expressions are to only include:
- mathematical operators 
  (+ : addition,  - : subtraction,  * : multiplication,  / : division,  $ or ^ : exponentiation)
- Note: '^' operators will be substituted with '$' exponentiation in the output file
- integer and alphabetical operands (lower and upper case supported). Note: Multi-digit integers are to be enclosed 
  within brackets eg. '(31)' represents a single integer 31 whereas '31' represents 2 separate integers 3 and 1 

The following Prefix expression errors are accounted for:
- Illegal characters: These are characters that are not valid operators or operands
- First and last characters: First character must be a valid operator and last character must be a valid operand
- Incorrect operators: Number of operators must be one less than the number of operands

## 5. Project Package Layout:

* [Lab2/](.): The parent or "root" folder containing all of these files. 
    * [README.md](README.md):
      The guide you're reading. 
    * [Lab2](process_files.py): 
      This is a *module* in the *package*. There are 5 modules in total:
      * [`__init__.py`](Lab2/__init__.py) 
        This file is used to expose what functions, variables, classes, etc are exposed when scripts import this module. 
      * [`__main__.py`](Lab2/__main__.py) 
        This file is the entrypoint to the program. It handles command line arguments
      * `process_files.py` 
        This module processes input file containing Prefix expressions and outputs formatted text file in Postfix + 
        error messages
      * `check_errors.py` 
        This module contains various error checking functions used to ensure that the input Prefix expression is correct
      * `convert_prefix.py` 
        This module contains all Prefix to Postfix conversion functions
      



