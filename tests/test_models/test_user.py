#!/usr/bin/python3

"""Test class User"""

from models.base_model import BaseModel
import models
from models.user import User
import unittest


class Testuser(unittest.TestCase):
    """tests for the User class"""

    def test_docstring(self):
        """ function test_docstring """
        msj = "Module doesnt have docstring"
        obj = models.user.__doc__
        self.assertIsNotNone(obj, msj)
        msj = "Class doesnt have docstring"
        self.assertIsNotNone(obj, msj)

    def test_class_name(self):
        """Tests if class is named correctly"""
        user_example = User()
        self.assertEqual(user_example.__class__.__name__, "User")

    def test_inheritance(self):
        """Tests if Class inherits from BaseModel"""
        user_example = User()
        self.assertTrue(issubclass(user_example.__class__, BaseModel))
