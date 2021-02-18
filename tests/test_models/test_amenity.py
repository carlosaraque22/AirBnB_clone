#!/usr/bin/python3

"""Test class Amenity"""

from models.base_model import BaseModel
from models.amenity import Amenity
from datetime import datetime
import uuid
import unittest


class Testamenity(unittest.TestCase):
    """test for amenity class"""

    def test_class_name(self):
        """ tests if the class is named correctly"""

        amenity_example = Amenity()
        self.assertEqual(amenity_example.__class__.__name__, "Amenity")

    def test_inheritance(self):
        """Tests if class inherits from BaseModel"""

        amenity_example = Amenity()
        self.assertTrue(issubclass(amenity_example.__class__, BaseModel))

    def test_amenity_id_format(self):
        """test if UUID is a string"""
        id_nbr = BaseModel()
        self.assertIsInstance(id_nbr.id, str)

    def test_amenity_created_at_format(self):
        """test if created_at is datetime format"""
        date = BaseModel()
        self.assertIsInstance(date.created_at, datetime)

    def test_amenity_updated_at_format(self):
        """test if date and time updated are in datetime format"""
        date = BaseModel()
        self.assertIsInstance(date.updated_at, datetime)
