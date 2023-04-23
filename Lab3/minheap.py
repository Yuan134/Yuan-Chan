"""
--------------
minheap.py
--------------
This module contains the minimum heap node class and corresponding functions to process the nodes according to
a priority queue implemented by a minimum heap

Classes:
    heap_node: Huffman frequency node to be inserted into priority queue implemented using a minimum heap

Functions:
    heapify: format the heap nodes into a valid minimum heap
    build_heap: build a minimum heap from the heap nodes
    heap_push: push a heap node into the priority queue
    heap_pop: remove a heap node from the priority queue
    print_heap: print the minimum heap to console (for checking purposes only)
    conv_huff_tree: converts a minimum heap into a Huffman Tree
    huffman_decode: convert encoded Huffman binary strings into decoded text
    huffman_encode: convert clear text into Huffman encoded strings
    get_codes: print to output file Frequency Table key symbols and corresponding Huffman encodings
    print_preorder: prints to output file Huffman Tree using Pre-Order Traversal
"""
from Lab3.utilities import *


class heap_node:
    """
    A class to represent the Huffman frequency nodes to be inserted into a priority queue implemented using
    a minimum heap

    Parameters
    ----------
    value: single character assigned to the node representing a Huffman Frequency table entry
    frequency: integer digits recording frequency of occurrences for the "value" character
    left: the left branch of the node, initialized to None
    right: the right branch of the node, initialized to None
    """

    def __init__(self, value, frequency, left=None, right=None):
        self.data = value
        self.frequency = frequency
        self.left = left
        self.right = right
        # Direction of Huffman tree (0/1)
        self.dir = ""


def heapify(array, node_index: int) -> None:
    """
    Processes an array of Huffman frequency nodes and re-arranges the indices of the array elements to
    obtain a minimum heap format
    :param array: array containing Huffman frequency nodes
    :param node_index: The index of the array containing the Huffman node
    :return: None
    """
    smallest = node_index  # Initialize "smallest" heap node as root

    left_child = 2 * node_index + 1  # left = 2*i + 1
    right_child = 2 * node_index + 2  # right = 2*i + 2

    # If the left child is smaller than the root
    if len(array) > left_child == check_smallest(array, left_child, smallest):
        smallest = left_child

    # If the right child is smaller than all preceding nodes
    if len(array) > right_child == check_smallest(array, right_child, smallest):
        smallest = right_child

    # If smallest node is not the root
    if smallest != node_index:
        swap_nodes(array, node_index, smallest)

        # Heapify subtree recursively
        heapify(array, smallest)


def build_heap(array):
    """
    Constructs a minimum heap from an array of Huffman Frequency nodes
    :param array: Array of Huffman Frequency nodes
    :return: Array of Huffman Frequency nodes in minimum heap format
    """
    # The starting index is the index of the last non-leaf node
    start_index = len(array) // 2 - 1

    # Heapify each node in reverse order by traversing
    # from the last non-leaf node
    for i in range(start_index, -1, -1):
        heapify(array, i)

    return array


def heap_push(array, heap_node) -> None:
    """
    Function to insert a new Huffman Frequency node into the minimum heap priority queue
    :param array: Minimum heap array
    :param heap_node: New Huffman Frequency node to be inserted
    :return: None
    """
    array.append(heap_node)
    node_index = len(array) - 1

    while node_index > 0:
        parent_index = (node_index - 1) // 2

        # Perform "percolate up" to re-order array into minimum heap format
        if parent_index == check_smallest(array, node_index, parent_index):
            return
        elif node_index == check_smallest(array, node_index, parent_index):
            swap_nodes(array, node_index, parent_index)
            node_index = parent_index


def heap_pop(array):
    """
    Function to remove and return the smallest heap node from the minimum heap implemented priority queue
    :param array: array containing the Huffman frequency nodes
    :return: popped: the smallest removed heap node
    """
    # Remove the root node and return its value
    popped = array[0]
    # replace the popped root node with the last leaf node
    array[0] = array[len(array) - 1]
    del (array[len(array) - 1])  # Delete the last leaf node
    heapify(array, 0)  # Perform "percolate down" process - re-order array with respect to the new root

    return popped


def print_heap(array) -> None:
    """
    Prints the minimum heap configuration to the console (for checking purposes only)
    :param array: array containing the Huffman frequency nodes
    :return: None
    """
    print("Huffman heap:")

    for i in range(len(array)):
        print(array[i].data, array[i].frequency, end=" ")


def conv_huff_tree(huffman_heap):
    """
    Converts a minimum heap of Huffman Frequency nodes into a Huffman encoding tree
    :param huffman_heap: input heap to be converted into Huffman tree
    :return: huffman_heap: Reconfigured heap as a Huffman encoding tree
    """
    while len(huffman_heap) > 1:
        # Pop Huffman table twice to obtain Huffman Tree left and right nodes
        left = heap_pop(huffman_heap)
        right = heap_pop(huffman_heap)

        # assign directional value to heap nodes
        left.dir = 0
        right.dir = 1

        # combine the 2 smallest nodes to create
        # a new compound node as their parent

        node_comb_data = left.data + right.data
        # Sort the order of the compound node symbol characters for evaluation of precedence according (ascending order)
        node_comb_data = bubble_sort(node_comb_data)
        node_comb_freq = left.frequency + right.frequency  # Compound node combines the frequency values
        new_node = heap_node(node_comb_data, node_comb_freq, left, right)

        heap_push(huffman_heap, new_node)

    return huffman_heap


def huffman_decode(encoded_data, huffman_tree):
    """
    Function to decode the Huffman encoded binary string input
    :param encoded_data: Huffman encoded binary string list input
    :param huffman_tree: Huffman tree
    :return: string: str containing decoded text, tree_path: path of tree traversal recorded by branch directions (0/1)
    """
    root = huffman_tree[0]

    tree_path = ""  # Initialize empty string to store tree path directions
    decoded_output = []  # Initialize empty list to store decoded text strings

    # Recursively traverse Huffman Tree according to the Binary string encoding
    for item in encoded_data:
        if item == '0':
            root = root.left
            tree_path += str(root.dir)
        elif item == '1':
            root = root.right
            tree_path += str(root.dir)
        if root.left is not None or root.right is not None:
            pass
        elif root.left is None and root.right is None:
            decoded_output.append(root.data)
            root = huffman_tree[0]
            tree_path = ""

    string = ''.join([str(item) for item in decoded_output])

    return string, tree_path


def huffman_encode(un_encoded_str, code_dict, output_file, enhanced=False):
    """
    Function to convert text strings into Huffman binary encoding strings
    :param un_encoded_str: Clear text to be encoded using Huffman Tree
    :param code_dict: dictionary storing Huffman codes
    :param output_file: Output file containing Huffman encoding / decoding output
    :param enhanced: Boolean toggle (True/False) for enhanced mode "OFF" or "ON"
    :return: encoded_output: list containing Huffman encoded strings
    """
    encoded_output = []

    if enhanced is False:
        un_encoded_str = un_encoded_str.upper()

    for item in un_encoded_str:

        if enhanced is False and item.isalpha() is False:  # If not in enhanced mode: Skip whitespace and punctuation
            pass
        else:
            # If item is an upper case alphabet that does not exist in the Frequency Table but its lower-case exists
            if item not in code_dict and item.isalpha() and item.lower() in code_dict:
                output_file.write("Warning! Upper-case character: '" + item + "' not present in frequency table and" +
                                    " has been replaced with: '" + item.lower()+"'\n")

                encoded_output.append(code_dict[item.lower()])

            # Item does not exist in the Frequency Table
            elif item not in code_dict and not item.isalpha():
                output_file.write("Character: '" + item + "' not present in frequency table and has been IGNORED!\n")

            else:
                # print(code_dict[item], end = " ")
                encoded_output.append(code_dict[item])

    encoded_output = ''.join([str(item) for item in encoded_output])

    return encoded_output


def get_codes(root, output_file, expr='', code_dict={}, title=True):
    """
    Function to print the Huffman codes of each character by traversing the Huffman Tree
    :param root: Root node of the Huffman Tree
    :param output_file: Output file containing Huffman encoding / decoding output
    :param expr: string to store the tree direction (0/1) along the tree traversal
    :param code_dict: empty dictionary to store Huffman codes
    :param title: Toggle to ensure that the encoding section title is printed only once in the output
    :return: code_dict: populated dictionary storing Huffman codes
    """
    if title is True:  # Print title once only
        output_file.write("\nFREQUENCY TABLE ENCODING:\n")
        output_file.write("=========================\n")

    # string to store the tree direction (0/1) along the tree traversal
    new_expr = expr + str(root.dir)

    # keep traversing the tree until a leaf mode is reached
    if root.left:
        get_codes(root.left, output_file, new_expr, title=False)
    if root.right:
        get_codes(root.right, output_file, new_expr, title=False)

    # obtain the Huffman code at the leaf node
    if not root.left and not root.right:
        code_dict[root.data] = new_expr

        output_file.write(f"{root.data} -> {new_expr}\n")

    return code_dict


def print_preorder(root, output_file, title=True, space_counter=10) -> None:
    """
    Function to perform preorder tree traversal and print to output file
    :param root: Root of Huffman Tree
    :param output_file: Output file containing Huffman encoding / decoding output
    :param title: Toggle to ensure that the section title is printed only once in the output
    :param space_counter: Whitespace to format Huffman tree output (defaulted to 10 spaces)
    :return: None
    """
    if title is True:  # Print title once only
        output_file.write("HUFFMAN TREE IN PRE-ORDER TRAVERSAL:\n")
        output_file.write("====================================\n\n")

    if root:
        # Print the data of the tree node
        if root.dir == 0:
            tree_dir = "(L);"
            space_counter -= 2  # Decrement number of whitespaces by 2 when a left traversal occurs
        elif root.dir == 1:
            tree_dir = "(R);"
            space_counter += 2  # Increment number of whitespaces by 2 when a right traversal occurs
        else:
            tree_dir = "(root)"
        output_file.write(" " * space_counter + root.data + ":" + str(root.frequency) + tree_dir + '\n')

        # Call function recursively on the left child
        print_preorder(root.left, output_file, title=False, space_counter=space_counter)

        # Finally call function recursively on the right child
        print_preorder(root.right, output_file, title=False, space_counter=space_counter)
