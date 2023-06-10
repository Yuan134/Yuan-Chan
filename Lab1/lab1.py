"""
-------
lab1.py
-------
This module processes input file containing Prefix expressions and outputs formatted text file with converted
Infix / Postfix expressions via "process_files" function
"""

from typing import TextIO
from Lab1 import LLstack
from Lab1 import check_errors
from Lab1 import prefix_convert


def process_files(input_file: TextIO, output_file: TextIO) -> None:

    """
    :param input_file: '.txt' text file containing the Prefix expressions
    :param output_file: '.txt' text file output containing the conversion results from Prefix to Infix and Postfix
    """

    # char_stack: Empty character stack for Prefix expression; order of expression will be reversed (right to left)
    # char_list: Empty character list to compile the Prefix expression read conventionally left to right
    char_stack = LLstack.Stack()
    char_list = []

    with input_file as opened_file:

        output_file.write('PREFIX TO POSTFIX (AND INFIX) CONVERTER\n')
        output_file.write('=======================================\n\n')

        while True:
            char = opened_file.read(1)
            if not char:
                break
            else:
                if char != '\n' and char != '\t' and char != '\r':  # Keep reading Prefix characters on a single line
                    if char != " " and char != "":
                        if char == '^':  # Replace '^' with '$' for all exponentiation
                            char = '$'
                        char_stack.push(char)
                        char_list += char

                elif char == '\n' or char == '\r':  # End of prefix expression on a single line

                    if not char_stack.is_empty():
                        output_file.write("PREFIX INPUT: ")
                        output_file.writelines(char_list)
                        # Check for prefix expression errors
                        valid = check_errors.is_valid_expr(char_stack, output_file)

                        if valid is True:  # Prefix expression does not contain errors
                            output_file.write("\nINFIX OUTPUT: ")
                            s_infix = prefix_convert.prefix_to_infix(char_stack)  # Convert prefix to infix
                            s_infix.print_stack(output_file)

                            output_file.write("\nPOSTFIX OUTPUT: ")
                            s_postfix = prefix_convert.prefix_to_postfix(char_stack)  # Convert prefix to postfix
                            s_postfix.print_stack(output_file)
                            output_file.write('\n\n')

                    # Re-initialize all stacks and lists to receive new line input
                    char_stack = LLstack.Stack()
                    char_list = []
