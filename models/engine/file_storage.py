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


    __file_path = "file.json"
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
        for key, value in self.__objects.items():
            if not isinstance(value, dict):
                self.objects[key] = value.to_dict()
        with open(self.__file_path, "w") as file:
            json.dumps(self.__objects, file)

    def reload(self):
        """deserializes the JSON file to __objects, only if the JSON file"""
        """__file_path exists ; otherwise, do nothing. If the file doesnt"""
        """exist, no exception should be raised"""
        try:
            with open(self.__file_path, "r") as file:
                serializable_file = json.load(file)
            for key, value in serializable_file.items():
                self.__objects[key] = eval(value['__class__'])(**value)
        except FileNotFoundError:
            pass
