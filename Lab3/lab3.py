"""
-------
lab3.py
-------
This module processes input files to obtain output for Huffman encoding/decoding

Functions:
    process_freq_table: Processes input Frequency Table text and converts to Huffman Frequency Table
    build_custom_frequency_table: Constructs customized Huffman Frequency Table for input custom source text file
    process_clear_text: Parses input clear text file and returns a list of clear text expressions
    process_encoded_text: Parses encoded text file and returns a list of Huffman encoded binary strings
"""

from typing import TextIO
from Lab3.minheap import heap_node
import sys
from sys import stderr


def process_freq_table(in_freq_file: TextIO, output_file: TextIO, enhanced=False):
    """
    Processes input Frequency Table text and converts to Huffman Frequency Table containing minimum heap nodes
    :param in_freq_file: input file containing Frequency Table text
    :param output_file: output file containing converted Huffman Frequency Table
    :param enhanced: Boolean toggle (True/False) for enhanced mode "OFF" or "ON"
    :return: huff_freq_table: Huffman Frequency Table containing minimum heap nodes
    """

    # Initialized variables / counters
    frequency_char = ""
    huff_freq_table = []  # Stores Huffman heap nodes
    char_counter = 0  # Counts the number of characters advanced at the start of each new line
    line_counter = 1  # Counter to track the line number of the processed input text file
    error_str_list = []  # List to store error messages

    with in_freq_file as opened_file:

        while True:
            char = opened_file.read(1)
            if not char:
                break
            else:
                if char != '\n' and char != '\t' and char != '\r':  # Keep reading Prefix characters on a single line
                    char_counter += 1
                    if char_counter == 1:
                        char_symbol = char  # Only the first character is read as the key symbol
                    # If enhanced mode is disabled, only alphanumeric characters will be read, whitespace and
                    # other characters will be skipped
                    if char_counter == 1 and enhanced is False and char_symbol.isalpha() is False:
                        # Non-alphabetical symbols not permitted
                        error_str = ("Error! Non-alphabetical character '" + char_symbol + "' detected on line: "
                                     + str(line_counter) + " of input frequency file\n")
                        error_str_list.append(error_str)

                    # All other digits after the first character on each line will be concatenated into frequency value
                    if char.isdigit():
                        frequency_char += char

                elif char == '\n' or char == '\r':  # Finished reading line

                    # Catch zero or missing frequency values
                    if frequency_char == "" or frequency_char == '0':
                        error_str = ("Error! 0 or blank is not permitted for frequency value on line: "
                                     + str(line_counter) + " of input frequency file\n")

                        error_str_list.append(error_str)

                    # Instantiate Huffman minimum heap node with character symbol and corresponding frequency value
                    node = heap_node(char_symbol, int(frequency_char))

                    # Add to Huffman frequency table
                    huff_freq_table.append(node)

                    # Re-initialize variables and counters for new line input
                    frequency_char = ""
                    line_counter += 1
                    char_counter = 0

        if len(error_str_list) > 0:  # Errors in file input detected

            for i in range(len(error_str_list)):
                output_file.write(error_str_list[i])
            output_file.write("\nProgram exited without completing processing")
            print("Error in input frequency file format - Refer output file for error log.", file=stderr)
            sys.exit()

    return huff_freq_table


def build_custom_frequency_table(in_path: str, out_path: str):
    """
    Constructs customized Huffman Frequency Table for input custom source text file
    :param in_path: input file path containing custom source text file
    :param out_path: output file path containing customized Huffman Frequency Table
    :return: custom_freq_table: Customized Huffman Frequency Table (in Dictionary format)
    """
    custom_freq_table = {}  # Initialize dictionary to store Huffman Frequencies

    try:
        with in_path.open('r') as input_file, out_path.open('w') as output_file:

            while True:
                char = input_file.read(1)
                if not char:
                    break
                else:
                    # Store all unique character symbols as dictionary keys and record corresponding frequencies
                    if char not in custom_freq_table:
                        custom_freq_table[char] = 1
                    else:
                        custom_freq_table[char] += 1

            # Sort dictionary according to keys
            custom_freq_table = dict(sorted(custom_freq_table.items()))

            # Create custom Frequency Table text file
            for keys in custom_freq_table:
                output_file.write(keys + " - " + str(custom_freq_table[keys]) + "\n")

    # File path error
    except FileNotFoundError:
        print('Input file does not exist in supplied path: ', in_path, file=stderr)

    return custom_freq_table


def process_clear_text(in_clear_text_file: TextIO, output_file: TextIO, enhanced=False):
    """
    Parses input clear text file and returns a list of clear text expressions to be processed using Huffman encoding
    :param in_clear_text_file: Clear Text File input
    :param output_file: Output file containing Huffman encoding / decoding output
    :param enhanced: Boolean toggle (True/False) for enhanced mode "OFF" or "ON"
    :return: expr_list: List containing Clear Text expression strings - to be processed by Huffman encoding function
    """

    # Initialized variables / counters
    expr_list = []  # List to store clear text expression strings
    expr_str = ""  # Clear text expression strings
    line_counter = 1  # Counter to track the line number of the processed input text file
    warning_counter = True  # Toggle to determine if warning message should be printed
    # Store non-alphabetical characters in dictionary (for non-enhanced mode only) to output as warning message
    non_alpha_chars = {}

    with in_clear_text_file as opened_file:

        while True:
            char = opened_file.read(1)
            if not char:
                break
            else:
                if char != '\n' and char != '\t' and char != '\r':  # Keep reading Prefix characters on a single line
                    # Non-alphabet characters not permitted in non-enhanced mode
                    if enhanced is False and char.isalpha() is False:
                        # Record illegal characters and frequencies in dictionary
                        if char in non_alpha_chars:
                            non_alpha_chars[char] += 1
                        else:
                            non_alpha_chars[char] = 1
                        if warning_counter is True:  # Only print warning message once if illegal characters detected
                            output_file.write("\n<<WARNING: Non-alphabetical characters detected " +
                                              "in CLEAR TEXT file and have been IGNORED in non-enhanced mode.>>" + "\n")
                            warning_counter = False  # Re-set counter to suppress repeated warning messages

                    if enhanced is False:
                        if char.isalpha():  # process alphabetical characters for standard non-enhanced mode
                            expr_str += char
                    elif enhanced is True:  # all characters permitted for enhanced mode "ON"
                        expr_str += char
                elif char == '\n' or char == '\r':
                    # end of line - reset variables / counters
                    line_counter += 1
                    expr_list.append(expr_str)
                    expr_str = ""

        for key in non_alpha_chars.keys():  # Output detected non-alphabetical characters for warning message
            output_file.write("Non-Alphabetical Character: '" + key + "' Occurrences: " +
                              str(non_alpha_chars[key]) + "\n")

    return expr_list


def process_encoded_text(in_encoded_file: TextIO, output_file: TextIO):
    """
    Parses encoded text file and returns a list of binary strings to be processed using Huffman decoding
    :param in_encoded_file: encoded binary string input file
    :param output_file: Output file containing Huffman encoding / decoding output
    :return: digit_list: List containing encoded binary expression strings to be processed by Huffman decoding
    """
    digit_list = []  # List containing encoded Huffman binary expression strings
    digit_str = ""  # Huffman encoded binary string
    warning_counter = True  # Counter to print warning message
    non_binary_chars = {}  # Dictionary to store illegal non-binary characters

    with in_encoded_file as opened_file:

        while True:
            char = opened_file.read(1)
            if not char:
                break
            else:
                if char != '\n' and char != '\t' and char != '\r':  # Keep reading Prefix characters on a single line
                    if char != "1" and char != "0":  # Non-binary characters detected
                        # Record illegal character and frequency in dictionary
                        if char in non_binary_chars:
                            non_binary_chars[char] += 1
                        else:
                            non_binary_chars[char] = 1

                        if warning_counter is True:  # if illegal characters detected
                            output_file.write("\n<<WARNING: Only binary characters (0/1) are read." +
                                              " Non-binary characters detected in clear text file" +
                                              " and have been" + "\nIGNORED in non-enhanced mode.>>" + "\n")
                            warning_counter = False  # Print warning message once only - reset counter
                    if char.isdigit():  # Concatenate legal binary characters
                        digit_str += char

                elif char == '\n' or char == '\r':  # End of line, add binary string to list
                    digit_list.append(digit_str)
                    digit_str = ""  # Re-initialize binary expression string to store upcoming new string

        for key in non_binary_chars.keys():  # Output illegal characters and occurrences to file
            output_file.write("Non-Binary Character: " + key + " Occurrences: " + str(non_binary_chars[key]) + "\n")
        output_file.write("\n")

    return digit_list
