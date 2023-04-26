#!/usr/bin/python3

"""test suite for base class"""

import unittest
from models.base import Base


class Test_Base(unittest.TestCase):
    """a suite to test base class"""

    def setUp(self):

        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base(5)
    def tearDown(self):
        del self.b1
        del self.b2
        del self.b3

    def test_base(self):
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 5)

if __name__ == "__main__":
    unittest.main()
