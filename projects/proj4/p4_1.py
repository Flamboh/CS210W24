'''
CIS 210 proj 4 - 1
Author: Oliver Boorstein
Credits: N/A
Implement a simple transposition cipher
'''


def encrypt(msg: str) -> str:
    '''
    Encrypt a string using even-odd encryption
    Examples:
    
    >>> encrypt("It was a dark and stormy night")
    twsadr n tryngtI a  akadsom ih
    >>> encrypt("The quick brown fox jumps over the lazy dog")
    h uc rw o up vrtelz oTeqikbonfxjmsoe h aydg
    '''
    # create empty strings to add the even and odd characters to
    even_encrypt = ""
    odd_encrypt = ""

    for index in range(0, len(msg), 2):
        even_encrypt += msg[index]
    for index in range(1, len(msg), 2):
        odd_encrypt += msg[index]

    return odd_encrypt + even_encrypt

def decrypt(msg: str) -> str:
    '''
    Decrypt a string that was encrypted
    using even-odd encrpytion
    Examples:
    
    >>> decrypt("twsadr n tryngtI a  akadsom ih")
    It was a dark and stormy night
    >>> decrypt("h uc rw o up vrtelz oTeqikbonfxjmsoe h aydg")
    The quick brown fox jumps over the lazy dog
    '''

    decrypted = ""

    for odd_index in range(len(msg) // 2, len(msg)):
        even_index = odd_index - len(msg) // 2

        decrypted += msg[odd_index]
        
        if len(decrypted) != len(msg):
            decrypted += msg[even_index]
        else:
            break

    return decrypted


if __name__ == "__main__":
    message = "The quick brown fox jumps over the lazy dog"

    encrypted = encrypt(message)

    print(decrypt(encrypted), len(encrypted))