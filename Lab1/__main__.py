"""
-----------
__main__.py
-----------
- Executes file input and output via "process_files" function
- Initializes argument parser for terminal entry of input and output file paths
- Provides exception handling for file IO
"""
import sys
from Lab1.lab1 import process_files
from pathlib import Path
from sys import stderr

import argparse

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("in_file", type=str, help="Input File Pathname")
arg_parser.add_argument("out_file", type=str, help="Output File Pathname")
args = arg_parser.parse_args()


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

        process_files(input_file, output_file)

# File path error
except FileNotFoundError:
    print('Input file does not exist in supplied path: ', in_path, file=stderr)
