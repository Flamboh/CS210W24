'''
CIS 210 proj 3 - mc
Author: Oliver Boorstein
Credits: N/A
Estimate Pi using the Monte Carlo simulation
'''

import doctest
import random
import math


def pi_mc(num_darts: int) -> float:
    '''
    (int) -> float
    
    Estimate Pi using the Monte Carlo simulation,
    with a certain number of darts
    and with randomness seeded to 42
    Examples:

    >>> pi_mc(5)
    3.2
    >>> pi_mc(40)
    2.9
    '''

    random.seed(42)
    darts_in_circle = 0 # accumulator variable

    for i in range(num_darts):
        # generate random coordinates from 0 to 1
        x = random.random()
        y = random.random()

        # calculate the distance from the origin of the quarter circle
        distance = math.sqrt(x**2 + y**2)

        # if the distance is less than 1 then the dart landed in the circle
        if distance <= 1:
            darts_in_circle += 1


    pi = darts_in_circle / num_darts * 4 

    return pi

if __name__ == "__main__":
    print(doctest.testmod())
    