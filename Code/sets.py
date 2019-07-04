#!python

from linkedlist import LinkedList
from hashtable import HashTable


class LinkedSet(object):

    def __init__(self, items=None):
        """Initialize the set and add the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        # self.size property is _size()
        if items is not None:
            for item in items:
                self.add(item)

    def _size(self):
        """Get size of self.list"""
        return self.list.size

    def add(self, item):
        """Append given item to the end of the set."""
        # Raise value error if set already contains input value.
        if self.has(item):
            # raise ValueError('Set already contains {}'.format(item))
            print('Set already contains {}'.format(item))
            return
        
        # Add item to set using LL.append() method
        self.list.append(item)
        print(self.list)
    
    def has(self, item):
        """Determine if the set contains a given value."""
        value = self.list.find(lambda value: value == item)

        if value is not None:
            return True
        
        return False

    def remove(self, item):
        """Remove an item from the set if it exists"""
        self.list.delete(item)


class HashedSet(object):

    def __init__(self, items=None):
        """Initialize the set and add the given items, if any"""
        # Initialize a new hashtable to store the items
        self.table = HashTable()
        self.size = self._size
        if items is not None:
            for item in items:
                self.add(item)

    def __str__(self):
        """Return a formatted string representation of this set"""
        # Use HT.__str__() method to format
        return self.table.__str__()
    
    def _size(self):
        """Get size of hashtable"""
        # Use HT.size property to get size
        return self.table.size

    def add(self, item):
        """Add given item to the set
        Time Complexity Avg Case -- O(1) using hashtable
        Time Complexity Worst Case -- O(n) on resize
        """
        # Raise value error if set already contains input value
        if self.has(item):
            raise ValueError('Set already contains {}'.format(item))
        
        # Add item to set using HT.set() method
        self.table.set(item, item)
    
    def has(self, item):
        """Determine if the set contains a given value
        Time Complexity Avg Case -- O(1) using hashtable"""
        # Use HT.contains() method to find item
        return self.table.contains(item)

    def remove(self, item):
        """Remove an item from the set if it exists
        Time Complexity Avg Case -- O(1) using hashtable
        Time Complexity Worst Case -- O(n) on resize"""
        # Use HT.delete() method to remove item
        self.table.delete(item)

    def union(self, set_two):
        """Return the concatenation of two sets
        Time Complexity Avg Case -- O(n+m)"""
        # If set_two is empty return only set_one (self)
        if set_two.size is 0:
            return self
        
        # Create new set to hold set_one (self) values
        union = HashedSet(self.table.values()) # O(n)
        # Check if each value in set_two is in set_one (self)
        for value in set_two.table.values(): # O(m)
            if not self.has(value): # O(1)
                # Add any non-duplicates to union
                union.add(value) # O(1) / unlikely worst case O(n)

        return union

    def intersection(self, set_two):
        """Return a set of the common values of two sets
        Time Complexity Avg Case -- O(m)"""
        # Create a new set
        intersection = HashedSet() # O(1)
        
        # If set_two is empty return empty set
        if set_two._size is 0: # O(1)
            return intersection
        
        # Check if each value in set_two is in set_one (self)
        for value in set_two.table.values(): # O(m)
            if self.has(value): # O(1)
                # Add common values to intersection
                intersection.add(value) # O(1) / unlikely worst case O(n)

        return intersection

    def difference(self, set_two):
        """Return a set that contains all of the values not
        appearing in set_two that are in set_one (self)
        Time Complexity Avg Case -- O(n+m)"""
        # If set_two is empty return only set_one (self)
        if set_two._size is 0: # O(1)
            return self
        # Create a new set to hold set_one (self) values
        difference = HashedSet(self.table.values()) # O(n)
        # Remove each value from difference as they appear in set_two
        for value in set_two.table.values(): # O(m)
            if self.has(value): # O(1)
                difference.remove(value) # O(1) / unlikely worst case O(n)
        
        return difference

    def is_subset(self, set_two):
        """Return if every element of set_one (self) is a member of set_two.
        Time Complexity Avg Case -- O(m)"""
        if set_two.size is 0: # O(1)
            if self.size is 0: # O(1)
                return True
            return False
        # Create a bool to return and to control while loop
        is_subset = True # O(1)
        # Loop until a value of set_two isn't found in set_one
        while is_subset is True:
            for value in self.table.values(): # O(m)
                if not set_two.has(value): # O(1)
                    is_subset = False # O(1)
            return is_subset


def main():
    hs = HashedSet([1, 2, 3, 4, 5, 'yeehaw'])
    print(hs)

    union = hs.union(HashedSet(['hawyee', 6, 7, 8, 9, 10]))
    # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, yeehaw, hawyee
    # print(union)

    intersection = hs.intersection(HashedSet(['yeehaw', 3, 5, 10])) # yeehaw, 3, 5
    # print(intersection)

    difference = hs.difference(HashedSet([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # yeehaw
    # print(difference)

    is_subset_true = hs.is_subset(HashedSet([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'yeehaw']))
    # print(is_subset_true)
    
    is_subset_false = hs.is_subset(HashedSet([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    # print(is_subset_false)


if __name__ == "__main__":
    main()
