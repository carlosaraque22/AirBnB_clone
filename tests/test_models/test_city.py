#!/usr/bin/python3

"""Test class City"""

import models
from models.base_model import BaseModel
from models.city import City
import unittest


class Testcity(unittest.TestCase):
    """tests for the City class"""

    def test_docstring(self):
        """ function test_docstring """
        msj = "Module doesnt have docstring"
        obj = models.city.__doc__
        self.assertIsNotNone(obj, msj)
        msj = "Classes doesnt have docstring"
        self.assertIsNotNone(obj, msj)

    def test_class_name(self):
        """Tests if class is named correctly"""

        city_example = City()
        self.assertEqual(city_example.__class__.__name__, "City")

    def test_inheritance(self):
        """Tests if Class inherits from BaseModel"""

        city_example = City()
        self.assertTrue(issubclass(city_example.__class__, BaseModel))
