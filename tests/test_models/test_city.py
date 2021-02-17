#!/usr/bin/python3

"""Test class City"""

from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
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
