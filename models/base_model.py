#!/usr/bin/python3
""" Module class BaseModel
    This module is for the project 0x00. AirBnB clone - The console
    proposed by Holberton school to learn how a web page works.
"""
import uuid
from datetime import datetime
from __init__ import storage


class BaseModel:
    """BaseModel class that defines all common
        attributes/methods for other classes.
    Args:
        None
    Attributes:
        None
    """

    def __init__(self, *args, **kwargs):
        """ Initializator method """
        if not kwargs and not args:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new()
        else:
            del kwargs["__class__"]
            kwargs["created_at"] = datetime.strptime(
                kwargs["created_at"], '%Y-%m-%dT%H:%M:%S.%f')
            kwargs["updated_at"] = datetime.strptime(
                kwargs["updated_at"], '%Y-%m-%dT%H:%M:%S.%f')
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """ Print class format """
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """ Updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values
        of __dict__ of the instance:
        """
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = type(self).__name__
        return new_dict
