#!/usr/bin/python3

"""Test class Amenity"""

from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
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
