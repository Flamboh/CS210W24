'''
CIS 210 proj 3 - wallis
Author: Oliver Boorstein
Credits: N/A
Estimate Pi using the Wallis method
'''


def pi_wallis(num_pairs: int) -> float:
    '''
    (int) -> float
    
    Estimate Pi using the wallis method,
    given a certain number of pairs
    Examples:
    
    >>> pi_wallis(5)
    3.0021759545569062
    >>> pi_wallis(20)
    3.1035169615392304
    '''

    half_pi = 1
    num = 2

    for pair in range(num_pairs): # add number of pairs
        # building the fractions
        left_frac = num / (num- 1) 
        right_frac = num / (num + 1)

        half_pi = half_pi * left_frac * right_frac # must not use *= syntax as it causes trouble with floats

        num += 2

    pi = half_pi * 2

    return pi

if __name__ == "__main__":
    print(pi_wallis(20))