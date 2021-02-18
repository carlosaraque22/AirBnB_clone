#!/usr/bin/python3

"""Test class City"""

from models.base_model import BaseModel
from models.city import City
from datetime import datetime
import uuid
import unittest


class Testcity(unittest.TestCase):
    """tests for the City class"""

    def test_class_name(self):
        """Tests if class is named correctly"""

        city_example = City()
        self.assertEqual(city_example.__class__.__name__, "City")

    def test_inheritance(self):
        """Tests if Class inherits from BaseModel"""

        city_example = City()
        self.assertTrue(issubclass(city_example.__class__, BaseModel))

    def test_city_id_format(self):
        """test if UUID is a string"""
        id_nbr = BaseModel()
        self.assertIsInstance(id_nbr.id, str)

    def test_city_created_at_format(self):
        """test if created_at is datetime format"""
        date = BaseModel()
        self.assertIsInstance(date.created_at, datetime)

    def test_city_updated_at_format(self):
        """test if date and time updated are in datetime format"""
        date = BaseModel()
        self.assertIsInstance(date.updated_at, datetime)
