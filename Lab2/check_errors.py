"""
---------------
check_errors.py
---------------
This module contains various functions to check the input Prefix expressions for errors
"""


def is_operator(char: str) -> bool:
    """
    Identifies individual characters that are operators. Returns boolean True / False.
    :param char: Single character string
    :return: Boolean
    """

    # Predefined acceptable set of operators
    # Note: '^' is equivalent to and will be replaced by '$'
    if char == '$' or char == '^' or char == '*' or char == '/' or char == '+' or char == '-':
        return True
    else:
        return False


def is_operand(char: str, build_tree = False) -> bool:
    """
    Identifies valid operand characters (lower and uppercase alphabets and integers). Returns boolean True / False.
    :param char: Single character string representing alphabetical or numeric operands or "(" ")" parentheses
    :return: Boolean
    """
    if build_tree is False:  # if not building an expression tree, parentheses to define compound integers is supported
        if char == "(" or char == ")" or char.isalnum() is True:
            return True
        else:
            return False

    if build_tree is True:  # if building an expression tree, parentheses to define compound integers is not supported
        if char.isalnum() is True:
            return True
        else:
            return False


def check_illegal_char(char_str: str, build_tree=False):
    """
    Identifies if character is illegal i.e. invalid operand or operator. Returns error msg with illegal character count.
    :param char_str: Character string representing prefix expression input
    :return: Error message string if illegal characters detected or "None" for valid prefix expression
    """

    ill_char_list = []  # Initialize list to contain all identified illegal characters

    for item in char_str:
        if is_operand(item, build_tree) is False and is_operator(item) is False:
            ill_char_list += item

    ill_char_size = len(ill_char_list)  # Total number of illegal characters

    if ill_char_size > 0:  # Illegal characters > 0
        ill_char_str = " ".join(ill_char_list)
        error_msg = '\nExpression error! ' + str(ill_char_size) + \
                    ' illegal character/s detected: {} '.format(ill_char_str)

        return error_msg

    else:
        return None


def check_first(char_str: str):
    """
    Identifies if the first character of the Prefix expression is a valid operator. If invalid, returns error msg.
    :param char_str: Character string representing prefix expression input
    :return: Error message string if error detected or "None" for valid expression
    """

    first_char = char_str[0]

    if is_operator(first_char):
        return None
    else:
        error_msg = '\nExpression error! First character must be a valid operator'
        return error_msg


def check_last(char_str: str):
    """
    Identifies if the last character of the Prefix expression is a valid operand
    :param char_str: Character string representing prefix expression input
    :return: Error message string if error detected or "None" for valid expression
    """

    last_char = char_str[-1]

    if is_operand(last_char):
        return None
    else:
        error_msg = '\nExpression error! Last character must be a valid operand'

        return error_msg


def check_num_operators(char_str: str):
    """
    Checks the number of integer operands against the number of operators. Allows for parentheses to define compound
    (multi-digit) integers. Returns error message for invalid number of operators to integer operands
    :param char_str: Prefix expression string
    :return: Error message stating expected versus provided number of operators
    """

    # Initialize counters
    operand_count = 0  # Number of detected operands
    operator_count = 0  # Number of detected operators
    bracket_depth = 0  # Counter to record opening and closing parentheses. Opening parenthesis add 1, closing minus 1.

    for item in char_str:

        if item == '(':
            bracket_depth += 1
        elif item == ')':
            bracket_depth -= 1

        # If bracket depth is 1 (opening parenthesis), operands within the bracket can only be counted once, when
        # closing bracket is detected (i.e. bracket_depth is zero, and closing bracket is counted as a single operand)
        if bracket_depth == 0:  # Valid configuration - all opening brackets matched by closing brackets.

            if is_operator(item):
                operator_count += 1

            elif is_operand(item):
                operand_count += 1

    expected_operators = operand_count - 1  # Number of operators must be one more than number of operands

    if operand_count - operator_count != 1:
        error_msg = '\nExpression error! Number of operands = ' + str(operand_count) + \
                    '; Expected number of operators = ' + str(expected_operators) + \
                    '; Provided number of operators = ' + str(operator_count)

        return error_msg

    else:
        return None


def check_int_exp_consistency(int_exp_str):
    """
    Checks a string expression to ensure that integers and alphabets are not both present so that mathematical
    evaluation of an integer expression is possible. Returns error msg
    :param int_exp_str: Integer Prefix expression string
    :return: Error message if alphabetical operands are detected alongside integer operands or "None" for consistent
    expression
    """

    valid = True  # Set to valid expression by default - False if illegal operands detected
    illegal_oprnds = []  # Initialize empty list to store detected illegal operands

    for item in int_exp_str:

        if is_operand(item) and item.isalpha() is True:
            valid = False
            illegal_oprnds += item

    illegal_oprnds = " ".join(illegal_oprnds)

    if valid is False:
        error_msg = "\nIllegal expression! For expressions containing integers, alphabetical operands \"" + illegal_oprnds +\
                    "\" are not permitted!"
        return error_msg
    else:
        return None


def check_int_exp_parentheses(char_str: str):
    """
    Checks for valid parenthesis configuration - all opening brackets matched by closing brackets
    :param char_str: Prefix expression string
    :return: Error message if invalid parentheses configuration detected
    """
    # Initialize counter to check bracket configuration. 0 for valid configuration.
    # Add 1 for opening bracket, minus 1 for closing bracket
    bracket_depth = 0
    valid = True  # Set as default until illegal bracket configuration detected

    for item in char_str:
        if item == '(':
            bracket_depth += 1
        elif item == ')':
            bracket_depth -= 1

        if bracket_depth > 1:  # Invalid parentheses configuration detected
            valid = False

    if valid is False:  # Successive opening brackets without paired closing brackets
        error_msg = "\nIllegal parentheses configuration! Successive opening brackets \'(\' " \
                    "without matching closing brackets \')\'!"
        return error_msg

    else:  # Bracket depth is zero - all opening parentheses having paired closing parentheses
        return None


def is_valid_expr(char_str: str, output_file, is_int_exp: bool, build_tree=False) -> bool:
    """
    Compiles all error checks for the Prefix expression and writes corresponding error messages to output file
    :param char_str: Character string representing prefix expression input
    :param output_file: Output text file for writing error messages
    :param is_int_exp: Boolean for whether the input expression string is an integer mathematical expression
    :param build_tree: Boolean for whether to convert prefix to postfix by building and traversing an expression tree
    :return: boolean ('valid')
    """
    valid = True

    if build_tree is True:  # Obtain postfix by building and traversing expression tree
        if check_illegal_char(char_str, True) is not None:
            valid = False
            output_file.writelines(check_illegal_char(char_str, True))
        else:
            pass
    else:  # Direct recursion - expression tree is not built
        if check_illegal_char(char_str) is not None:
            valid = False
            output_file.writelines(check_illegal_char(char_str))
        else:
            pass

    if check_first(char_str) is not None:  # Check for valid first character
        valid = False
        output_file.writelines(check_first(char_str))

    else:
        pass

    if check_last(char_str) is not None:  # Check for valid last character
        valid = False
        output_file.writelines(check_last(char_str))

    # Prefix expression is an integer expression, check for number of operands vs operators
    if is_int_exp is True and check_num_operators(char_str) is not None:
        valid = False
        output_file.writelines(check_num_operators(char_str))

    # Prefix expression is an integer expression, check for consistency
    if is_int_exp is True and check_int_exp_consistency(char_str) is not None:
        valid = False
        output_file.writelines(check_int_exp_consistency(char_str))

    # Prefix expression is an integer expression, check for valid parentheses configuration
    if is_int_exp is True and check_int_exp_parentheses(char_str) is not None:
        valid = False
        output_file.writelines(check_int_exp_parentheses(char_str))

    # Regular non-integer prefix expression, check for number of operands vs operators
    elif is_int_exp is False and check_num_operators(char_str) is not None:
        valid = False
        output_file.writelines(check_num_operators(char_str))

    else:
        pass

    if valid is False:
        output_file.write('\n\n')

    return valid
