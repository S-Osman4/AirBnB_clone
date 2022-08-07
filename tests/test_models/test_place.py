#!/usr/bin/python3
"""
This module contains the unittests for Place class
"""
import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    Test for class Place and its methods
    """
    def setUp(self):
        """
        Set up method
        """
        self.place1 = Place()
        self.place2 = Place()

    def tearDown(self):
        """
        Tear down method
        """
        pass

    def test_city_id(self):
        self.assertTrue(hasattr(self.place1, "city_id"))
        self.assertTrue(type(self.place1.city_id) is str)
        self.assertEqual(self.place1.city_id, "")
        Place.city_id = "Nairobi"
        self.assertEqual(self.place1.city_id, "Nairobi")
        self.assertEqual(self.place1.city_id, self.place2.city_id)
        self.place1.city_id = "Mombasa"
        self.assertEqual(self.place1.city_id, "Mombasa")
        self.assertFalse(self.place1.city_id == self.place2.city_id)

    def test_user_id(self):
        self.assertTrue(hasattr(self.place1, "user_id"))
        self.assertTrue(type(self.place1.user_id) is str)
        self.assertEqual(self.place1.user_id, "")
        Place.user_id = "ShamsoOsman"
        self.assertEqual(self.place1.user_id, "ShamsoOsman")
        self.assertEqual(self.place1.user_id, self.place2.user_id)
        self.place1.user_id = "EricBotchway"
        self.assertEqual(self.place1.user_id, "EricBotchway")
        self.assertFalse(self.place1.user_id == self.place2.user_id)

    def test_name(self):
        self.assertTrue(hasattr(self.place1, "name"))
        self.assertTrue(type(self.place1.name) is str)
        self.assertEqual(self.place1.name, "")
        Place.name = "Shamso Osman"
        self.assertEqual(self.place1.name, "Shamso Osman")
        self.assertEqual(self.place1.name, self.place2.name)
        self.place1.name = "Eric Botchway"
        self.assertEqual(self.place1.name, "Eric Botchway")
        self.assertFalse(self.place1.name == self.place2.name)

    def test_description(self):
        self.assertTrue(hasattr(self.place1, "description"))
        self.assertTrue(type(self.place1.description) is str)
        self.assertEqual(self.place1.description, "")
        Place.description = "Awesome place"
        self.assertEqual(self.place1.description, "Awesome place")
        self.assertEqual(self.place1.description, self.place2.description)
        self.place1.description = "Decent place"
        self.assertEqual(self.place1.description, "Decent place")
        self.assertFalse(self.place1.description == self.place2.description)

    def test_number_rooms(self):
        self.assertTrue(hasattr(self.place1, "number_rooms"))
        self.assertTrue(type(self.place1.number_rooms) is int)
        self.assertEqual(self.place1.number_rooms, 0)
        Place.number_rooms = 2
        self.assertEqual(self.place1.number_rooms, 2)
        self.assertEqual(self.place1.number_rooms, self.place2.number_rooms)
        self.place1.number_rooms = 5
        self.assertEqual(self.place1.number_rooms, 5)
        self.assertFalse(self.place1.number_rooms == self.place2.number_rooms)

    def test_number_bathrooms(self):
        self.assertTrue(hasattr(self.place1, "number_bathrooms"))
        self.assertTrue(type(self.place1.number_bathrooms) is int)
        self.assertEqual(self.place1.number_bathrooms, 0)
        Place.number_bathrooms = 1
        self.assertEqual(self.place1.number_bathrooms, 1)
        self.assertEqual(self.place1.number_bathrooms,
                         self.place2.number_bathrooms)
        self.place1.number_bathrooms = 2
        self.assertEqual(self.place1.number_bathrooms, 2)
        self.assertFalse(self.place1.number_bathrooms ==
                         self.place2.number_bathrooms)

    def test_max_guest(self):
        self.assertTrue(hasattr(self.place1, "max_guest"))
        self.assertTrue(type(self.place1.max_guest) is int)
        self.assertEqual(self.place1.max_guest, 0)
        Place.max_guest = 5
        self.assertEqual(self.place1.max_guest, 5)
        self.assertEqual(self.place1.max_guest,
                         self.place2.max_guest)
        self.place1.max_guest = 10
        self.assertEqual(self.place1.max_guest, 10)
        self.assertFalse(self.place1.max_guest ==
                         self.place2.max_guest)

    def test_price_by_night(self):
        self.assertTrue(hasattr(self.place1, "price_by_night"))
        self.assertTrue(type(self.place1.price_by_night) is int)
        self.assertEqual(self.place1.price_by_night, 0)
        Place.price_by_night = 100
        self.assertEqual(self.place1.price_by_night, 100)
        self.assertEqual(self.place1.price_by_night,
                         self.place2.price_by_night)
        self.place1.price_by_night = 200
        self.assertEqual(self.place1.price_by_night, 200)
        self.assertFalse(self.place1.price_by_night ==
                         self.place2.price_by_night)

    def test_latitude(self):
        self.assertTrue(hasattr(self.place1, "latitude"))
        self.assertTrue(type(self.place1.latitude) is float)
        self.assertEqual(self.place1.latitude, 0.0)
        Place.latitude = 100.0
        self.assertEqual(self.place1.latitude, 100.0)
        self.assertEqual(self.place1.latitude, self.place2.latitude)
        self.place1.latitude = 80.0
        self.assertEqual(self.place1.latitude, 80.0)
        self.assertFalse(self.place1.latitude ==
                         self.place2.latitude)

    def test_longitude(self):
        self.assertTrue(hasattr(self.place1, "longitude"))
        self.assertTrue(type(self.place1.longitude) is float)
        self.assertEqual(self.place1.longitude, 0.0)
        Place.longitude = 100.0
        self.assertEqual(self.place1.longitude, 100.0)
        self.assertEqual(self.place1.longitude, self.place2.longitude)
        self.place1.longitude = 80.0
        self.assertEqual(self.place1.longitude, 80.0)
        self.assertFalse(self.place1.longitude ==
                         self.place2.longitude)

    def test_amenity_ids(self):
        self.assertTrue(hasattr(self.place1, "amenity_ids"))
        self.assertTrue(type(self.place1.amenity_ids) is list)
        self.assertEqual(self.place1.amenity_ids, [])
        Place.amenity_ids = ["Toothpaste"]
        self.assertEqual(self.place1.amenity_ids, ["Toothpaste"])
        self.assertEqual(self.place1.amenity_ids, self.place2.amenity_ids)
        self.place1.amenity_ids = ["Toothbrush"]
        self.assertEqual(self.place1.amenity_ids, ["Toothbrush"])
        self.assertFalse(self.place1.amenity_ids ==
                         self.place2.amenity_ids)

    def test_isinstance(self):
        self.assertTrue(isinstance(self.place1, BaseModel))
        self.assertFalse(type(self.place1) is BaseModel)

if __name__ == '__main__':
    unittest.main()
