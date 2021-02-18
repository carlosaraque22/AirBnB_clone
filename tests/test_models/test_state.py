#!/usr/bin/python3

"""Test class State"""

from models.base_model import BaseModel
from models.state import State
from datetime import datetime
import uuid
import unittest


class Teststate(unittest.TestCase):
    """tests for the Place class"""

    def test_class_name(self):
        """Tests if class is named correctly"""

        state_example = State()
        self.assertEqual(state_example.__class__.__name__, "State")

    def test_inheritance(self):
        """Tests if Class inherits from BaseModel"""

        state_example = State()
        self.assertTrue(issubclass(state_example.__class__, BaseModel))

    def test_state_id_format(self):
        """test if UUID is a string"""
        id_nbr = BaseModel()
        self.assertIsInstance(id_nbr.id, str)

    def test_state_created_at_format(self):
        """test if created_at is datetime format"""
        date = BaseModel()
        self.assertIsInstance(date.created_at, datetime)

    def test_state_updated_at_format(self):
        """test if date and time updated are in datetime format"""
        date = BaseModel()
        self.assertIsInstance(date.updated_at, datetime)
