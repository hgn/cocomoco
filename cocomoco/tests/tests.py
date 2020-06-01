import os
import sys

import unittest

import cocomoco

FILE_PATH = os.path.dirname(os.path.realpath(__file__))


class TestBasic(unittest.TestCase):


    def test_initialization(self):
        cm = cocomoco.calculate(100000, model=cocomoco.Embedded())
        self.assertTrue(cm != None)


if __name__ == '__main__':
    unittest.main()
