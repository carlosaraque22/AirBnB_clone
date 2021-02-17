#!/usr/bin/python3

""" Module to test class File Storage"""

import json
import unittest
from models.base_model import BaseModel
from os import path
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):

    """test File Storage"""

    def test_all_methods(self):
        """test all methods"""
        Dict_storage = FileStorage()
        new_dict_storage = Dict_storage.all()
        self.assertEqual(type(new_dict_storage), dict)
