'''
CIS 210 lab 3 - pizza cal
Author: Oliver Boorstein
Credits: N/A
Calculate cost per square inch of a pizza
'''

import math
import doctest


def circle_area(diameter):
    '''
    (int) -> float
    
    Calculates and returns the area of a circle,
    given the diameter of the circle
    Examples:
    
    >>> circle_area(10)
    78.54
    >>> circle_area(4)
    12.566
    '''

    r = diameter / 2
    area = math.pi * r**2

    return round(area, 3)


def pizza_CPSI(diameter, cost):
    '''
    (int, num) -> float

    Calculates and returns the cost per square inch,
    given the diameter and cost of a pizza.
    Examples:
    
    >>> pizza_CPSI(14, 18)
    0.117
    >>> pizza_CPSI(14, 20.25)
    2   
    '''

    # r = diameter / 2
    # area = math.pi * r**2

    area = circle_area(diameter)

    cost_per_inch = cost / area
    cost_per_inch = round(cost_per_inch, 3)
    return cost_per_inch


if __name__ == "__main__":
    print(doctest.testmod())