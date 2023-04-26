#!/usr/bin/python3

"""test suite for base class"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
import os

class Test_Base(unittest.TestCase):
    """a suite to test base class"""

    def setUp(self):

        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base(5)
        self.r1 = Rectangle(10, 7, 2, 8)
    def tearDown(self):
        del self.b1
        del self.b2
        del self.b3
        try:
            os.remove(f"{self.r1.__class__.__name__}.json")
        except FileNotFoundError:
            pass
        del self.r1

    def test_base(self):
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 5)

    def test_type_instance(self):
        self.assertEqual(type(self.b1), Base)
        self.assertIsInstance(self.b2, Base)

    def test_to_json_string(self):
        dictionary = self.r1.to_dictionary()
        json_dict = Base.to_json_string([dictionary])
        self.assertEqual(type(dictionary), dict)
        self.assertIsInstance(json_dict, str)
    
    def test_save_to_file(self):
        dictionary = self.r1.to_dictionary()
        dictionary = Base.to_json_string([dictionary])
        Rectangle.save_to_file([self.r1])
        filename = f'{self.r1.__class__.__name__}.json'
        with open(filename, 'r') as f:
            data = f.read()
        self.assertEqual(data, dictionary)



if __name__ == "__main__":
    unittest.main()
