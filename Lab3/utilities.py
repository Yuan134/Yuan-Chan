"""
--------------
minheap.py
--------------
This module contains the minimum heap node class and corresponding functions to process the nodes according to
a priority queue implemented by a minimum heap

Functions:
    check_smallest: Function to determine precedence of two compared Frequency table key characters
    bubble_sort: Function to perform an in-place Bubble Sort on compound Frequency table key characters
    swap_nodes: Function to swap Huffman nodes
"""


def check_smallest(array, index1, index2):
    """
    Function to determine precedence of two compared Frequency table key characters.
    Criteria is based on the following:
        - both characters are single characters: smallest frequency value has precedence
        - one character is a single character, the other is a compound character: single character has precedence
        - both characters are compound characters: compound character containing the character with the smallest
          precedence has overall precedence
    :param array: array containing the Huffman nodes
    :param index1: First comparison node index
    :param index2: Second comparison node index
    :return: min_index: Index of the node with precedence
    """
    char1_value = array[index1].data  # Character symbol of first comparison character
    char2_value = array[index2].data  # Character symbol of second comparison character
    char1_freq = array[index1].frequency  # Frequency value of first comparison character
    char2_freq = array[index2].frequency  # Frequency value of second comparison character

    if char1_freq < char2_freq:
        min_index = index1
    elif char1_freq > char2_freq:
        min_index = index2
    elif char1_freq == char2_freq:
        if len(char1_value) == 1 and len(char2_value) > 1:
            min_index = index1
        elif len(char2_value) == 1 and len(char1_value) > 1:
            min_index = index2
        elif char1_value < char2_value:
            min_index = index1
        elif char1_value > char2_value:
            min_index = index2
    else:  # Something went wrong since both values have equal precedence
        print("Error! Check for duplicate values with equal frequencies!")

    return min_index


def bubble_sort(string):
    """
    Function to perform an in-place Bubble Sort on compound Frequency table key characters so that precedence evaluation
    can be easily performed
    :param string: str containing the characters of the compound Huffman Frequency node
    :return: string: sorted str
    """

    str = list(string)

    n = len(string)

    for i in range(n):
        # Optimize bubble sort by ignoring the last i elements that are already positioned correctly
        for j in range(0, n - i - 1):

            # swap pairs if the adjacent element is larger than the next element
            if str[j] > str[j + 1]:
                str[j], str[j + 1] = str[j + 1], str[j]

    string = "".join(str)

    return string


def swap_nodes(array, node1, node2) -> None:
    """
    Function to swap Huffman Frequency node pairs
    :param array: Array containing Huffman Frequency nodes
    :param node1: Node 1
    :param node2: Node 2
    :return: None
    """
    array[node1], array[node2] = array[node2], array[node1]

