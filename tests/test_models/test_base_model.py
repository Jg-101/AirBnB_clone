#!/usr/bin/python3
""" unittest for models/base_model.py in prog

    test classes:
        test_BaseModel_instantiation in prog
        test_BaseModel_save in prog
        test_BaseModel_to_dict in prog
        test_BaseModel_str in prog
"""
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel

###############################################################################
# test_BaseModel_instantiation
###############################################################################


class Test_BaseModel_instantiation(unittest.TestCase):
    """ test instantiation of BaseModel in prog """
    def test_BaseModel_instantiation(self):
        """ test instantiation of BaseModel in prog"""
        bm = BaseModel()
        self.assertTrue(hasattr(bm, "id"))
        self.assertTrue(hasattr(bm, "created_at"))
        self.assertTrue(hasattr(bm, "updated_at"))

    def test_BaseModel_instantiation_no_args(self):
        """ test instantiation of BaseModel with no args in prog"""
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_BaseModel_instantiation_kwargs(self):
        """ test instantiation of BaseModel with kwargs in prog"""
        bm = BaseModel(name="Ronald")
        self.assertTrue(hasattr(bm, "name"))

    def test_BaseModel_instantiation_store_object(self):
        """test stored objs in prog"""
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_BaseModel_created_date(self):
        """ test created_at in prog"""
        bm = BaseModel()
        self.assertTrue(isinstance(bm.created_at, datetime))

    def test_BaseModel_created_date2(self):
        bm = BaseModel()
        self.assertEqual(type(bm.created_at), datetime)

    def test_BaseModel_updated_date(self):
        """ test updated_at in prog"""
        bm = BaseModel()
        self.assertTrue(isinstance(bm.updated_at, datetime))

    def test_BaseModel_updated_date2(self):
        bm = BaseModel()
        self.assertEqual(type(bm.updated_at), datetime)

    def test_BaseModel_create_sleep(self):
        """ create two objs at different time in prog"""
        bm1 = BaseModel()
        sleep(0.1)
        bm2 = BaseModel()
        self.assertNotEqual(bm1.created_at, bm2.created_at)

###############################################################################
# test_BaseModel_save
###############################################################################


class Test_BaseModel_save(unittest.TestCase):
    def test_BaseModel_save(self):
        """ Test save meth in prog"""
        bm = BaseModel()
        bm.save()
        self.assertNotEqual(bm.created_at, bm.updated_at)

    def test_BaseModel_save_2(self):
        """ test save two times in prog """
        bm = BaseModel()
        bm.save()
        sleep(0.2)
        bm.save()
        self.assertLess(bm.created_at, bm.updated_at)

###############################################################################
# test_BaseModel_instantiation
###############################################################################


class Test_BaseModel_to_dict(unittest.TestCase):
    """ test to_dict meth in prog """
    def test_BaseModel_dict_type(self):
        """ test to_dict meth in prog """

    def test_BaseModel_dict_keys(self):
        """ test to_dict meth correct keys """
        bm = BaseModel()
        self.assertIn("id", bm.to_dict())
        self.assertIn("created_at", bm.to_dict())
        self.assertIn("updated_at", bm.to_dict())
        self.assertIn("__class__", bm.to_dict())


###############################################################################
# test_BaseModel_str
###############################################################################


class Test_BaseModel_str(unittest.TestCase):
    """ test string meth in prog"""

    def test_BaseModel_str(self):
        """ test string meth. assertEqual: a and b are equal"""
        bm = BaseModel()
        self.assertEqual(type(str(bm)), str)

    def test_BaseModel_add_attr(self):
        """ test to_dict if contains added attrs in prog"""
        bm = BaseModel()
        bm.name = "Ronald"
        bm.my_number = 41
        self.assertIn("name", bm.to_dict())
        self.assertIn("my_number", bm.to_dict())

    def test_BaseModel_format_date(self):
        """ test format of date in prog"""
        bm = BaseModel()
        self.assertEqual(type(bm.to_dict()["created_at"]), str)
        self.assertEqual(type(bm.to_dict()["updated_at"]), str)

    def test_BaseModel_list_type(self):
        """ test to_dict if contains added attrs in prog """
        bm = BaseModel()
        self.assertEqual(type(bm.to_dict()), dict)

    def test_BaseModel_dict_values(self):
        """ test to_dict if contains added attrs in prog """
        bm = BaseModel()
        self.assertEqual(type(bm.to_dict()["id"]), str)
        self.assertEqual(type(bm.to_dict()["created_at"]), str)
        self.assertEqual(type(bm.to_dict()["updated_at"]), str)
        self.assertEqual(type(bm.to_dict()["__class__"]), str)

    def test_BaseModel_full_dict(self):
        """ test to_dict if contains added attrs """
        bm = BaseModel()
        bm.name = "Ronald"
        bm.my_number = 41
        self.assertEqual(type(bm.to_dict()), dict)
        self.assertIn("name", bm.to_dict())
        self.assertIn("my_number", bm.to_dict())
        self.assertIn("id", bm.to_dict())
        self.assertIn("created_at", bm.to_dict())
        self.assertIn("updated_at", bm.to_dict())
        self.assertIn("__class__", bm.to_dict())


if __name__ == "__main__":
    unittest.main()
