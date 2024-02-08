'''
CIS 210 proj 5
Author: Oliver Boorstein
Credits: N/A
Implement a program to interpret and evaluate postfix expressions
'''

import doctest

def is_operator(operator: str) -> bool:
    '''
    (str) -> bool

    Return True if the operator is one of +, -, *, /, False otherwise.
    Examples:

    >>> is_operator("+")
    True
    >>> is_operator("a")
    False
    '''
    if operator in ('+', '-', '*', '/'):
        return True
    else:
        return False
    
def is_operand(operand: str) -> bool:
    '''
    (str) -> bool
    
    Return True if the operand is a digit, False otherwise.
    Examples:
    
    >>> is_operand("a")
    False
    >>> is_operand("3")
    True
    >>> is_operand("3.14")
    False
    '''
    if operand.strip("-").isdigit():
        return True
    else:
        return False


def apply_operator(op: str, oper_1: float, oper_2: float) -> float:
    '''
    (str, float, float) -> float
    
    Return the result of applying the operator to the operands.
    Examples:
    
    >>> apply_operator("+", 3, 4)
    7
    >>> apply_operator("/", 4, 2)
    2.0
    '''
    return eval(str(oper_1) + op + str(oper_2)) 

def eval_postfix(expr_str: str) -> float:
    '''
    (str) -> float

    Return the result of evaluating the postfix expression.
    Examples:

    >>> eval_postfix("3 4 +")
    7.0
    >>> eval_postfix("3 3 4 + 7 * /")
    0.061224489795918366
    '''
    operands = []
    expr_list = expr_str.split()
    for oper in expr_list:
        if is_operand(oper):
            operands.append(float(oper))
        elif is_operator(oper):
            if len(operands) < 2:
                return "error on postfix expression"
            result = apply_operator(oper, operands.pop(-2), operands.pop(-1))
            operands.append(result)
        else:
            return "error on postfix expression"
    if len(operands) != 1:
        return "error on postfix expression"
    return operands.pop(0)


if __name__ == "__main__":
    # print(apply_operator("/", 4, 2))
    # print(is_operand("a"))
    # print(is_operator(""))
    # print(eval_postfix("33 4 +"))
    # print(eval_postfix("3 3 4 + 7 * /"))
    # print(doctest.testmod())
    # print(is_operand("-2"))
    # print(eval_postfix("3 4 - 7 *"))
    pass