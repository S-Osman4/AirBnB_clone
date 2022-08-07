#!/usr/bin/python3
"""
This module contains unit tests for class BaseModel
"""
from datetime import datetime
import io
from models.amenity import Amenity
from models.base_model import BaseModel
import sys
import pep8
import unittest


class TestAmenity(unittest.TestCase):
    """test for class Amenity
    """
    def setUp(self):
        """Set up method"""
        self.amenity1 = Amenity()
        self.amenity2 = Amenity()

    def test_uuid(self):
        self.assertNotEqual(self.amenity1.id, self.amenity2.id)
        self.assertTrue(hasattr(self.amenity1, "id"))
        self.assertEqual(type(self.amenity1.id), str)
        self.assertEqual(type(self.amenity2.id), str)

    def test_instance(self):
        self.assertTrue(isinstance(self.amenity1, Amenity))
        self.assertTrue(isinstance(self.amenity1, BaseModel))

    def test_type(self):
        self.assertEqual(type(self.amenity1), Amenity)
        self.assertEqual(type(self.amenity2), Amenity)

    def test_created_at(self):
        self.assertTrue(hasattr(self.amenity1, "created_at"))
        self.assertEqual(type(self.amenity1.created_at), type(datetime.now()))
        self.assertNotEqual(self.amenity1.created_at, self.amenity1.updated_at)

    def test_updated_at(self):
        self.assertTrue(hasattr(self.amenity1, "updated_at"))
        self.assertEqual(type(self.amenity1.updated_at), type(datetime.now()))

    def test_str(self):
        self.amenity1.name = "Swimming Pool"
        expected = "[{}] ({}) {}".format(
            self.amenity1.__class__.__name__,
            self.amenity1.id,
            self.amenity1.__dict__
        )
        a_io = io.StringIO()
        sys.stdout = a_io
        print(self.amenity1, end="")
        self.assertEqual(expected, a_io.getvalue())
        sys.stdout = sys.__stdout__

    def test_name(self):
        self.assertTrue(hasattr(self.amenity1, "name"))
        self.assertEqual(self.amenity1.name, "")
        Amenity.name = "Swimming Pool"
        self.assertEqual(Amenity.name, "Swimming Pool")
        self.assertEqual(self.amenity1.name, "Swimming Pool")
        self.amenity1.name = "Hot Tub"
        self.assertEqual(self.amenity1.name, "Hot Tub")
        Amenity.name = "Fireplace"
        self.assertEqual(self.amenity2.name, "Fireplace")


    def test_to_dict(self):
        self.amenity1.name = "Fireplace"
        model_json = self.amenity1.to_dict()
        amenity1_dict = self.amenity1.__dict__.copy()
        self.assertEqual(model_json['created_at'],
                         amenity1_dict['created_at'].isoformat())
        self.assertEqual(model_json['updated_at'],
                         amenity1_dict['updated_at'].isoformat())
        amenity1_dict['created_at'] = (amenity1_dict['created_at']).isoformat()
        amenity1_dict['updated_at'] = (amenity1_dict['updated_at']).isoformat()
        amenity1_dict['__class__'] = 'Amenity'
        self.assertDictEqual(amenity1_dict, model_json)

    def test_init_with_kwargs(self):
        self.amenity1.name = "Swimming Pool"
        model_json = self.amenity1.to_dict()
        my_new_amenity = Amenity(**model_json)
        self.assertDictEqual(model_json, my_new_amenity.to_dict())
        self.assertIn("name", my_new_amenity.to_dict())
        self.assertEqual(my_new_amenity.name, "Swimming Pool")
        self.assertIsNot(self.amenity1, my_new_amenity)
        
    def test_pep8_conformance_model(self):
        """
        Test that we conform to PEP8.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0, "Fix pep8 in amenity")
        
    def test_docstring(self):
        """
        Testing docstring
        """
        self.assertIsNotNone(Amenity.__doc__)
        
    

if __name__ == '__main__':
    unittest.main()
