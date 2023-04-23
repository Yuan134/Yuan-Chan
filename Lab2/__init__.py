"""
------------
Lab2 package
------------
Modules:
  __main__.py:          Entry point to convert Prefix to Postfix
  process_files.py:     Accepts input text file containing Prefix; Outputs text file with Postfix + errors
  check_errors.py:      Contains various functions to check the correct formatting of the Prefix expression
  conv_prefix.py:       Contains conversion functions from prefix to postfix using:
                        1) direct recursion 2) recursively traversing an expression tree
"""
from Lab2.process_files import process_files  # process_files: main function to process input and output files
