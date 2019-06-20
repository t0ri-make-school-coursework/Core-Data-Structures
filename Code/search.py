#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_iterative(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    if array[index] == item:    # O(1)
        return index            # O(1)
    
    if array[index] == array[len(array) - 1]:   # O(1)
        return None                             # O(1)
    
    return linear_search_recursive(array, item, index + 1)  # O(1)
    
    
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # implement binary search iteratively here
    left = 0                        # O(1)
    right = len(array) - 1
    while left <= right:
        middle = (left + right) // 2
        if array[middle] == item:
            return middle
        elif item > array[middle]:
            left = middle + 1
        elif item < array[middle]:
            right = middle - 1
        
    return None
    # while the array at index is not item
    # middle = (len(array)-1)//2
    # check if middle is item
    # if item is bigger than middle
    # index = middle + 1
    # else
    # index = middle - 1
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests


def binary_search_recursive(array, item, left=None, right=None):
    if (left and right) is None:
        left = 0
        right = len(array) - 1
    
    if left <= right:
        middle = (left + right) // 2
        if array[middle] == item:
            return middle
        elif item > array[middle]:
            return binary_search_recursive(array, item, middle + 1, right)
        elif item < array[middle]:
            return binary_search_recursive(array, item, left, middle - 1)
    
    return None
    
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests

def main():
    names = ['Alex', 'Brian', 'Julia', 'Kojin', 'Nabil', 'Nick', 'Winnie']
    binary_search(names, 'Alex')

if __name__ == "__main__":
    main()