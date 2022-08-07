#!/usr/bin/python3
"""
This module contains the unittests for User class
"""
import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """
    Test for class User and its methods
    """
    def setUp(self):
        """
        Set up method
        """
        self.user1 = User()
        self.user2 = User()

    def tearDown(self):
        """
        Tear down method
        """
        pass

    def test_email(self):
        self.assertTrue(hasattr(self.user1, "email"))
        self.assertTrue(type(self.user1.email) is str)
        self.assertEqual(self.user1.email, "")
        User.email = "foo@gmail.com"
        self.assertEqual(self.user1.email, "foo@gmail.com")
        self.assertEqual(self.user1.email, self.user2.email)
        self.user1.email = "bar@gmail.com"
        self.assertEqual(self.user1.email, "bar@gmail.com")
        self.assertFalse(self.user1.email == self.user2.email)

    def test_password(self):
        self.assertTrue(hasattr(self.user1, "password"))
        self.assertTrue(type(self.user1.password) is str)
        self.assertEqual(self.user1.password, "")
        User.password = "password123"
        self.assertEqual(self.user1.password, "password123")
        self.assertEqual(self.user1.password, self.user2.password)
        self.user1.password = "123password"
        self.assertEqual(self.user1.password, "123password")
        self.assertFalse(self.user1.password == self.user2.password)

    def test_first_name(self):
        self.assertTrue(hasattr(self.user1, "first_name"))
        self.assertTrue(type(self.user1.first_name) is str)
        self.assertEqual(self.user1.first_name, "")
        User.first_name = "Shamso"
        self.assertEqual(self.user1.first_name, "Shamso")
        self.assertEqual(self.user1.first_name, self.user2.first_name)
        self.user1.first_name = "Eric"
        self.assertEqual(self.user1.first_name, "Eric")
        self.assertFalse(self.user1.first_name == self.user2.first_name)

    def test_last_name(self):
        self.assertTrue(hasattr(self.user1, "last_name"))
        self.assertTrue(type(self.user1.last_name) is str)
        self.assertEqual(self.user1.last_name, "")
        User.last_name = "Osman"
        self.assertEqual(self.user1.last_name, "Osman")
        self.assertEqual(self.user1.last_name, self.user2.last_name)
        self.user1.last_name = "Botchway"
        self.assertEqual(self.user1.last_name, "Botchway")
        self.assertFalse(self.user1.last_name == self.user2.last_name)

    def test_isinstance(self):
        self.assertTrue(isinstance(self.user1, BaseModel))
        self.assertFalse(type(self.user1) is BaseModel)

if __name__ == '__main__':
    unittest.main()
