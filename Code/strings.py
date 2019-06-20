#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text.
    Runtime, worst case: O(n^2), n is the len(text)
    Runtime, best case: O(1), if text == ''
    Space Complexity: O(n), n is the len(text)
    """
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    
    if text == '':
        return False
    elif pattern == '':
        return True
    
    if text[0] == pattern[0]:               # if the first characters match
        if len(pattern) == 1:               # and the pattern is only 1 character
            return True 
        for i in range(1, len(pattern)):    # loop 1 through length of pattern
            if len(text) < len(pattern):        # check there are enough characters left
                return False

            if text[i] == pattern[i]:       # if the pattern matches
                if i == len(pattern) - 1:     # check if the pattern is over
                    return True
            else:                           # if the pattern stops matching
                text = text[i:]                 # set text to after current index
                return contains(text, pattern)  # start again
    else:                                   # if no match
        text = text[1:]                     # set text to after current index
        return contains(text, pattern)      # start again


def find_index_iterative(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found.
    Runtime, worst case: O(n), n is len(text)
    Runtime, best case: O(1), if text == ''
    Space Complexity: O(n), n is len(text)
    """
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    
    if text == '':
        return None
    elif pattern == '':
        return 0

    index = 0
    iterator = 0
    for char in text:                           # for each character of text
        if char == pattern[iterator]:               # if character matches current character of pattern
            if iterator == len(pattern) - 1:            # if iterator is at the length of pattern
                return index - iterator                     # return starting index
            
            iterator += 1                               # if iterator is not at pattern length, iterator++
        else:
            iterator = 0                            # reset iterator if pattern stops matching
            if char == pattern[iterator]:           # check start of pattern on current char
                iterator += 1
        index += 1                                  # index++

def find_index(text, pattern, index=0, iterator=0):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found.
    Runtime, worst case: O(n), n is len(text)
    Runtime, best case: O(1), if text == ''
    Space Complexity: O(1), creating no new variables
    """
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    
    if text == '':
        return None
    elif pattern == '':
        return 0

    if index < len(text):  #if text[index] exists
        if text[index] == pattern[iterator]:
            if iterator == len(pattern) - 1:
                return index - iterator
            
            return find_index(text, pattern, index+1, iterator+1)
        elif iterator > 0:
            return find_index(text, pattern, index)
        else:
            return find_index(text, pattern, index+1)
    else:
        return None

def find_all_indexes(text, pattern, indexes=None, index=0, iterator=0):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found.
    Runtime, worst case: O(n), n is len(text)
    Runtime, best case: O(1), if text == ''
    Space Complexity: O(n), appending to indexes list
    """
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    

    # lists were initializing using previous function call's output
    if indexes == None:
        indexes = list() 
    
    if text == '':
        return indexes
    elif pattern == '':
        for i in range(0, len(text)):
            indexes.append(i)
        return indexes

    if index < len(text):  #if text[index] exists
        if text[index] == pattern[iterator]:
            if len(pattern) == 1:
                indexes.append(index - iterator)
                return find_all_indexes(text, pattern, indexes, index+1, 0)
            if iterator == len(pattern) - 1:                
                indexes.append(index - iterator)
                return find_all_indexes(text, pattern, indexes, index, 0)
            
            return find_all_indexes(text, pattern, indexes, index+1, iterator+1)
        elif iterator > 0:
            return find_all_indexes(text, pattern, indexes, index, 0)
        else:
            return find_all_indexes(text, pattern, indexes, index+1, 0)
    else:
        return indexes


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))

    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
