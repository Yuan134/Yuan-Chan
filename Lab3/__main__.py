"""
-----------
__main__.py
-----------
- Executes file input and output
- Run with either 'enhanced_off' mode or 'enhanced_on' mode
- 'enhanced_off': Standard mode only allows upper case alphabets in Huffman encoding characters; no symbols / whitespace
- 'enhanced_on': Enhanced mode allows upper/lower case alphabets, symbols (including punctuation and whitespace)
- Initializes argument parser for terminal entry of input and output file paths
- Provides exception handling for file IO via "check_input_file" and "check_output_file" functions

Functions:
    check_input_file: checks and validates input files and input file paths
    check_output_file: checks and validates output files and output file paths
    process_huffman_encoding: executes processes to obtain huffman encoding / decoding

"""
import sys
from Lab3.lab3 import *
from Lab3.minheap import *
from pathlib import Path
from sys import stderr

import argparse

arg_parser = argparse.ArgumentParser()
# Subparser to enable enhanced mode to be toggled 'ON' or 'OFF'
arg_subparser = arg_parser.add_subparsers(dest='command', help='Select Enhanced mode(on/off)')

enhanced_off = arg_subparser.add_parser('enhanced_off', help='Enhanced mode off')
enhanced_on = arg_subparser.add_parser('enhanced_on', help='Enhanced mode on')

# CLI arguments for enhanced mode "OFF" - this is the standard operation without enhancements
# Input file paths
enhanced_off.add_argument("in_freq_file", type=str, help="Frequency Table File Input Pathname")
enhanced_off.add_argument("in_clear_text_file", type=str, help="Clear Text File Input Pathname")
enhanced_off.add_argument("in_encoded_file", type=str, help="Encoded File Input Pathname")
# Output file path
enhanced_off.add_argument("out_file", type=str, help="Output File Pathname")

# CLI arguments for enhanced mode "ON" - enhancements enabled
# Input file paths
# "in_custom_text" specifies input file path for custom frequency table text source
enhanced_on.add_argument("in_custom_text", type=str, help="Custom Text File for Custom Frequency Table Input Pathname")
enhanced_on.add_argument("in_clear_text_file", type=str, help="Clear Text File Input Pathname")
enhanced_on.add_argument("in_encoded_file", type=str, help="Encoded File Input Pathname")
# Output file paths
# "custom_freq_table_out_file" specifies output file path for customized frequency table
enhanced_on.add_argument("custom_freq_table_out_file", type=str, help="Custom Frequency Table Output File Pathname")
enhanced_on.add_argument("out_file", type=str, help="Output File Pathname")

args = arg_parser.parse_args()


def check_input_file(in_file_path: str) -> None:
    """
    Verifies input file types, file size and file path
    :param in_file_path: input file path string
    :return: None
    """
    try:
        # Incorrect input file type exception - only .txt files permitted
        if in_file_path.suffix != '.txt':
            print('Error! Incorrect input file type. Supplied file type:', in_file_path.suffix,
                  ' Required file type: .txt', file=stderr)
            sys.exit()

        # Empty file exception
        elif in_file_path.stat().st_size == 0:
            print("Error! File is empty!", file=stderr)
            sys.exit()

    # File path error
    except FileNotFoundError:
        print('Input file does not exist in supplied path: ', in_file_path, file=stderr)


def check_output_file(out_path: str) -> None:
    """
    Verifies output file types and file path
    :param out_path: output file path string
    :return: None
    """
    try:
        # Incorrect output file type exception - only .txt files permitted
        if out_path.suffix != '.txt':
            print('Error! Incorrect output file type. Supplied file type:', out_path.suffix,
                  ' Required file type: .txt', file=stderr)
            sys.exit()

    # File path error
    except FileNotFoundError:
        print('Output file directory does not exist in supplied path: ', out_path, file=stderr)


def process_huffman_encoding(in_freq_file_path, in_clear_text_path, in_encoded_path, out_path, enhanced) -> None:
    """
    Function to process input files to output Huffman encodings / decodings
    :param in_freq_file_path: input file path string for input Frequency Table
    :param in_clear_text_path: input file path string for input Clear Text (to be converted to Huffman encodings)
    :param in_encoded_path: input file path string for input encodings (to be converted to text by Huffman decoding)
    :param out_path: output file path for output results text file
    :param enhanced: boolean toggle (True/False) for enhancements 'OFF' or 'ON'
    :return: None
    """
    with in_freq_file_path.open('r') as input_file1, in_clear_text_path.open('r') as input_file2, \
            in_encoded_path.open('r') as input_file3, out_path.open('w') as output_file:

        # Verify input and output files / file paths
        check_input_file(in_freq_file_path)
        check_input_file(in_clear_text_path)
        check_input_file(in_encoded_path)
        check_output_file(out_path)

        # Process frequency tables to obtain Huffman Encoding frequency table
        huff_freq_table = process_freq_table(input_file1, output_file, enhanced=enhanced)
        # Build priority queue minimum heap from frequency table
        huffman_heap = build_heap(huff_freq_table)
        # Build Huffman tree from Huffman minimum heap
        huffman_tree = conv_huff_tree(huffman_heap)
        # Print Huffman tree using Pre-order traversal
        print_preorder(huffman_tree[0], output_file)
        # Obtain corresponding Huffman encoding dictionary for each Huffman frequency table key
        code_dict = get_codes(huffman_tree[0], output_file)

        # Parse input clear text strings
        clear_text_strings = process_clear_text(input_file2, output_file, enhanced=enhanced)
        output_file.write("\nCLEAR TEXT TO ENCODING:\n")
        output_file.write("=======================\n")

        # Convert clear text to Huffman encodings
        for i in range(len(clear_text_strings)):
            encoded_str = huffman_encode(clear_text_strings[i], code_dict, output_file, enhanced=enhanced)
            output_file.write("TEXT: ")
            output_file.write(clear_text_strings[i] + "\n")
            output_file.write("ENCODING: ")
            output_file.write(encoded_str + "\n")
            # Determine amount of compression obtained using Huffman encoding vs ASCII encoding (8 bits per character)
            output_file.write("BEFORE HUFFMAN COMPRESSION: No. of Characters = " + str(len(clear_text_strings[i])) +
                              "; No. of ASCII Bits = " + str(len(clear_text_strings[i]) * 8) + "\n")
            output_file.write("AFTER HUFFMAN COMPRESSION: No. of Bits = " + str(len(encoded_str)) + "\n")
            # Percentage compressed is the difference between the number of Huffman encoded and un-encoded ASCII
            # character bits (8 per character) divided by the number of un-encoded ASCII character bits
            output_file.write("% COMPRESSED: " + str(round((len(clear_text_strings[i]) * 8 - len(encoded_str))
                                                           / (len(clear_text_strings[i] * 8)) * 100, 1)) + "\n\n")

        # Parse Huffman binary encoding strings
        encoded_strings = process_encoded_text(input_file3, output_file)
        output_file.write("ENCODED TO DECODED TEXT:\n")
        output_file.write("========================")

        # Convert encoded strings into text
        for i in range(len(encoded_strings)):
            decoded_str, tree_path = huffman_decode(encoded_strings[i], huffman_tree)

            output_file.write("\nENCODING: " + encoded_strings[i] + "\n")
            output_file.write("DECODED TEXT: " + decoded_str + "\n")

            # Warning messages if encodings were not successfully processed
            if len(decoded_str) == 0:
                output_file.write("WARNING! Check validity of binary string. String '" +
                                  encoded_strings[i] + "' could not be decoded!\n")
            elif len(tree_path) > 0:
                output_file.write("WARNING! Check validity of binary string. Substring '"
                                  + tree_path
                                  + "' was not completed!\n")


# Driver code run using subparsers for enhanced mode 'OFF' or enhanced mode 'ON'
if args.command == 'enhanced_off':
    # User input file paths for standard mode input and output text files
    in_freq_file_path = Path(args.in_freq_file)
    in_clear_text_path = Path(args.in_clear_text_file)
    in_encoded_path = Path(args.in_encoded_file)
    out_path = Path(args.out_file)

    process_huffman_encoding(in_freq_file_path, in_clear_text_path, in_encoded_path, out_path, enhanced=False)

elif args.command == 'enhanced_on':

    # User input file paths for enhanced mode input and output text files
    freq_table_out_path = Path(args.custom_freq_table_out_file)  # File path for custom frequency table
    in_freq_file_path = Path(args.custom_freq_table_out_file)  # Use same path as output path for the custom freq table
    in_custom_text_path = Path(args.in_custom_text)
    in_clear_text_path = Path(args.in_clear_text_file)
    in_encoded_path = Path(args.in_encoded_file)
    out_path = Path(args.out_file)

    # Build custom frequency table and store into 'freq_table_out_path'
    custom_freq_table = build_custom_frequency_table(in_custom_text_path, freq_table_out_path)

    process_huffman_encoding(in_freq_file_path, in_clear_text_path, in_encoded_path, out_path, enhanced=True)
