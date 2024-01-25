'''
CIS 210 proj 4 - 4
Author: Oliver Boorstein
Credits: N/A
Implement a fuction to choose a cipher to encrypt a message
'''

import p4_1, p4_2, p4_3

def crypt(msg: str, method) -> str:
    '''
    Encrypt/decrypt a given message using a requested
    encryption/decryption method
    Examples:
    
    >>> crypt("Ahoy, there!", p4_1.encrypt)
    hy hr!Ao,tee
    >>> crypt("hy hr!Ao,tee", p4_1.decrypt)
    Ahoy, there!
    '''
    return method(msg)

encrypted = crypt("Ahoy, there!", p4_1.encrypt)

print(encrypted, crypt(encrypted, p4_1.decrypt))