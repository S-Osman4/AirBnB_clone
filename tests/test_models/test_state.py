#!/usr/bin/python3
"""
This module contains unit tests for class State
"""
from datetime import datetime
import io
from models.base_model import BaseModel
from models.state import State
import sys
import unittest


class TestState(unittest.TestCase):
    """test for class State
    """
    def setUp(self):
        """Set up method"""
        self.state1 = State()
        self.state2 = State()

    def tearDown(self):
        """Tear down method"""
        pass

    def test_uuid(self):
        self.assertNotEqual(self.state1.id, self.state2.id)
        self.assertTrue(hasattr(self.state1, "id"))
        self.assertEqual(type(self.state1.id), str)
        self.assertEqual(type(self.state2.id), str)

    def test_instance(self):
        self.assertTrue(isinstance(self.state1, State))
        self.assertTrue(isinstance(self.state1, BaseModel))

    def test_type(self):
        self.assertEqual(type(self.state1), State)
        self.assertEqual(type(self.state2), State)

    def test_created_at(self):
        self.assertTrue(hasattr(self.state1, "created_at"))
        self.assertEqual(type(self.state1.created_at), type(datetime.now()))
        self.assertNotEqual(self.state1.created_at, self.state2.created_at)
        self.assertNotEqual(self.state1.created_at, self.state1.updated_at)

    def test_updated_at(self):
        self.assertTrue(hasattr(self.state1, "updated_at"))
        self.assertEqual(type(self.state1.updated_at), type(datetime.now()))

    def test_str(self):
        expected = "[{}] ({}) {}".format(
            self.state1.__class__.__name__,
            self.state1.id,
            self.state1.__dict__
        )
        a_io = io.StringIO()
        sys.stdout = a_io
        print(self.state1, end="")
        self.assertEqual(expected, a_io.getvalue())
        sys.stdout = sys.__stdout__

    def test_name(self):
        self.assertTrue(hasattr(self.state1, "name"))
        self.assertEqual(self.state1.name, "")
        State.name = "California"
        self.assertEqual(State.name, "California")
        self.assertEqual(self.state1.name, "California")
        self.state1.name = "Massachusetts"
        self.assertEqual(self.state1.name, "Massachusetts")
        State.name = "Connecticut"
        self.assertEqual(self.state2.name, "Connecticut")

    def test_to_dict(self):
        self.state1.name = "California"
        model_json = self.state1.to_dict()
        state1_dict = self.state1.__dict__.copy()
        self.assertEqual(model_json['created_at'],
                         state1_dict['created_at'].isoformat())
        self.assertEqual(model_json['updated_at'],
                         state1_dict['updated_at'].isoformat())
        state1_dict['created_at'] = state1_dict['created_at'].isoformat()
        state1_dict['updated_at'] = state1_dict['updated_at'].isoformat()
        state1_dict['__class__'] = self.state1.__class__.__name__
        self.assertDictEqual(state1_dict, model_json)

    def test_init_with_kwargs(self):
        self.state1.name = "California"
        model_json = self.state1.to_dict()
        my_new_state = State(**model_json)
        self.assertDictEqual(model_json, my_new_state.to_dict())
        self.assertIn("name", my_new_state.to_dict())
        self.assertEqual(my_new_state.name, "California")
        self.assertIsNot(self.state1, my_new_state)

if __name__ == '__main__':
    unittest.main()
