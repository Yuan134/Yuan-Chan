"""
-----------
__main__.py
-----------
- Executes file input and output via "process_files" function
- Initializes argument parser for terminal entry of input and output file paths
- Provides exception handling for file IO
"""
import sys
from Lab2.process_files import process_files
from pathlib import Path
from sys import stderr

import argparse

arg_parser = argparse.ArgumentParser()
# Argument to accept input file path
arg_parser.add_argument("in_file", type=str, help="Input File Pathname")
# Argument to accept output file path
arg_parser.add_argument("out_file", type=str, help="Output File Pathname")
# Argument '--tree' (optional) to accept option to build expression tree
arg_parser.add_argument('-t', '--tree', action='store_true', help='Convert prefix to postfix using expression tree')

args = arg_parser.parse_args()

# User input file paths for input and output text files
in_path = Path(args.in_file)
out_path = Path(args.out_file)

try:
    with in_path.open('r') as input_file, out_path.open('w') as output_file:

        # Incorrect input and output file type exception
        if in_path.suffix != '.txt':
            print('Error! Incorrect input file type. Supplied file type:', in_path.suffix,
                  ' Required file type: .txt', file=stderr)
            sys.exit()
        if out_path.suffix != '.txt':
            print('Error! Incorrect output file type. Supplied file type:', out_path.suffix,
                  ' Required file type: .txt', file=stderr)
            sys.exit()

        # Empty file exception
        elif in_path.stat().st_size == 0:
            print("Error! File is empty!", file=stderr)
            sys.exit()

        if args.tree:  # Convert to Postfix using an expression tree
            process_files(input_file, output_file, build_tree=True)
        else:  # Convert to Postfix without an expression tree - direct recursion
            process_files(input_file, output_file, build_tree=False)

# File path error
except FileNotFoundError:
    print('Input file does not exist in supplied path: ', in_path, file=stderr)