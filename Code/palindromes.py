#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase

# def reverse_text(text): 
#     return text[::-1] 

def clean_up(text):
    """
    Runtime: O(n) where n is length of text
    """
    text = text.lower()
    return ''.join(filter(str.isalpha, text))

def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    # return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    """
    Runtime: O(n)
    """
    text = clean_up(text) # O(n)
    length = len(text)
    for num in range(0, length // 2):
        if text[num] != text[length - 1 - num]:
            return False
    return True

    # once implemented, change is_palindrome to call is_palindrome_iterative
    # to verify that your iterative implementation passes all tests


def is_palindrome_recursive(text, left=None, right=None):
    if type(text) is not list: # init, base cases
        text = list(clean_up(text))

        if len(text) > 2: # if longer than 2
            left = 0
            right = len(text) - 1
        elif len(text) == 2: # if is 2
            if text[0] == text[1]:
                return True
            return False
        else: # if 1 or smaller
            return True
    
    if (left or right) is len(text) // 2: # if left or right is the middle
        return True
    
    if text[left] == text[right]: # if they're equal
        return is_palindrome_recursive(text, left + 1, right - 1)
    
    return False
    # once implemented, change is_palindrome to call is_palindrome_recursive
    # to verify that your iterative implementation passes all tests


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
