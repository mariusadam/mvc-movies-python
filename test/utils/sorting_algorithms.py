'''
Created on Dec 13, 2015

@author: Adam
'''
import unittest
from src.utils.sorting_algorithms import quick_sort, gnome_sort
from copy import deepcopy
from random import shuffle


class TestSorting(unittest.TestCase):

    def testQuickSort(self):
        l = [x for x in range(0, 100)]
        l2 = l[:]
        while l == l2:
            shuffle(l2)
        self.assertNotEqual(l, l2)
        l2 = quick_sort(l2, reverse=False)
        self.assertEqual(l, l2)
        while l == l2:
            shuffle(l2)
        l2 = quick_sort(l2, reverse=True)
        self.assertEqual(l[::-1], l2)
        
    def testGnomeSort(self):
        l = [x for x in range(0, 100)]
        l2 = l[:]
        while l == l2:
            shuffle(l2)
        self.assertNotEqual(l, l2)
        l2 = gnome_sort(l2, reverse=False)
        self.assertEqual(l, l2)
        while l == l2:
            shuffle(l2)
        l2 = gnome_sort(l2, reverse=True)
        self.assertEqual(l[::-1], l2)
        
def suite_utils():
    ts = unittest.TestSuite()
    ts.addTests(unittest.TestLoader().loadTestsFromTestCase(TestSorting))
    return ts


