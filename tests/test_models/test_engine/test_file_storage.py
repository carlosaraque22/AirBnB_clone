#!/usr/bin/python3

""" Module to test class File Storage"""

import unittest
import json
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

        dict_storage = FileStorage()
        new_dict_storage = self.storage.all()
        self.assertEqual(type(dict_storage), new_dict_storage)
