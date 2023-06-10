"""
---------------------
natural_merge_sort.py
---------------------
Python3 program to perform natural merge sort of linked list
"""
class Counter:
    """
    Counter class to record comparisons and swaps made by a sort algorithm
    """
    def __init__(self):
        self.swaps = 0
        self.comparisons = 0



class Node:
    """
    Node of a linked list element for storing a sequence of numbers to be sorted
    """
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_length(self):
        """
        Gets length of the linked list
        :return: count representing the length of the linked list
        """
        temp = self  # Initialise temp
        count = 0  # Initialise count

        # Loop while end of linked list is not reached
        while temp:
            count += 1
            temp = temp.next
        return count


class Queue:
    """
    Class represents a Queue ADT to implement FIFO precedence for merging of linked lists during natural merge sort
    """
    def __init__(self):
        self.head = None
        self.last = None

    def enqueue(self, data):
        """
        Function to push a node onto the queue
        :param data: the value of the node
        """
        if self.last is None:
            self.head = Node(data)
            self.last = self.head
        else:
            self.last.next = Node(data)
            self.last = self.last.next

    def dequeue(self):
        """
        Function to pop a node from the queue
        :return: the value of the popped node
        """
        if self.head is None:
            return None
        else:
            val_returned = self.head.data
            self.head = self.head.next
            return val_returned

    def is_empty(self):
        """
        Function to check if the queue is empty
        :return: Boolean True / False whether queue is empty
        """
        return self.head is None


def merge(h1, h2, counter, output_file, disable=False):
    """
    Function to merge 2 linked sub-lists as part of the merging process of natural merge sort.
    Each linked list is a run of sequentially ordered numbers.
    :param h1: first sub-list
    :param h2: second sub-list
    :param counter: counter to record comparisons and swaps during the merge operation
    :param output_file: output file to write results to
    :param disable: disable the writing to text files
    :return: 2 sub-lists merged as one
    """

    if disable is False:
        output_file.write("\n<<Pop and Merge Left sub-list and Right sub-lists>>\n")
        output_file.write("Popping sub-lists..." + "\n")
        output_file.write(">\tLeft:" + " ".join(map(str,print_list(h1))) + "\n")
        output_file.write(">\tRight:" + " ".join(map(str,print_list(h2))) + "\n")

    if h1 is None:  # left sub-list is empty, the rest of the non-empty sub-list is merged
        print_list(h2)
        h2_length = h2.get_length()
        counter.swaps += h2_length
        if disable is False:
            output_file.write("Left sub-list is empty, Pop and Merge remaining " + str(h2_length)
                              + " Right sub-list nodes; Swap count: " + str(counter.swaps) + "\n")
        return h2

    if h2 is None:  # right sub-list is empty, the rest of the non-empty sub-list is merged
        print_list(h1)
        h1_length = h1.get_length()
        counter.swaps += h1_length
        if disable is False:
            output_file.write("Right sub-list empty. Pop and Merge remaining " + str(h1_length)
                              + " Left sub-list nodes; Swap count: " + str(counter.swaps) + "\n")
        return h1

    # start with the linked list
    # whose head data is the least
    if h1.data < h2.data:
        counter.comparisons += 1
        counter.swaps += 1
        if disable is False:
            output_file.write(str(h1.data) + " compared with " + str(h2.data) + ";" + str(h1.data) + " merged" + "\n")
            output_file.write("Comparisons count: " + str(counter.comparisons) + "\n")
            output_file.write("Swap count: " + str(counter.swaps) + "\n")

        h1.next = merge(h1.next, h2, counter, output_file, disable)
        return h1

    else:
        counter.comparisons += 1  # Comparison made
        counter.swaps += 1  # Swap made
        if disable is False:
            output_file.write(str(h1.data) + " compared with " + str(h2.data) + ";" + str(h2.data) + " merged" + "\n")
            output_file.write("Comparisons count: " + str(counter.comparisons) + "\n")
            output_file.write("Swap count: " + str(counter.swaps) + "\n")

        h2.next = merge(h1, h2.next, counter, output_file, disable)
        return h2


def get_sorted_run_length(numbers_ll, num_queue, counter, output_file, disable=False):
    """
    Gets the sequence of linked list nodes that are in sequential order as a run
    :param numbers_ll: the linked list containing the numbers to be sorted
    :param num_queue: the numbers queue containing the linked lists
    :param counter: counter to record comparisons and swaps during the merge operation
    :param output_file: output file to write results to
    :param disable: disable the writing to text files
    :return: a queue containing all the individual run lengths of linked lists
    """
    numbers_end = numbers_ll

    if numbers_end.next is not None:
        if disable is False:
            output_file.write("\nSorted run-length comparisons:" + "\n")
            output_file.write("==============================" + "\n")

    while numbers_end.next:
        counter.comparisons += 1

        if disable is False:
            output_file.write(str(numbers_end.data) + " compared with " + str(numbers_end.next.data) +
                              "; comparison count = " + str(counter.comparisons) + "\n")

        if numbers_end.data > numbers_end.next.data:
            break

        numbers_end = numbers_end.next

    remaining = numbers_end.next

    numbers_end.next = None

    num_queue.enqueue(numbers_ll)

    if remaining is not None:
        return get_sorted_run_length(remaining, num_queue, counter, output_file, disable)

    else:
        if disable is False:
            output_file.write("\n>>>Sorted sub-lists have been pushed to queue<<<" + "\n")

        temp = num_queue.head
        temp_count = 0
        while temp:
            if disable is False:
                output_file.write("Linked List" + str(temp_count+1) + ":" + " ".join(map(str, print_list(temp.data)))
                                  + "\n")
            temp = temp.next
            temp_count += 1

        return num_queue


def get_num_queue(numbers_ll, counter, output_file, disable=False):
    """
    Function to get a number queue object containing runs of sequential linked list nodes
    :param numbers_ll: numbers linked list
    :param counter: counter to count comparisons and swaps performed by the sorting function
    :param output_file: output file to write results to
    :param disable: toggle to disarm or enable the writing of text output to file
    :return: num_queue object containing the linked list runs
    """
    num_queue = Queue()
    num_queue = get_sorted_run_length(numbers_ll, num_queue, counter, output_file, disable)

    return num_queue


def natural_merge_sort(num_queue, counter, output_file, disable=False):
    """
    Function to perform natural merge sort by calling upon get_sorted_run_length and merge functions
    :param num_queue: the numbers queue containing the linked lists
    :param counter: counter to record comparisons and swaps during the merge operation
    :param output_file: output file to write results to
    :param disable: toggle to disarm or enable the writing of text output to file
    :return: merged linked list object that has been sorted
    """

    left = num_queue.dequeue()
    right = num_queue.dequeue()

    if num_queue.is_empty():
        merged = merge(left, right, counter, output_file, disable)

        return merged

    else:
        merged = merge(left, right, counter, output_file, disable)
        num_queue.enqueue(merged)

        return natural_merge_sort(num_queue, counter, output_file, disable)


def print_list(node):
    """
    Utility function to print linked list
    :param node: Linked list node
    :return: node list
    """
    node_list = []

    while node is not None:
        node_list.append(node.data)
        node = node.next

    return node_list


def insert(root, item):
    """
    Function to insert a new node into a linked list
    :param root: the root / head of the linked list
    :param item: the item to be inserted
    :return: the root / head of the resulting linked list
    """
    temp = Node(item)  # Holding node

    if (root == None):
        root = temp
    else:
        ptr = root
        while (ptr.next != None):
            ptr = ptr.next
        ptr.next = temp

    return root


def arrayToList(arr):
    """
    Function to convert an array to a linked list
    :param arr: an array
    :return: linked list of nodes
    """
    n = len(arr)
    root = None
    for i in range(0, n, 1):
        root = insert(root, arr[i])

    return root

nms_counter = Counter()
