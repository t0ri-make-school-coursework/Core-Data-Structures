#!python

from sets import HashedSet
import unittest


# class LinkedSetTest(unittest.TestCase):

#     def test_init(self):
#         items = [3, 5, 7, 2, 5, 1, 'yeehaw']
#         linkedset = LinkedSet(items)
        
#         assert linkedset.size is 7
#         assert linkedset.list.head.data is 3

class HashedSetTest(unittest.TestCase):

    def test_init(self):
        ht = HashedSet()
        assert ht._size() == 0


    def test_init_with_items(self):
        items = [3, 5, 7, 2, 1, 'yeehaw']
        ht = HashedSet(items)
        
        assert ht._size() == 6
        assert ht.has('yeehaw') == True
        assert ht.has('') == False

    def test_size(self):
        ht = HashedSet()
        assert ht._size() == 0
        ht.add('A')
        assert ht._size() == 1
        ht.add('B')
        assert ht._size() == 2
        ht.remove('A')
        assert ht._size() == 1
        ht.remove('B')
        assert ht._size() == 0

    def test_add(self):
        ht = HashedSet()
        assert ht._size() == 0
        ht.add('A')
        assert ht._size() == 1
        assert ht.has('A') == True
        ht.add('B')
        assert ht._size() == 2
        assert ht.has('B') == True

    def test_remove(self):
        ht = HashedSet(['A', 'B'])
        ht.remove('A')
        assert ht._size() == 1
        assert ht.has('A') == False
        ht.remove('B')
        assert ht._size() == 0
        assert ht.has('B') == False

    def test_has(self):
        ht = HashedSet([3, 5, 7, 2, 1, 'yeehaw'])
        assert ht._size() == 6
        assert ht.has(5) == True
        ht.remove(5)
        assert ht.has(5) == False
        assert ht._size() == 5
        assert ht.has('A') == False
        assert ht.has('yeehaw') == True

    def test_union(self):
        ht = HashedSet([3, 5, 7, 2, 1, 'yeehaw'])

        assert ht.union(HashedSet([3, 5, 7, 2, 1, 'yeehaw']))._size() is 6 # all values same
        assert ht.union(HashedSet([4, 6, 8, 'hawyee']))._size() is 10 # all values different
        assert ht.union(HashedSet([1, 2, 9, 10]))._size() is 8 # some overlap
        assert ht.union(HashedSet([]))._size() is 6 # empty

    def test_intersection(self):
        ht = HashedSet([1, 2, 3, 4, 5, 6, 7])

        assert ht.intersection(HashedSet([6, 7, 8, 9, 10]))._size() is 2 # some overlap
        assert ht.intersection(HashedSet([1, 2, 3, 4, 5, 6, 7]))._size() is 7 # all values same
        assert ht.intersection(HashedSet(['yeehaw', 'hawyee']))._size() is 0 # no overlap
        assert ht.intersection(HashedSet([]))._size() is 0 #empty

    def test_is_subset(self):
        ht = HashedSet([1, 2, 3, 4, 5, 6, 7])
        empty_ht = HashedSet()

        assert ht.is_subset(HashedSet([1, 2, 3, 4, 5, 6, 7])) is True # exact match
        assert ht.is_subset(HashedSet([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) is True # overlap
        assert empty_ht.is_subset(HashedSet([])) is True # both empty
        assert ht.is_subset(HashedSet([])) is False # empty x2