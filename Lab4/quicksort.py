
"""
------------
quicksort.py
-------------
Python program for recursive implementation of QuickSort
Adapted from original code by Sarah Kingan
Code ref: https://github.com/skingan/CSC162/blob/master/CSC162_LAB11_SBK.py
"""
import sys
from Lab4.insertion_sort import *


class Counter:
    """
    Class to perform counts of sort comparison and swap operations
    """

    def __init__(self):
        self.swaps = 0
        self.comparisons = 0


def quicksort(alist, pivot_type, counter, limit, output_file, disable):
    """
    quicksort algorithm with allowance for 3 different pivot types and for insertion sort to be performed once a
    partition size cut off is reached
    :param alist: a list of numbers to be sorted
    :param pivot_type: the pivot type for partitioning operations, options are:
        1 - First Index Position
        2 - Median of Three Position
        3 - Middle Index Position
    :param counter: counter that will permit sort comparisons and swaps to be recorded
    :param limit: the limit for insertion sort to be activated
    :param output_file: output file to write results to
    :param disable: disable the writing to text files
    """
    quicksort_helper(alist, 0, len(alist) - 1, pivot_type, counter, limit, output_file, disable)

    # Msg to be printed stating Pivot Type function
    if pivot_type == 1:
        if disable is False:
            output_file.write("\nQuickSort using pivot type: First Position Index\n")
    elif pivot_type == 2:
        if disable is False:
            output_file.write("\nQuickSort using pivot type: Median of Three\n")
    elif pivot_type == 3:
        if disable is False:
            output_file.write("\nQuickSort using pivot type: Middle Index\n")


def quicksort_helper(alist, first, last, pivot_type, counter, limit, output_file, disable):
    """
    Helper function for quicksort algorithm. Calls the partition function.
    :param alist: A list containing numbers to be sorted
    :param first: first index position of the input arrary
    :param last: last index position of the input array
    :param pivot_type: pivot type for partitioning operations
    :param counter: counter that will permit sort comparisons and swaps to be recorded
    :param limit: the limit for insertion sort to be activated
    :param output_file: output file to write results to
    :param disable: disable the writing to text files
    """

    arr_size = last - first + 1  # determine array size

    if first >= last:  # base case of a single partition, sort is complete
        return

    elif arr_size <= limit:  # Insertion sort activated
        if disable is False:  # print output text
            alist_str = " " .join(map(str, alist))
            output_file.write("\n<<INSERTION SORT ACTIVATED>>\n")
            output_file.write("\nArray in progress = " + alist_str + "\n")
            output_file.write("\nSize of sub-partition =" + str(arr_size) + "\n")
        # determines sub-partition for insertion sort to operate
        sub_partition = alist[first:last + 1]
        sub_part_str = " " .join(map(str, sub_partition))
        if disable is False:
            output_file.write("Sub-partition =" + sub_part_str + "\n")
        # Call insertion sort function
        sorted_sub_partition = insertion_sort(sub_partition, arr_size, counter, output_file, disable)
        sorted_sub_part_str = " ".join(map(str, sorted_sub_partition))
        if disable is False:
            output_file.write("sorted sub_partition: \n")
            output_file.write(sorted_sub_part_str + "\n")
        alist[first:last + 1] = sorted_sub_partition[0:]

    else:  # Continue with QuickSort partitioning
        split_point = partition(alist, first, last, pivot_type, counter, output_file, disable)
        if disable is False:
            output_file.write("\n*** Array in progress:\n" + " ".join(map(str,alist)) + "\n")
            output_file.write("\nArray split on either side of " + str(alist[split_point]) + " at index: "
                              + str(split_point) + "\n")
            output_file.write("\tPartition left: " + " ".join(map(str,alist[first: split_point - 1 + 1])) + "\n")
            output_file.write("\tPartition right: " + " ".join(map(str,alist[split_point + 1: last + 1]))+"\n")
        quicksort_helper(alist, first, split_point - 1, pivot_type, counter, limit, output_file, disable)
        quicksort_helper(alist, split_point + 1, last, pivot_type, counter, limit, output_file, disable)


def partition(alist, first, last, pivot_type, counter, output_file, disable=False):
    """
    Performs partitioning of array to be sorted recursively until base case of a single unit partition is reached
    to complete the sort
    :param alist: A list containing numbers to be sorted
    :param first: first index position of the input arrary
    :param last: last index position of the input array
    :param pivot_type: pivot type for partitioning operations
    :param counter: counter that will permit sort comparisons and swaps to be recorded
    :param output_file: output file to write results to
    :param disable: disable the writing to text files
    :return: the right mark index indicating where a new pivot should be located for the next recursive partitioning
    """
    pivot_index = get_pivot_index(alist, first, last, pivot_type, counter, output_file, disable)
    if disable is False:
        output_file.write("\nPivot at index: " + str(pivot_index) + ":" + str(alist[pivot_index]) + "\n")

    # if the chosen pivot is not at the first index,
    # swap the pivot into the first position
    if pivot_type == 2 or pivot_type == 3:
        temp = alist[first]
        alist[first] = alist[pivot_index]
        alist[pivot_index] = temp
        counter.swaps += 1

    # Incrementally move left and right marker
    left_mark = first + 1
    right_mark = last

    done = False

    while not done:
        while left_mark <= right_mark:
            #print("Last is index:", last)
            counter.comparisons += 1
            if disable is False:
                output_file.write("> " + str(alist[left_mark]) + " (index" + str(left_mark) +
                      ") left pointer compared with pivot; comparison count:" + str(counter.comparisons) + "\n")
            if alist[left_mark] > alist[first]:
                break

            elif alist[left_mark] <= alist[first]:

                if left_mark + 1 > last:  # Left pointer must not go beyond the right end of the sub-partition
                    break
                else:
                    left_mark += 1

        while right_mark >= left_mark:
            counter.comparisons += 1  # Comparisons made
            if disable is False:
                output_file.write("> " + str(alist[right_mark]) + " (index" + str(right_mark) +
                      ") right pointer compared with pivot; comparison count:" + str(counter.comparisons) + "\n")
            if alist[right_mark] < alist[first]:
                break
            elif alist[right_mark] >= alist[first]:
                right_mark -= 1
                if right_mark == first:
                    counter.comparisons += 1
                    if disable is False:
                        output_file.write("> " + str(alist[right_mark]) + " (index" + str(right_mark) +
                              ") right pointer compared with pivot; comparison count:" +
                                          str(counter.comparisons) + "\n")

        if right_mark <= left_mark:  # Right mark has either reached left mark position or moved beyond
            done = True  # Partitioning completed

        else:
            if alist[left_mark] != alist[right_mark]:
                counter.swaps += 1
                if disable is False:
                    output_file.write("\n>> '" + str(alist[left_mark]) + "' at index " + str(left_mark) +
                                      " swapped with '" + str(alist[right_mark]) + "' at index " + str(right_mark) +
                                      "; swap count:" + str(counter.swaps) + "\n")

            # swap markers for partitioning to continue
            temp = alist[left_mark]
            alist[left_mark] = alist[right_mark]
            alist[right_mark] = temp

    # Pivot is not equal to the number on the right marker
    if alist[first] != alist[right_mark]:
        counter.swaps += 1  # Perform swap
        if disable is False:
            output_file.write("\n>> '" + str(alist[first]) + "' at index " + str(first) + " swapped with '" +
                              str(alist[right_mark]) + "' at index " + str(right_mark) + "; swap count:" +
                              str(counter.swaps)+"\n")
    # Swap pivot with right mark
    temp = alist[first]
    alist[first] = alist[right_mark]
    alist[right_mark] = temp

    return right_mark


def get_median_three(alist, first, last, counter, output_file, disable):
    """
    obtains the index pertaining to the median of three value for use as the partition pivot
    :param alist: A list containing numbers to be sorted
    :param first: first index position of the input array
    :param last: last index position of the input array
    :param counter: counter that will permit sort comparisons and swaps to be recorded
    :param output_file: output file to write results to
    :param disable: disable the writing to text files
    :return: returns the median of three index to position the pivot
    """
    m3_counter = 0  # initialize median of three counter

    middle = first + (last - first) // 2

    if alist[first] <= alist[middle] <= alist[last]:
        m3_counter += 1  # comparison made
        m3_index = middle

    elif alist[last] <= alist[middle] <= alist[first]:
        m3_counter += 2  # 2nd comparison made
        m3_index = middle

    elif alist[first] <= alist[last] <= alist[middle]:
        m3_counter += 3  # 3rd comparison made
        m3_index = last

    elif alist[middle] <= alist[last] <= alist[first]:
        m3_counter += 4  # 4th comparison made
        m3_index = last

    else:
        m3_counter += 4
        m3_index = first

    counter.comparisons += m3_counter  # add comparisons made here to the overall count
    if disable is False:
        output_file.write("\n" + str(m3_counter) + " comparison/s made for Median of Three pivot; comparison count: "
                          + str(counter.comparisons) + "\n")

    return m3_index


def get_pivot_index(alist, first, last, pivot_type, counter, output_file, disable):
    """
    gets the position index of the pivot
    :param alist: A list containing numbers to be sorted
    :param first: first index position of the input array
    :param last: last index position of the input array
    :param pivot_type: pivot type for partitioning operations
    :param counter: counter that will permit sort comparisons and swaps to be recorded
    :param output_file: output file to write results to
    :param disable: disable the writing to text files
    :return: the pivot index
    """
    # pivot_type 1: Get index of first position
    if pivot_type == 1:
        pivot_index = first

    # pivot_type 2: Get median of three
    elif pivot_type == 2:
        pivot_index = get_median_three(alist, first, last, counter, output_file, disable)

    # pivot_type 3: Get middle index
    elif pivot_type == 3:
        pivot_index = first + (last - first) // 2
        if disable is False:
            output_file.write("pivot middle index: " + str(pivot_index) + "\n")
            output_file.write("pivot value: " + str(alist[pivot_index]) + "\n")

    else:
        if disable is False:
            output_file.write("Error - Invalid Pivot Type: please enter a valid pivot type (1-3)")
        sys.exit(1)

    return pivot_index


