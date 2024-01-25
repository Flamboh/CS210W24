'''
CIS 210 proj 3 - arch
Author: Oliver Boorstein
Credits: N/A
Estimate Pi using the Archimedes approach
'''

import matplotlib.pyplot as plt
import numpy as np
import math


def pi_arch(num_sides: int) -> float:
    '''
    (int) -> float
    
    Estimate Pi using the Archimedes approach,
    given a certain number of sides
    Examples:
    >>> pi_arch(20)
    3.1286893008046173
    >>> pi_arch(5)
    2.938926261462366
    '''
    
    inner_angle_B = 360.0 / num_sides
    half_angle_A = inner_angle_B / 2

    half_side_S = math.sin(math.radians(half_angle_A))
    side_S = half_side_S * 2

    polygon_circumference = num_sides * side_S
    pi = polygon_circumference / 2
    
    return pi


def gen_increasing_pi(n):
    nums = ()
    increasing_pi = ()
    for i in range(1, n):
        increasing_pi += (pi_arch(i),)
        nums += (i,)

    return nums, increasing_pi


if __name__ == "__main__":
    data_x, data_y = gen_increasing_pi(10)

    plt.scatter(data_x, data_y)
    plt.show()