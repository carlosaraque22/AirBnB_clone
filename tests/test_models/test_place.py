#!/usr/bin/python3

"""Test class Place"""

from models.base_model import BaseModel
from datetime import datetime
import uuid
from models.place import Place
import unittest


class Testplace(unittest.TestCase):
    """tests for the Place class"""

    def test_class_name(self):
        """Tests if class is named correctly"""

        place_example = Place()
        self.assertEqual(place_example.__class__.__name__, "Place")

    def test_inheritance(self):
        """Tests if Class inherits from BaseModel"""

        place_example = Place()
        self.assertTrue(issubclass(place_example.__class__, BaseModel))

    def test_place_id_format(self):
        """test if UUID is a string"""
        id_nbr = BaseModel()
        self.assertIsInstance(id_nbr.id, str)

    def test_place_created_at_format(self):
        """test if created_at is datetime format"""
        date = BaseModel()
        self.assertIsInstance(date.created_at, datetime)

    def test_place_updated_at_format(self):
        """test if date and time updated are in datetime format"""
        date = BaseModel()
        self.assertIsInstance(date.updated_at, datetime)
