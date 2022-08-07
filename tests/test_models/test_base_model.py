#!/usr/bin/python3
"""
This module contains unit tests for class BaseModel
"""
import unittest
import io
import sys
from datetime import datetime
from models.base_model import BaseModel
import models


class TestBaseModel(unittest.TestCase):
    """test for class BaseModel and its methods
    """
    def setUp(self):
        """Set up method"""
        self.base1 = BaseModel()
        self.base2 = BaseModel()

    def tearDown(self):
        """Tear down method"""
        pass

    def test_uuid(self):
        self.assertNotEqual(self.base1.id, self.base2.id)
        self.assertTrue(hasattr(self.base1, "id"))
        self.assertEqual(type(self.base1.id), str)
        self.assertEqual(type(self.base2.id), str)

    def test_instance(self):
        self.assertTrue(isinstance(self.base1, BaseModel))
        self.assertTrue(isinstance(self.base2, BaseModel))

    def test_type(self):
        self.assertEqual(type(self.base1), BaseModel)

    def test_created_at(self):
        self.assertTrue(hasattr(self.base1, "created_at"))
        self.assertEqual(type(self.base1.created_at), type(datetime.now()))

    def test_updated_at(self):
        self.assertTrue(hasattr(self.base1, "updated_at"))
        self.assertEqual(type(self.base1.updated_at), type(datetime.now()))

    def test_str(self):
        expected = "[{}] ({}) {}".format(
            self.base1.__class__.__name__,
            self.base1.id,
            self.base1.__dict__
        )
        a_io = io.StringIO()
        sys.stdout = a_io
        print(self.base1, end="")
        self.assertEqual(expected, a_io.getvalue())
        sys.stdout = sys.__stdout__

    def test_save(self):
        time = self.base1.updated_at
        self.base1.save()
        self.assertFalse(time == self.base1.updated_at)

    def test_update(self):
        self.base1.name = "Holberton"
        self.assertTrue(hasattr(self.base1, "name"))

    def test_to_dict(self):
        self.base2.name = "Holberton"
        model_json = self.base2.to_dict()
        base1_dict = self.base2.__dict__.copy()
        self.assertEqual(
                model_json['created_at'],
                base1_dict['created_at'].isoformat()
                )
        self.assertEqual(
                model_json['updated_at'],
                base1_dict['updated_at'].isoformat()
                )
        base1_dict['created_at'] = base1_dict['created_at'].isoformat()
        base1_dict['updated_at'] = base1_dict['updated_at'].isoformat()
        base1_dict['__class__'] = self.base1.__class__.__name__
        self.assertDictEqual(base1_dict, model_json)

    def test_init_with_kwargs(self):
        self.base1.name = "Holberton"
        model_json = self.base1.to_dict()
        my_new_model = BaseModel(**model_json)
        self.assertDictEqual(model_json, my_new_model.to_dict())
        self.assertIn("name", my_new_model.to_dict())
        self.assertIsNot(self.base1, my_new_model)

    def test_storage(self):
        obj_dict = models.storage.all()
        self.assertTrue(obj_dict)

if __name__ == '__main__':
    unittest.main()
