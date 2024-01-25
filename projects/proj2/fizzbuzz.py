"""
CIS 210 proj1 - fizzbuzz
Author: Oliver Boorstein
Credits: N/A
Write a function for the game fizzbuzz
"""


def fb(n):
    '''
    If n is divisible by 3, return “fizz”.
    If it is divisible by 5, return “buzz”.
    If it is divisible by both 3 and 5, return “fizzbuzz”.
    Otherwise, just return the number.

    Parameters:
        n (int): A decimal integer
    
    Returns:
        n, 'fizz', or 'buzz'
    '''

    if n % 15 == 0:
        return 'fizzbuzz'   
    elif n % 3 == 0:
        return 'fizz'
    
    elif n % 5 == 0:
        return 'buzz'
    
    else:
        return n


def fbloop(num):
    '''
    Loop from 1 to num executing fb

    Parameters:
        num: the last number to include in the loop

    Returns:
        None
    '''

    for i in range(1, num + 1):
        print(fb(i))
    print("Game over!")

fb(1)

if __name__ == '__main__':
    fbloop(15)
