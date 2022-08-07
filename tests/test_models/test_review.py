#!/usr/bin/python3
"""
This module contains unit tests for class Review
"""
from datetime import datetime
import io
from models.base_model import BaseModel
from models.place import Place
from models.review import Review
from models.user import User
import sys
import unittest


class TestReview(unittest.TestCase):
    """test for class Review
    """
    def setUp(self):
        """Set up method"""
        self.review1 = Review()
        self.review2 = Review()

    def tearDown(self):
        """Tear down method"""
        pass

    def test_uuid(self):
        self.assertNotEqual(self.review1.id, self.review2.id)
        self.assertTrue(hasattr(self.review1, "id"))
        self.assertEqual(type(self.review1.id), str)

    def test_instance(self):
        self.assertTrue(isinstance(self.review1, Review))
        self.assertTrue(isinstance(self.review1, BaseModel))

    def test_type(self):
        self.assertEqual(type(self.review1), Review)

    def test_created_at(self):
        self.assertTrue(hasattr(self.review1, "created_at"))
        self.assertEqual(type(self.review1.created_at), type(datetime.now()))

    def test_updated_at(self):
        self.assertTrue(hasattr(self.review1, "updated_at"))
        self.assertEqual(type(self.review1.updated_at), type(datetime.now()))

    def test_str(self):
        expected = "[{}] ({}) {}".format(
            self.review1.__class__.__name__,
            self.review1.id,
            self.review1.__dict__
        )
        a_io = io.StringIO()
        sys.stdout = a_io
        print(self.review1, end="")
        self.assertEqual(expected, a_io.getvalue())
        sys.stdout = sys.__stdout__

    def test_place_id(self):
        self.assertTrue(hasattr(self.review1, "place_id"))
        self.assertEqual(Review.place_id, "")
        self.assertEqual(self.review1.place_id, "")
        a = Place()
        self.review1.place_id = a.id
        self.assertEqual(self.review1.place_id, a.id)
        self.assertEqual(type(self.review1.place_id), str)

    def test_user_id(self):
        self.assertTrue(hasattr(self.review1, "user_id"))
        self.assertEqual(Review.user_id, "")
        self.assertEqual(self.review1.user_id, "")
        a = User()
        self.review1.user_id = a.id
        self.assertEqual(self.review1.user_id, a.id)
        self.assertEqual(type(self.review1.user_id), str)

    def test_text(self):
        self.assertTrue(hasattr(self.review1, "text"))
        self.assertEqual(Review.text, "")
        self.assertEqual(self.review1.text, "")
        self.review1.text = "This is a review"
        self.assertEqual(self.review1.text, "This is a review")
        self.assertEqual(self.review2.text, "")
        Review.text = "No review yet"
        self.assertEqual(self.review2.text, "No review yet")

    def test_to_dict(self):
        a = Place()
        b = User()
        self.review1.place_id = a.id
        self.review1.user_id = b.id
        self.review1.text = "Leave a review!"
        model_json = self.review1.to_dict()
        review_dict = self.review1.__dict__.copy()
        self.assertEqual(model_json['created_at'],
                         review_dict['created_at'].isoformat())
        self.assertEqual(model_json['updated_at'],
                         review_dict['updated_at'].isoformat())
        review_dict['created_at'] = review_dict['created_at'].isoformat()
        review_dict['updated_at'] = review_dict['updated_at'].isoformat()
        review_dict['__class__'] = self.review1.__class__.__name__
        self.assertDictEqual(review_dict, model_json)

    def test_init_with_kwargs(self):
        a = Place()
        b = User()
        self.review1.place_id = a.id
        self.review1.user_id = b.id
        self.review1.text = "Leave a review!"
        self.review1.stars = 5
        model_json = self.review1.to_dict()
        my_new_review = Review(**model_json)
        self.assertDictEqual(model_json, my_new_review.to_dict())
        self.assertIn("place_id", my_new_review.to_dict())
        self.assertIn("user_id", my_new_review.to_dict())
        self.assertIn("text", my_new_review.to_dict())
        self.assertIn("stars", my_new_review.to_dict())
        self.assertIsNot(self.review1, my_new_review)

if __name__ == '__main__':
    unittest.main()
