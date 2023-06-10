"""
----------
LLstack.py
----------
Stack class implementation using a singly linked list
"""


class Node:
    """
    Node class to implement the singly linked list
    """

    # Constructor to initialize the singly linked list node
    # Each node to contain a single character string
    def __init__(self, char: str):
        self.data = char
        self.next = None


class Stack:
    """
    Stack class to implement the stack object using the singly linked list
    """

    def __init__(self):
        """
        Constructor: Stack is initially empty so set head of linked list to NULL by default
        """
        self.head = None

    def is_empty(self):
        """
        Method to check if the stack is empty
        :return: Boolean
        """
        if self.head is None:
            return True
        else:
            return False

    def push(self, char):
        """
        - Method to add push a data item onto the top of the stack
        - Top of stack coincides with head of linked list
        :param char: single character string
        :return: None
        """

        if self.head is None:  # If stack is empty, initialize new data item as the head of the linked list
            self.head = Node(char)

        else:
            new_node = Node(char)  # Stack not empty
            new_node.next = self.head  # Current head of the linked list is re-positioned and linked behind the new node
            self.head = new_node  # New node is the new head of the linked list

    def pop(self):
        """
        Method to pop the top element of the stack
        :return: Popped item data or "None" if the stack is empty
        """

        if self.is_empty():
            return None

        else:
            # Popped item is the first node of the linked list
            popped_item = self.head
            # Define the next node on the linked list as the head
            self.head = self.head.next
            # Detach and discard the popped item
            popped_item.next = None

            return popped_item.data

    def size(self) -> int:
        """
        Returns the size of the stack
        :return: size_count: Integer size of the stack
        """

        aux_s = Stack()
        size_count = 0

        while not self.is_empty():
            aux_s.push(self.pop())
            size_count += 1

        while aux_s.is_empty():
            self.push(aux_s.pop())

        return size_count

    def peek(self):
        """
        Returns the item at the top of the stack without changing the stack
        :return: Single char string value or "None" if stack is empty
        """

        if self.is_empty():
            return None

        else:
            return self.head.data

    def reverse(self):
        """
        Reverses the order of the items in the stack
        :return: rev_stack (reversed stack)
        """
        rev_stack = Stack()

        while not self.is_empty():
            item = self.pop()

            rev_stack.push(item)

        return rev_stack

    def copy_stack(self):
        """
        Makes a deep copy of a stack without making changes to its contents
        :return: copied_stack
        """
        aux_stack = Stack()  # temporary holding stack
        copied_stack = Stack()

        while not self.is_empty():
            item = self.pop()

            aux_stack.push(item)

        # This step transfers all data items back to the original stack to reinstate it
        while not aux_stack.is_empty():
            copied_item = aux_stack.pop()
            copied_stack.push(copied_item)
            self.push(copied_item)

        return copied_stack

    def print_stack(self, output_file):
        """
        Displays the stack contents
        :param output_file: text file to write string of stack contents
        :return: None
        """

        item = self.head
        if self.is_empty():
            print("Error: Stack underflow")

        else:

            while item is not None:
                output_file.write(item.data)
                item = item.next
