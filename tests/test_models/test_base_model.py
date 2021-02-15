#!/usr/bin/python3

"""Unittest for base model module."""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid

class TestBaseModel(unittest.TestCase):
    """ test the base model class"""

    def test_base_model_id_format(self):
       """check if UUID is a string"""
       id_nbr = BaseModel()
        self.assertIsInstance(id_nbr.id, str)


    def test_base_model_created_at_format(self):
        """check if created_at is datetime format"""
        date = BaseModel()
        self.assertIsInstance(date.created_at, datetime)

    def test_base_model_updated_at_format(self):
        """check if date and time updated are in datetime format"""
        date = BaseModel()
        self.assertIsInstance(date.updated_at, datetime)

    
