# Lab 3 Project

Author: Chih Yuan Chan ID: 28A8CA

Contact email: cchan64@jh.edu

## 1. Overview:

This project performs Huffman encoding and decoding based on a Huffman Frequency Table.
A Huffman Encoding Tree is constructed using a priority queue (minimum heap) to perform encoding / decoding operations

Standard mode ('enhanced_off' - No enhancements): 
- Only uppercase alphabetical characters are accounted for, based on provided Huffman Frequency Table

Enhanced mode('enhanced_on - Enhancements enabled): 
- All characters can be assessed, including upper and lower-case, punctuation and whitespace. 
- Module to build and use a customized Huffman Frequency table using user supplied input source text
- Creates text file containing customized Frequency Table and stores it to user-specified location

## 2. Running Lab3:

1. Download and install Python on your computer
2. Navigate to [this](.) directory (containing the README.md)
3. Run the program as a module: `python -m Lab3`. 
4. Run the program in Standard Mode ('enhanced_off' with real inputs): 
   `python -m Lab3 enhanced_off [-h] <input_file1> <input_file2> <input_file3> <output_file>`
    (i.e `python -m Lab3 enhanced_off resources\input\FreqTable.txt resources\input\ClearText.txt 
    resources\Input\Encoded.txt resources\output\Output.txt`)
5. Run the program in Standard Mode ('enhanced_off' with alternative input files): 
   `python -m Lab3 enhanced_off [-h] <input_file1> <alt_input_file2> <input_alt_file3> <output_file>`
    (i.e `python -m Lab3 enhanced_off resources\input\FreqTable.txt resources\input\ClearText2.txt 
    resources\Input\Encoded2.txt resources\output\Output2.txt`)
6. Run the program in Enhanced Mode ('enhanced on' with real inputs):
   `python -m Lab3 enhanced_on [-h] <input_file1> <input_file2> <input_file3> <output_file1> <output_file2>`
    (i.e `python -m Lab3 enhanced_on resources\input\CustomFreqText.txt resources\input\ClearText3.txt 
    resources\Input\Encoded3.txt resources\input\CustomFreqTable.txt resources\output\Output3.txt`)


```commandline
Standard usage: python -m enhanced_off Lab3 [-h] in_file1 in_file2 infile3 out_file
Enhanced usage: python -m enhanced_on Lab3 [-h] in_file1 in_file2 infile3 out_file1 outfile2

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

Both input and output files are to be in .txt format only.
Output will be written to the user specified output file after processing the input file.

Standard Mode Input files:
- 1. 'FreqTable.txt':  This is the standard Frequency Table provided for the lab
- 2. 'ClearText.txt':  This is the standard Clear Text file provided for the lab - to be converted to Huffman encodings
- 3. 'Encoded.txt':    This is the standard Encoded text file provided for the lab - to be converted to decoded text
- 4. 'ClearText2.txt':  This is an alternative Clear Text input file to demonstrate additional cases and edge handling
- 5. 'Encoded2.txt':  This is an alternative Encoded text file to demonstrate additional cases and edge handling

Standard Mode Output files:
- 'Output.txt':   Output text file recording results based on standard files (i,ii,iii) provided, per above
- 'Output2.txt':   Alternative output text file based on alternative (i, iv, v) files

Enhanced Mode Input files:
- 1. 'CustomFreqText.txt':  This is the source text provided by the user to convert into custom Huffman Frequency table
- 2. 'ClearText3.txt':  This is an alternative Clear Text input file to demonstrate additional cases and edge handling
- 3. 'Encoded3.txt':    This is an alternative Encoded text file to demonstrate additional cases and edge handling

Enhanced Mode Output files:
- 'CustomFreqTable.txt':   Custom Huffman Frequency Table built using user supplied text file (file i)
- 'Output3.txt':   Output text file recording results based on enhanced mode files provided, per above

## 4. Input file permissible format
FreqTable.txt:
- Enter 1 entry per line with the following example format: A - 20 (char, ' - ', integer)
- 'char' denotes the character symbol
- 'integer' denotes the frequency value
- NOTE: Only the FIRST character of each line is read in as the character symbol. 
- NOTE: Do NOT leave blank spaces prior to the character symbol or whitespace will be incorrectly read in.
- NOTE: Only alphabetical characters are accepted in Standard mode for the character symbol. All other symbols ignored.

CustomFreqText.txt:
- NOTE: Do not use blank spaces unless explicitly intended - eg. paragraph spaces etc. 
- Write single paragraph without blank lines above per above

ClearText.txt:
- Provide 1 sentence per line - use return carriage on each completed sentence line
- NOTE: Do not use blank spaces unless explicitly intended

Encoded.txt:
- Binary values (0/1) permitted only. All other characters, including whitespace and symbols, will be ignored
- Provide 1 sentence per line - use return carriage on each completed sentence line

## 5. Priority Queue Implementation

A Huffman Encoding Tree is constructed using a Priority Queue implemented with a minimum heap.

The Priority Queue precedence evaluation is performed according to the following rules:
- both characters are single characters: smallest frequency value has precedence
- one character is a single character, the other is a compound character: single character has precedence 
- both characters are compound characters: compound character containing the character with the smallest
          precedence has overall precedence


## 6. Project Package Layout:

* [Lab3/](.): The parent or "root" folder containing all of these files. 
    * [README.md](README.md):
      The guide you're reading. 
    * [Lab3](process_files.py): 
      This is a *module* in the *package*. There are 5 modules in total:
      * [`__init__.py`](Lab3/__init__.py) 
        This file is used to expose what functions, variables, classes, etc are exposed when scripts import this module. 
      * [`__main__.py`](Lab3/__main__.py) 
        This file is the entrypoint to the program. It handles command line arguments
      * `Lab3.py` 
        This module contains functions to parse input files for processing into the Huffman Frequency Table output and
        for encoding / decoding operations
      * `minheap.py` 
        This module contains heap node classes and functions performing minimum heap-related operations 
      * `utilities.py` 
        This module contains the utility functions such as comparison functions, sort functions and swap node functions
      



