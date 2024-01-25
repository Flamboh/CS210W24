'''
CIS 210 proj 3 - all pi
Author: Oliver Boorstein
Credits: N/A
Calculate pi to certain error tolerances with the Archimedes, Wallis, and Monte Carlo methods.
'''

import math
import arch
import wallis
import mc


def diff(num1, num2): # find the difference between two numbers
    return abs(num1 - num2)


def all_pi(err_tol: float) -> list:
    '''
    (float) -> list
    
    Calculate pi to a given error tolerance with
    three methods (Archimedes, Wallis, and Monte Carlo)
    using their imported functions in order to return the 
    number of  sides, pairs, or darts each method needs.
    Also prints something for each showing the difference 
    and the numbers of the accumulators.
    Examples:

    >>> all_pi(0.1)
    Archimedes: num_sides = 8 (Differs by 0.08012519466907486)
    Wallis: num_pairs = 8 (Differs by 0.0910026575342835)
    Monte Carlo: num_darts = 5 (Differs by 0.05840734641020706)
    [8, 8, 5] 

    >>> all_pi(0.01)
    Archimedes: num_sides = 23 (Differs by 0.009759724376121603)
    Wallis: num_pairs = 78 (Differs by 0.009989089968862164)
    Monte Carlo: num_darts = 14 (Differs by 0.0012644892673496777)
    [23, 78, 14]           
    '''
    # accumulators
    arch_acc = 1 
    wallis_acc = 1
    mc_acc = 1

    while True:
        if diff(arch.pi_arch(arch_acc), math.pi) >= err_tol: # loop until the difference between pi calculated using arch and math.pi is less than the inputted error tolerance
            arch_acc += 1
        elif diff(wallis.pi_wallis(wallis_acc), math.pi) >= err_tol: # same but with wallis
            wallis_acc += 1
        elif diff(mc.pi_mc(mc_acc), math.pi) >= err_tol: # same but with monte carlo
            mc_acc += 1   
        else: # if they're all within the error tolerance break the while loop
            break

    print(f"Archimedes: num_sides = {arch_acc} (Differs by {diff(arch.pi_arch(arch_acc), math.pi)})")
    print(f"Wallis: num_pairs = {wallis_acc} (Differs by {diff(wallis.pi_wallis(wallis_acc), math.pi)})")
    print(f"Monte Carlo: num_darts = {mc_acc} (Differs by {diff(mc.pi_mc(mc_acc), math.pi)})")

    return [arch_acc, wallis_acc, mc_acc] # return the accumulators in a list


if __name__ == "__main__":
    print(all_pi(0.1))