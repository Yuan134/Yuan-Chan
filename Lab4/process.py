"""
----------
process.py
----------
This module processes an input file containing a series of numbers and produces an output file containing
the numbers sorted using a series of various Sort functions
"""

from typing import TextIO
from pathlib import Path


def process_files(input_file: TextIO):
    """
    Accepts an input file of a vertical list of integers and writes the sorted output using various sort functions
    :param input_file: '.dat' text file containing the random, reversed, ascending and random with duplicate number sets
    :param output_file: '.dat' text file output.........
    :param input_file: input text file containing the sequence of integers to be sorted in '_ccy.dat' format
    :return: num_array: an array of numbers to be sorted
    """
    # Initialize empty lists and strings
    num_array = []  # This will hold the character strings read line by line
    char_str = ""  # character string to hold each number read by line

    with input_file as opened_file:
        while True:
            char = opened_file.read(1)
            if not char:
                break
            else:
                if char != '\n' and char != '\t' and char != '\r':  # Keep reading characters on a single line
                    if char != " " and char != "":
                        if char.isdigit():
                            char_str += char

                # End of prefix expression on a single line
                elif char == '\n' or char == '\r':
                    num_array.append(int(char_str))
                    char_str = ""

    return num_array





