#!/usr/bin/env python

import search
import unittest


class TestSearchIndex(unittest.TestCase):
    def test_empty_list(self):
        l = []
        self.assertEqual(search.index(10, l), -1)

    def test_single_element(self):
        l = [5]
        self.assertEqual(search.index(5, l), 0)
        self.assertEqual(search.index(10, l), -1)

    def test_elements(self):
        l = [2, 5, 9]
        for x in l:
            self.assertEqual(search.index(x, l), l.index(x), "{0} in {1}".format(x, l))


if "__main__" == __name__:
    unittest.main()
