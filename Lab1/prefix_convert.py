"""
-----------------
prefix_convert.py
-----------------
Module contains functions:
    prefix_to_postfix: Converts Prefix expression to equivalent Postfix expression
    prefix_to_infix: Converts Prefix expression to equivalent Infix expression
"""
from Lab1 import LLstack
from Lab1 import check_errors


def prefix_to_postfix(char_stack):
    """
    :param char_stack: Stack containing original prefix expression (characters read right to left)
    :return: postfix_stack: Stack containing equivalent Postfix expression
    """
    # Make deep copy of original stack to prevent modification
    copied_stack = char_stack.copy_stack()
    postfix_stack = LLstack.Stack()

    while not copied_stack.is_empty():
        item = copied_stack.pop()

        if check_errors.is_operator(item):
            operand1 = postfix_stack.pop()
            operand2 = postfix_stack.pop()

            string = operand1 + operand2 + item  # Equivalent Postfix sub-expression

            postfix_stack.push(string)

        else:

            postfix_stack.push(item)

    return postfix_stack


def prefix_to_infix(char_stack):
    """
    :param char_stack: Stack containing original prefix expression (characters read right to left)
    :return: infix_stack: Stack containing equivalent Infix expression
    """
    # Make deep copy of original stack to prevent modification
    copied_stack = char_stack.copy_stack()
    infix_stack = LLstack.Stack()

    while not copied_stack.is_empty():
        item = copied_stack.pop()

        if check_errors.is_operand(item):
            infix_stack.push(item)

        else:
            string = "(" + infix_stack.pop() + item + infix_stack.pop() + ")"  # Equivalent Infix sub-expression
            infix_stack.push(string)

    return infix_stack


