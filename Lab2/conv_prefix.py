"""
--------------
conv_prefix.py
--------------
Contains classes and functions to convert Prefix expression string to equivalent Postfix expression string.
3 alternatives are provided:
    1) Convert Prefix to Postfix using recursion directly
    2) Evaluate mathematical result of integer Prefix expression by obtaining infix order through recursion.
    3) Convert Prefix to Postfix by building and traversing expression tree

Classes:
    Node: Binary tree node to build expression tree

Functions:
    pre_post_rec: Converts Prefix expression to equivalent Postfix expression using recursion directly
    eval_pre_rec: Evaluates result of Prefix integer expression using recursion directly
    build_exp_tree: Builds binary expression tree from Prefix expression string
    trav_postfix: Traverses expression tree to derive Postfix expression
"""
from Lab2 import check_errors


def pre_post_rec(exp, curr_index=0, out_str=""):
    """
    Converts Prefix expression to equivalent Postfix expression using recursion directly
    :param exp: prefix expression string
    :param curr_index: index to iterate through the expression string character by character
    :param out_str: result string containing Postfix expression
    :return: out_str: the converted Postfix expression
    """
    while curr_index <= len(exp):
        op = exp[curr_index]
        curr_index += 1

        if check_errors.is_operator(exp[curr_index]):  # If character is an operator, left operand not yet detected
            # Iterate recursively through expression to find left operand
            op1, curr_index = pre_post_rec(exp, curr_index, out_str)

        else:
            op1 = exp[curr_index]  # left operand found
            curr_index += 1

        if check_errors.is_operator(exp[curr_index]):  # If character is an operator, right operand not yet detected
            # Iterate recursively through expression to find right operand
            op2, curr_index = pre_post_rec(exp, curr_index, out_str)
        else:
            op2 = exp[curr_index]
            curr_index += 1

        # Concatenate operators and operands in Postfix sequence
        out_str += op1
        out_str += op2
        out_str += op
        return out_str, curr_index


def eval_pre_rec(exp, curr_index=0, res=""):
    """
    Evaluates integer Prefix expression to return mathematical result.
    :param exp: Prefix expression string
    :param curr_index: Counter to iterate through Prefix string character by character
    :param res: string contains mathematical value of evaluated Prefix expression
    :return: res: Mathematical result of Prefix expression
    """

    while curr_index <= len(exp):
        op = exp[curr_index]
        if op == '$':  # Replace '$' operator with '**' to use Python "eval" function
            op = '**'
        curr_index += 1

        if check_errors.is_operator(exp[curr_index]):  # Operator detected, activate recursion to find first operand.
            op1, curr_index = eval_pre_rec(exp, curr_index, res)

        # Define multi-digit compound integer contained within parentheses brackets
        elif exp[curr_index] == "(":
            op1 = ""
            curr_index += 1
            while exp[curr_index] != ")":
                op1 += exp[curr_index]
                curr_index += 1
            curr_index += 1

        else:  # First operand found
            op1 = exp[curr_index]
            curr_index += 1

        if check_errors.is_operator(exp[curr_index]):  # Operator detected, activate recursion to find second operand.
            op2, curr_index = eval_pre_rec(exp, curr_index, res)

        # Define multi-digit compound integer contained within parentheses brackets
        elif exp[curr_index] == "(":
            op2 = ""
            curr_index += 1
            while exp[curr_index] != ")":
                op2 += exp[curr_index]
                curr_index += 1
            curr_index += 1

        else:
            op2 = exp[curr_index]
            curr_index += 1

        # Evaluate result in Infix order
        res += op1
        res += op
        res += op2
        eval_res = str(eval(res))
        return eval_res, curr_index


class node:
    """
    A class to represent the node of a binary tree.
    Parameters
    ----------
    data: string item assigned to the node representing an operator or operand
    left: the left branch of the node, initialized to None
    right: the right branch of the node, initialized to None
    """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_exp_tree(expr, curr_index=0):
    """
    Function to recursively build an expression tree from a Prefix expression string.
    :param expr: Prefix expression string
    :param curr_index: Index counter to iterate through Prefix string character by character
    :return: "root", the constructed expression tree
    """
    while curr_index <= len(expr):

        # Determine if the character is an operand
        if check_errors.is_operand(expr[curr_index]):
            prev_index = curr_index
            curr_index += 1
            return node(expr[prev_index]), expr, curr_index
        else:
            # Set the tree root node
            root = node(expr[curr_index])
            # Recursively build the left sub-tree
            curr_index += 1
            root.left, expr, curr_index = build_exp_tree(expr, curr_index)
            # Recursively build the right sub-tree
            root.right, expr, curr_index = build_exp_tree(expr, curr_index)
            return root, expr, curr_index


def trv_postfix(root, postfix_str=[]):
    """
    Function to traverse an expression tree and to output the equivalent Postfix expression
    :param root: Provided expression tree
    :param postfix_str: Postfix expression output contained in a list
    :return: postfix_str
    """
    if root is None:
        return
    else:
        trv_postfix(root.left, postfix_str)
        trv_postfix(root.right, postfix_str)
        postfix_str.append(root.data)

    postfix_str = "".join(postfix_str)

    return postfix_str
