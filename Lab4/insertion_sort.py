"""
-----------------
insertion_sort.py
-----------------
Python program for recursive implementation of Insertion Sort
Adapted from original code by Harsh Valecha
Code ref: https://www.geeksforgeeks.org/recursive-insertion-sort/
"""

class Counter:
    """
    Class to perform counts of sort comparison and swap operations
    """
    def __init__(self):
        self.swaps = 0
        self.comparisons = 0


def insertion_sort(arr, n, counter, output_file, disable=False):
    """
    Function to perform insertion sort algorithm
    :param arr: an array of numbers to be sorted
    :param n: the size of the array
    :param counter: counter that will permit sort comparisons and swaps to be recorded
    :param output_file: output file to write results to
    :param disable: disable the writing to text files
    :return: sorted array
    """
    # base case
    if n <= 1:
        return

    # Sort first n-1 elements
    insertion_sort(arr, n - 1, counter, output_file, disable)
    # Insert last element at its correct position in sorted array
    last = arr[n - 1]
    j = n - 2

    if j >= 0 and arr[j] < last:
        counter.comparisons += 1
        if disable is False:
            output_file.write("\n>'" + str(arr[j]) + "' at index " + str(j) + " compared with '" + str(last) +
                              "' at index " + str(n-1) + "; Comparisons = " + str(counter.comparisons) + "\n")
    # Move elements of arr[0..i-1], that are
    # greater than key, to one position ahead
    # of their current position
    while j >= 0 and arr[j] > last:
        counter.comparisons += 1
        if disable is False:
            output_file.write("\n> '" + str(arr[j]) + "' at index " + str(j) + " compared with '" + str(last) +
                              "' at index " + str(n-1) + "; Comparisons = " + str(counter.comparisons) + "\n")
        arr[j + 1] = arr[j]
        counter.swaps += 1
        if disable is False:
            output_file.write("\n>> '" + str(arr[j+1]) + "' swapped with '" + str(last) + "' ; Swaps = "
                              + str(counter.swaps) + "\n")

        j = j - 1

    arr[j + 1] = last
    if disable is False:
        output_file.write("\n*** Array in-progress:\n")
        output_file.write(" ".join(map(str, arr)) + "\n")
        print("\n")

    return arr




