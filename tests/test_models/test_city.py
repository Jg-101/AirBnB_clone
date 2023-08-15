#!/usr/bin/env python3
"""
unittests for the City class in program
"""
import unittest
from models.city import City
from models.base_model import BaseModel


class testfile(unittest.TestCase):
    """ unittests for City class in prog"""
    def test_inheritance(self):
        """ checks if it inherits from BaseModel in prog"""
        self.assertTrue(issubclass(City, BaseModel))

    def test_attributes(self):
        """ checks if it has the correct attrs in prog """
        self.assertTrue('state_id' in City.__dict__)
        self.assertTrue('name' in City.__dict__)

    def test_str(self):
        """ checks if the string meth works """
        my_city = City()
        string = "[City] ({}) {}".format(my_city.id, my_city.__dict__)
        self.assertEqual(string, str(my_city))

    def test_save(self):
        """ checks if the save meth works """
        my_city = City()
        my_city.save()
        self.assertNotEqual(my_city.created_at, my_city.updated_at)

    def test_to_dict(self):
        """ checks if the to_dict meth works in prog"""
        my_city = City()
        new_dict = my_city.to_dict()
        self.assertEqual(type(new_dict), dict)
        self.assertTrue('to_dict' in dir(my_city))

    def test_docstring(self):
        """ checks if the docstr is correct in prog"""
        self.assertIsNotNone(City.__doc__)


if __name__ == "__main__":
    unittest.main()
