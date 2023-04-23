"""
-------
process_files.py
-------
This module processes input file containing Prefix expressions and outputs formatted text file with converted
Postfix expressions via "process_files" function
"""

from typing import TextIO
from Lab2 import conv_prefix
from Lab2 import check_errors


def process_files(input_file: TextIO, output_file: TextIO, build_tree=False) -> None:

    """
    Accepts an input file containing prefix expressions and writes converted postfix expressions to an output file.
    :param input_file: '.txt' text file containing the Prefix expressions
    :param output_file: '.txt' text file output containing the conversion results from Prefix to Infix and Postfix
    :param build_tree: boolean True or False. True indicates converting prefix to postfix by building and traversing
     an expression tree. False indicates using direct recursion to convert to postfix.
    """

    char_str = ""  # Initialize empty string to store full prefix expression
    is_int_exp = False  # Is an integer prefix expression - initialized to False by default

    with input_file as opened_file:

        if build_tree is False:
            output_file.write('PREFIX TO POSTFIX CONVERTER USING RECURSION\n')
            output_file.write('===========================================\n\n')

        elif build_tree is True:
            output_file.write('PREFIX TO POSTFIX CONVERTER USING EXPRESSION TREE\n')
            output_file.write('=================================================\n\n')

        while True:
            char = opened_file.read(1)
            if not char:
                break
            else:
                if char != '\n' and char != '\t' and char != '\r':  # Keep reading Prefix characters on a single line
                    if char != " " and char != "":
                        if char.isdigit():
                            is_int_exp = True
                        # Replace '$' with '^' for all exponentiation for evaluating mathematical expressions
                        if char == '^':  # replace '^' with '$' otherwise
                            char = '$'

                        char_str += char

                elif char == '\n' or char == '\r':  # End of prefix expression on a single line

                    if char_str != "":
                        output_file.write("PREFIX INPUT: ")
                        output_file.writelines(char_str)

                        # Check for prefix expression errors
                        valid = check_errors.is_valid_expr(char_str, output_file, is_int_exp, build_tree)

                        # Process Prefix to Postfix using recursion
                        process_recursion(char_str, valid, build_tree, is_int_exp, output_file)

                    # Re-initialize character string and integer detection for new prefix input
                    char_str = ""
                    is_int_exp = False


def process_recursion(char_str, valid: bool, build_tree: bool, is_int_exp: bool, output_file: TextIO) -> None:
    """
    Function to recursively process prefix expression string to postfix using direct recursion or via expression tree.
    If integer prefix expression, mathematical result is returned.
    :param char_str: Prefix expression string
    :param valid: Whether prior Prefix expression errors detected
    :param build_tree: Whether an expression tree is to be used
    :param is_int_exp: Whether Prefix expression is an integer expression
    :param output_file: Output file to write results
    :return: None
    """
    # Prefix expression is valid - evaluate Postfix using direct recursion
    if valid is True and build_tree is False:

        # Non-Integer Prefix Expression. Convert prefix to postfix using recursion
        if is_int_exp is False:
            out_str, index = conv_prefix.pre_post_rec(char_str)
            # If lengths of input and output strings are equal, recursion processed all characters,
            # otherwise recursion was terminated before processing entire string
            if len(char_str) == len(out_str):
                output_file.writelines("\nPOSTFIX(rec): " + out_str)
                output_file.write('\n\n')
            else:  # Recursion could not process fully due to error in positioning of operator
                output_file.writelines("\nInvalid expression! Each operator must have 2 operands"
                                       " to process throughout recursion")
                output_file.write('\n\n')

        # If prefix expression is an operation on integers (only), evaluate mathematical result recursively
        elif is_int_exp is True:
            result, index = conv_prefix.eval_pre_rec(char_str)
            output_file.writelines("\nRESULT: " + result)
            output_file.write('\n\n')

    # Prefix expression is valid - evaluate Postfix by building and traversing expression tree
    elif valid is True and build_tree is True:
        # Build expression tree from prefix expression using recursion
        tree, expr, index = conv_prefix.build_exp_tree(char_str)
        output_file.writelines("\nPOSTFIX(from traversing exp. tree): ")
        # Use post-order traversal to obtain Postfix expression
        output_file.writelines(conv_prefix.trv_postfix(tree, postfix_str=[]))
        print('\n')
        output_file.write('\n\n')




