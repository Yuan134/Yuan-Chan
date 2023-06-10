"""
------------
Lab4 package
------------
Modules:
  __main__.py:              Entry point to sort number files
  process.py:               Accepts input text file containing valid integer sequences (one number per line);
                            Outputs text file with sort counts
  quicksort.py:             Contains the quicksort algorithm implementation.
  insertion_sort.py:        Contains the insertion sort algorithm implementation. Called by the quicksort function.
  natural_merge_sort.py:    Contains the natural merge sort algorithm implementation
"""
from Lab4.process import process_files  # process_files: main function to process input and output files