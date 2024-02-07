'''
CIS 210 lab 4 - functions
Author: Oliver Boorstein
Credits: N/A
'''

import doctest


def hello(first_name: str) -> None:
    '''
    (str) -> None

    Print a greeting using a first name str.
    Examples:

    >>> hello("Oliver")
    Hello, Oliver!
    >>> hello("Josh")
    Hello, Josh!
    '''
    print("Hello, " + first_name + "!")
    return None

def ciao(first_name: str) -> None:
    '''
    (str) -> None

    Print a greeting using a first name str.
    Examples:

    >>> ciao("Oliver")
    Ciao, Oliver!
    >>> ciao("Josh")
    Ciao, Josh!
    '''
    print("Ciao, " + first_name + "!")
    return None


def greeting(f, s: str) -> None:
    '''
    (function, str) -> None

    Print a greeting using a first name str.
    Examples:

    >>> greeting(hello, "Oliver")
    Calling hello
    Hello, Oliver!
    >>> greeting(ciao, "Josh")
    Calling ciao
    Ciao, Josh!
    '''
    print("Calling " + f.__name__)
    f(s)
    return None


def add_3(a, b, c):
    '''
    (num, num, num) -> num

    Return the sum of three numbers.
    Examples:

    >>> add_3(1, 2, 3)
    6
    >>> add_3(4, 5, 6)
    15
    '''
    return a + b + c

def mult_3(a, b, c):
    '''
    (num, num, num) -> num

    Return the product of three numbers.
    Examples:

    >>> mult_3(1, 2, 3)
    6
    >>> mult_3(4, 5, 6)
    120
    '''
    return a * b * c

def higher_order(f, a, b, c):
    '''
    (function, num, num, num) -> num

    Return the result of a function applied to three numbers.
    Examples:

    >>> higher_order(add_3, 1, 2, 3)
    Function: add_3
    add_3(1, 2, 3) = 6
    6
    >>> higher_order(mult_3, 4, 5, 6)
    Function: mult_3
    mult_3(4, 5, 6) = 120
    120
    '''
    print(f"Function: {f.__name__}")
    print(f"{f.__name__}({a}, {b}, {c}) = {f(a, b, c)}")    
    return f(a, b, c)


if __name__ == "__main__":
    # print(higher_order(add_3, 1, 2, 3))
    # print(doctest.testmod())
    pass