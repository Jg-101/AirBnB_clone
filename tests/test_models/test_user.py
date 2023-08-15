
!/usr/bin/env python3

import unittest
from models.user import User
from models.base_model import BaseModel


class testUser(unittest.TestCase):
    """ unittests for User class in prog"""
    def test_inherit(self):
        """ checks if it inherits from BaseModel """
        self.assertTrue(issubclass(User, BaseModel))

    def test_attributes(self):
        """ checks if it has attrs """
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertTrue(hasattr(user, "password"))
        self.assertTrue(hasattr(user, "first_name"))
        self.assertTrue(hasattr(user, "last_name"))

    def test_types(self):
        """ checks if it has correct types in prog"""
        user = User()
        self.assertEqual(type(user.email), str)
        self.assertEqual(type(user.password), str)
        self.assertEqual(type(user.first_name), str)
        self.assertEqual(type(user.last_name), str)

    def test_values(self):
        """ checks if it has correct vals """
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_str(self):
        """ checks if it has correct string rep """
        user = User()
        string = "[User] ({}) {}".format(user.id, user.__dict__)
        self.assertEqual(user.__str__(), string)

    def test_save(self):
        """ checks if it saves correctly in prog"""
        user = User()
        user.save()
        self.assertNotEqual(user.created_at, user.updated_at)


if __name__ == '__main__':
    unittest.main()
