#!/usr/bin/python3

"""This class defines all common attributes/methods for other classes"""

import uuid
from datetime import datetime

class BaseModel:

    """class containing Public instance attributes"""

    def __init__(self, **argdict):

        """generate unique id converted to str"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if argdict:
            for key, value in argdict.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = value

    def to_dict(self, ):

        """create a dictionary"""
        

    def __str__(self):

        """str repr of class"""
        return "[BaseModel] ({}) <{}>" .format(self.id, self.__dict__)
