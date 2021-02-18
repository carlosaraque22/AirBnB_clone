#!/usr/bin/python3

"""Test class Review"""

from models.base_model import BaseModel
from models.review import Review
from datetime import datetime
import uuid
import unittest


class Testreview(unittest.TestCase):
    """tests for the Review class"""

    def test_class_name(self):
        """Tests if class is named correctly"""

        review_example = Review()
        self.assertEqual(review_example.__class__.__name__, "Review")

    def test_inheritance(self):
        """Tests if Class inherits from BaseModel"""

        review_example = Review()
        self.assertTrue(issubclass(review_example.__class__, BaseModel))

    def test_review_id_format(self):
        """test if UUID is a string"""
        id_nbr = BaseModel()
        self.assertIsInstance(id_nbr.id, str)

    def test_review_created_at_format(self):
        """test if created_at is datetime format"""
        date = BaseModel()
        self.assertIsInstance(date.created_at, datetime)

    def test_review_updated_at_format(self):
        """test if date and time updated are in datetime format"""
        date = BaseModel()
        self.assertIsInstance(date.updated_at, datetime)
