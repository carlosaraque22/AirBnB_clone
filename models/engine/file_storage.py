#!/usr/bin/python3

""" Module File Storage """

import json
from models.base_model import BaseModel
from os import path

class FileStorage:

    """ This class serializes instances to a JSON file and"""
    """ deserializes JSON file to instances """
    """__file_path: string - path to the JSON file (ex: file.json)"""
    """__objects: dictionary - empty but will store all objects by"""
    """ <class name>.id ex: BaseModel.12121212"""


    __file_path = "objects_contents_storage"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, mode="w", encoding="utf-8") as jason_file:
            jason_file.write(json.dumps(__objects))

    def reload(self):
        """deserializes the JSON file to __objects, only if the JSON file"""
        """__file_path exists ; otherwise, do nothing. If the file doesnt"""
        """exist, no exception should be raised"""
        if path.exists(self.__file_path):
            with open(self.__file_path, mode="r", encoding="utf-8") as f:
                __objects = (json.load(f))
