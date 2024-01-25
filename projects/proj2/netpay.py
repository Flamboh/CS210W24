"""
CIS 210 proj1 - netpay
Author: Oliver Boorstein
Credits: N/A
Solve the problem of net pay in Utopia
"""

def tax(gross_pay: int or float) -> float:
    """
    Compute a 15% flat tax on the gross pay and return the result.

    Args:
        gross_pay: the gross pay amount

    Returns:
        float: the amount of taxes paid
    """
    return gross_pay * .15

print(tax(125))
print(tax(200))

def netpay(hours_worked: int) -> float:
    pre_tax_pay = 16.25 * hours_worked

    return round(pre_tax_pay - tax(pre_tax_pay), 2)

def main():
    '''Net pay program driver.'''
    print('For 1 hour of work, netpay is: ', netpay(1)) 
    print('For 40 hours of work, netpay is: ', netpay(40))
    return None 

if __name__ == '__main__':
    main() 
