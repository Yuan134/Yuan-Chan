"""
---------------
check_errors.py
---------------
This module contains various functions to check the input Prefix expressions for errors
"""


def is_operator(char: str) -> bool:
    """
    Identifies individual characters that are operators
    :param char: Single character string
    :return: Boolean
    """

    # Predefined acceptable set of operators
    # Note: '^' is equivalent to and will be replaced by '$'
    if char == '$' or char == '^' or char == '*' or char == '/' or char == '+' or char == '-':
        return True
    else:
        return False


def is_operand(char: str) -> bool:
    """
    Identifies individual characters that are valid operands (lower and uppercase supported)
    :param char: Single character string
    :return: Boolean
    """
    return char.isalpha()


def check_illegal_char(char_stack):
    """
    Identifies whether the character string is illegal i.e. not valid operand or operator
    :param char_stack: Stack object implemented using a linked list; contains Prefix expression input
    :return: Error message string if error detected or "None" for valid expression
    """
    # Make deep copy of original stack to avoid modifying original stack
    # Reverse it to maintain original order of input Prefix expression
    copied_stack = char_stack.copy_stack().reverse()
    ill_char_list = []  # Initialize list to contain all identified illegal characters

    while not copied_stack.is_empty():
        item = copied_stack.pop()
        if not is_operator(item) and not is_operand(item):  # Illegal character
            ill_char_list += item

    ill_char_size = len(ill_char_list)  # Total number of illegal characters

    if ill_char_size != 0:  # Illegal characters > 0
        ill_char_str = " ".join(ill_char_list)
        error_msg = '\nExpression error! ' + str(ill_char_size) + \
                    ' illegal character/s detected: {} '.format(ill_char_str)

        return error_msg

    else:
        return None


def check_first(char_stack):
    """
    Identifies if the first character of the Prefix expression is a valid operator
    :param char_stack: Stack object implemented using a linked list; contains Prefix expression input
    :return: Error message string if error detected or "None" for valid expression
    """
    # Make deep copy of original stack to avoid modifying original stack
    copied_stack = char_stack.copy_stack()

    first_char = (copied_stack.reverse()).peek()

    if is_operator(first_char):
        return None
    else:
        error_msg = '\nExpression error! First character must be a valid operator'
        return error_msg


def check_last(char_stack):
    """
    Identifies if the last character of the Prefix expression is a valid operand
    :param char_stack: Stack object implemented using a linked list; contains Prefix expression input
    :return: Error message string if error detected or "None" for valid expression
    """
    # Make deep copy of original stack to avoid modifying original stack
    copied_stack = char_stack.copy_stack()

    last_char = copied_stack.peek()

    if is_operand(last_char):
        return None
    else:
        error_msg = '\nExpression error! Last character must be a valid operand'

        return error_msg


def check_num_operators(char_stack):
    """
    Identifies if the expression has a correct number of operators based on the number of operands
    Number of operators should be: (Number of operands - 1)
    :param char_stack: Stack object implemented using a linked list; contains Prefix expression input
    :return: Error message string if error detected or "None" for valid expression
    """
    operator_count = 0
    operand_count = 0

    # Make deep copy of original stack to avoid modifying original stack
    copied_stack = char_stack.copy_stack()

    while not copied_stack.is_empty():
        char = copied_stack.pop()

        if is_operator(char):
            operator_count += 1

        elif is_operand(char):
            operand_count += 1

    expected_operators = operand_count - 1

    if operand_count - operator_count != 1:
        error_msg = '\nExpression error! Expected number of operators = ' + str(expected_operators) + \
                    '; Provided number of operators = ' + str(operator_count)

        return error_msg

    else:
        return None


def is_valid_expr(char_stack, output_file) -> bool:
    """
    Compiles all error checks for the Prefix expression and writes corresponding error messages to output file
    :param char_stack: Stack object implemented using a linked list; contains Prefix expression input
    :param output_file: Output text file for writing error messages
    :return: boolean ('valid')
    """
    valid = True

    if check_illegal_char(char_stack) is not None:
        valid = False
        output_file.writelines(check_illegal_char(char_stack))

    else:
        pass

    if check_first(char_stack) is not None:
        valid = False
        output_file.writelines(check_first(char_stack))

    else:
        pass

    if check_last(char_stack) is not None:
        valid = False
        output_file.writelines(check_last(char_stack))

    if check_num_operators(char_stack) is not None:
        valid = False
        output_file.writelines(check_num_operators(char_stack))

    else:
        pass

    if valid is False:
        output_file.write('\n\n')

    return valid
