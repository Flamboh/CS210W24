'''
CIS 210 proj 4 - 2
Author: Oliver Boorstein
Credits: N/A
Implement functions to encrypt and decrypt a three rail cipher
'''


def encrypt(msg: str) -> str:
    '''
    Encrypt a str using the three
    rail cipher
    Examples:
    
    >>> encrypt("There is no reason anyone would want a computer in their home.")
    Trinrs yeoda cpeitihehesoeoao u naournhro.e   annnwlwt mt  e m
    >>> encrypt("The quick brown fox jumps over the lazy dog")
    T i o xusv ea ghqcbwf m et zdeukrnojporhlyo
    '''
    # use double colon slicing to take every third character from the message
    # starting at the first, second, and third character
    rail_1 = msg[::3]
    rail_2 = msg[1::3]
    rail_3 = msg[2::3]

    # the encrypted message is the concatenation of the three rails
    return rail_1 + rail_2 + rail_3


def decrypt(msg: str) -> str:
    '''
    Decrypt a str that was encrypted
    using the three rail cipher
    Examples:
    
    >>> decrypt("Trinrs yeoda cpeitihehesoeoao u naournhro.e   annnwlwt mt  e m")
    There is no reason anyone would want a computer in their home.
    >>> decrypt("T i o xusv ea ghqcbwf m et zdeukrnojporhlyo")
    The quick brown fox jumps over the lazy dog
    '''
    # create empty string to add the decrypted message to later
    decrypted = ""

    # the process for decrypting differs based on the length of the message,
    # specifically whether the length is divisible by 3 evenly, or has a remainder of either 1 or 2
    if len(msg) % 3 == 0:
        # split msg into three rails by using thirds indexes
        third_length = len(msg) // 3
        two_third_length = len(msg) // 3 * 2

        # each rail is a substring of msg using the thirds split
        rail_1 = msg[:third_length]
        rail_2 = msg[third_length:two_third_length]
        rail_3 = msg[two_third_length:]

        # as the lengths of each rail are the same in a message that fits evenly into thirds,
        # we can iterate through each rail and add the characters at the same index to the decrypted string   
        for i in range(third_length):
            decrypted += rail_1[i] + rail_2[i] + rail_3[i]
    # if the length of the message is not divisible by 3 evenly, we have to account for the remainder
    elif len(msg) % 3 == 1:
        # calculate thirds while accounting for the remainder
        third_length = len(msg) // 3 + 1
        two_third_length = len(msg) // 3 * 2 + 1
        
        # split msg into three rails by using thirds indexes
        rail_1 = msg[:third_length]
        rail_2 = msg[third_length:two_third_length]
        rail_3 = msg[two_third_length:]

        # if we iterate through the shortest rail, we can be sure that we will not go out of bounds
        # the third rail will always be the shortest
        for i in range(len(rail_3)):
            decrypted += rail_1[i] + rail_2[i] + rail_3[i]
        # in the case of 1 remainder only the first rail will have a character left over
        decrypted += rail_1[-1]
    # the only other option for remainder is 2 so we just use else
    else:
        # calculate thirds while accounting for the remainder again
        third_length = len(msg) // 3 + 1
        two_third_length = len(msg) // 3 * 2 + 2
        
        # split msg into three rails by using thirds indexes
        rail_1 = msg[:third_length]
        rail_2 = msg[third_length:two_third_length]
        rail_3 = msg[two_third_length:]

        # rail 3 remains the shortest in this case as well so we can iterate through its length
        for i in range(len(rail_3)):
            decrypted += rail_1[i] + rail_2[i] + rail_3[i]
        # this leaves two characters left over, one in rail 1 and one in rail 2
        decrypted += rail_1[-1] + rail_2[-1]


    
    return decrypted

if __name__ == "__main__":
    message = "The quick brown fox jumps over the lazy dog"
    # message = "There is no reason anyone would want a computer in their home."


    encrypted = encrypt(message)
    print(encrypted)

    decrypted = decrypt(encrypted)
    print(decrypted)

    # print(decrypted == message)
