#!/usr/bin/python3
"""
This module contains the tests for FileStorage class
"""
import unittest
import io
import sys
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestFileStorage(unittest.TestCase):
    """
    Test for class FileStorage and its methods
    """
    def setUp(self):
        """
        Set up method
        """
        self.storage = FileStorage()

    def tearDown(self):
        """
        Tear down method
        """
        pass

    def test_private_class_attributes(self):
        with self.assertRaises(AttributeError):
            print(self.storage.__objects)
        with self.assertRaises(AttributeError):
            print(self.storage.__file_path)

    def test_file_path(self):
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")

    def test_objects(self):
        self.assertIs(type(self.storage._FileStorage__objects), dict)

    def test_all(self):
        obj_dict = self.storage.all()
        self.assertTrue(type(obj_dict) is dict)

    def test_new(self):
        base1 = BaseModel()
        city1 = City()
        base1_id = "{}.{}".format(base1.__class__.__name__, base1.id)
        city1_id = "{}.{}".format(city1.__class__.__name__, city1.id)
        obj_dict = self.storage.all()
        self.assertTrue(base1_id in obj_dict)
        self.assertTrue(obj_dict[base1_id] is base1)
        self.assertTrue(city1_id in obj_dict)
        self.assertTrue(obj_dict[city1_id] is city1)

    def test_save(self):
        base1 = BaseModel()
        city1 = City()
        base1_id = "{}.{}".format(base1.__class__.__name__, base1.id)
        city1_id = "{}.{}".format(city1.__class__.__name__, city1.id)
        obj_dict_presave = self.storage.all()
        base1.save()
        self.storage.reload()
        obj_dict_postsave = self.storage.all()
        self.assertTrue(base1_id in obj_dict_postsave)
        self.assertTrue(city1_id in obj_dict_postsave)
        self.assertTrue(obj_dict_postsave == obj_dict_presave)

    def test_reload(self):
        base1 = BaseModel()
        city1 = City()
        base1_id = "{}.{}".format(base1.__class__.__name__, base1.id)
        city1_id = "{}.{}".format(city1.__class__.__name__, city1.id)
        obj_dict_presave = self.storage.all()
        base1.save()
        self.storage.reload()
        obj_dict_postsave = self.storage.all()
        self.assertTrue(base1_id in obj_dict_postsave)
        self.assertTrue(city1_id in obj_dict_postsave)
        self.assertTrue(obj_dict_postsave == obj_dict_presave)

if __name__ == '__main__':
    unittest.main()
