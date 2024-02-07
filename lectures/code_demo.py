
import doctest

def count_vowels(msg: str) -> int:
    '''
    Count the number of vowels in a string
    Examples:
    
    >>> count_vowels('UniversityOfOregon')
    8
    >>> count_vowels('8 vowels')
    2
    '''

    vowels_acc = 0 # accumulator
    consonants_acc = 0

    vowels_list = ['a', 'e', 'i', 'o', 'u']

    msg = msg.lower()

    for char in msg:
        if char in vowels_list:
            vowels_acc += 1
        elif char.isalpha():
            consonants_acc += 1
    
    return vowels_acc, consonants_acc
        

if __name__ == "__main__":
    # print(count_vowels('UniversityOfOregon'))
    print(count_vowels('8 vowels'))
    # print(doctest.testmod())