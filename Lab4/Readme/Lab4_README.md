# Lab 4 Project

Author: Chih Yuan Chan ID: 28A8CA

Contact email: cchan64@jh.edu

## 1. Overview:

This project runs the Quick Sort and Natural Merge Sort algorithms against input data sets of numbers
in varying sequencing and data sizes. Insertion Sort is combined with Quick Sort where the partition size falls below 
threshold limits. 
Output text files record the number of sorting operations (comparisons, sorts and comparisons + sorts)

Sort options:
1. Quick Sort with first array index as the pivot
2. Quick Sort with first array index as the pivot + Insertion Sort where file partition sizes <=50
3. Quick Sort with first array index as the pivot + Insertion Sort where file partition sizes <=100
4. Quick Sort with median of three as the pivot
5. Quick Sort with middle index as the pivot
6. Natural Merge Sort

Standard mode : 
- Output text file provided only for Size 50 data sets. No Dataframe summary results of sort runs.

Enhanced mode ('-a' or --'all'): 
- optional toggle on the CLI to indicate that all files are to produce text output files
- results summarized in Pandas dataframe 
- NOTE: Requires the installation of Pandas to run in enhanced mode.
- Pandas current version: 2.0.1. 
- To install: https://pandas.pydata.org/docs/getting_started/install.html

## 2. Acknowledgements:
Python program for recursive implementation of Insertion Sort
Adapted from original code by Harsh Valecha
`
Code ref: https://www.geeksforgeeks.org/recursive-insertion-sort/

Python program for recursive implementation of QuickSort
Adapted from original code by Sarah Kingan

Code ref: https://github.com/skingan/CSC162/blob/master/CSC162_LAB11_SBK.py`

## 3. Running Lab4:

1. Download and install Python on your computer
2. Navigate to [this](.) directory (containing the README.md)
3. Run the program as a module: `python -m Lab4`. 
4. Run the program in Standard Mode: 
   `python -m Lab4 [-h] <input_file_directory> <output_file directory>`
    (i.e `python -m Lab4 -a resources\input resources\output`)
5. Run the program in Enhanced Mode ('-a'):
   `python -m Lab3 -a [-h] <input_file_directory> <output_file_directory>`
    (i.e `python -m -a Lab4 resources\input resources\output`)


```commandline
Standard usage: python -m [-h] in_file out_file
Enhanced usage: python -m -a [-h] in_file out_file

positional arguments:
  in_file     Input File Directory Pathname
  out_file    Output File Directory Pathname

optional arguments:
  -a, --all   run all files and obtain text output and Pandas dataframes
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

## 4. Input and Output files:

Both input and output files are to be in .dat format only.
Both input and output files have been named according to the convention noted here and must be maintained:

## 5. Input file permissible format
'File Type' + 'File Size' + '_ccy.dat'
File type:-
- 'ran' (random ordered file)  
- 're>v' (reversed ordered file) 
- 'asc' (ascending ordered file)
- 'dup' (random wth 20% duplicates)
File size:- 
- This is an integer over the ranges: 50, 500, 1k, 2k, 3k (note: This module has not been designed to run file 
- sizes bigger than these because of memory performance)
Sample input text files:-
(Note: all input text files are appended with '_ccy' (my initials))

- 'ran2k_ccy.dat': random ordered file (size 2000)
- 'asc1k_ccy.dat': ascending ordered file (size 1000)   

## 6. Output file permissible format
'File Type' + ' File Size' + _ + Sort Type + _ + pivot type (Quick Sort only) + _ + limit (for Insertion Sort) 

NOTE: output text file self generated without user intervention once the directory is located.
File Type and File Size to be named per input file convention.
Additional requirements:
Sort type:- 
- 'QS' for QuickSort; 'NMS' for Natural Merge Sort
Pivot type:-
- 1: First position Index; 2: Median-of-Three Index; 3: Middle Index 
Output will be written to the user specified output directory  after processing the input file.
Insertion Sort limit:-
- This is the file size which will trigger Insertion Sort (currently 50 or 100)
Sample output text files:-
- ran1k_QS_1_0: random ordered file, size=1000 with first position as the index
- dup50_QS_1_100: random with duplicates ordered file; first position as index; 100 file limit for Insertion Sort

## 7. Project Package Layout:

* [Lab4/](.): The parent or "root" folder containing all of these files. 
    * [README.md](README.md):
      The guide you're reading. 
    * [Lab4](process.py): 
      This is a *module* in the *package*. There are 7 modules and 1 standalone script (generate_numbers.py) in total:
      * [`__init__.py`](Lab4/__init__.py) 
        This file is used to expose what functions, variables, classes, etc are exposed when scripts import this module. 
      * [`__main__.py`](Lab4/__main__.py) 
        This file is the entrypoint to the program. It handles command line arguments
      * `process.py` 
        This module contains functions to parse input files for processing into the Sorting modules
      * `quicksort.py` 
        This module contains the quicksort algorithm implementation
      * `insertion_sort.py`
        This module contains the insertion_sort algorithm implementation which is called by the quicksort function
      * `natural_merge_sort.py`
        This module contains the natural_merge_sort algorithm implementation      
      * `utility.py` 
        This module contains the utility functions to construct Pandas dataframe output
      - `generate_numbers.py`
        This is a standalone script to produce random and sequenced integer files complying with the input file format

## 8. Project Folder Contents
- 'input' folder: contains all input text files used as the basis to obtain the sort count results 
- 'output' folder: contains output text files for all size 50 input files + 'z_dataframes_out.dat' (dataframe summary)
- 'output_extra' folder: contains output text files for all file sizes

