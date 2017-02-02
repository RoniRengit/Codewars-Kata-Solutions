#!/ur/local/bin/python3.5
"""
Find the missing letter

Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
The array will always contain letters in only one case.
"""

def find_missing_letter(chars):

    
    alphabets = ['a', 'b' ,'c', 'd', 'e', 'f', 'g', 'h', \
                 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', \
                 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    if chars[0].islower():
        lists = [letter.lower() for letter in alphabets]
    else:
        lists = [letter.upper() for letter in alphabets]

    tmp = sorted([lists.index(characters) for characters in chars])

    for i in range(tmp[0], tmp[-1] + 1):
        if i not in tmp:
            return lists[i]
    
# Test Case
print(find_missing_letter(['O','Q','R','S'])) # => 'P'
