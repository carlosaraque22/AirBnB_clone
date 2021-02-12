#!/usr/bin/python3

"""This class defines all common attributes/methods for other classes"""

import uuid

class BaseModel:

    """class containing Public instance attributes"""

    def __init__(self):

        """generate unique id converted to str"""
        format_time = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def to_dict(self, ):

        """create a dictionary"""
        

    def __str__(self):

        """str repr of class"""
        return "[BaseModel] ({}) <{}>" .format(self.id, self.__dict__)
