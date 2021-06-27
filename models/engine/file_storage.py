#!/usr/bin/python3
""" Module class FileStorage
    This module is for the project 0x00. AirBnB clone - The console
    proposed by Holberton school to learn how a web page works.
"""

"""from datetime import datetime
import uuid
import os, sys
p = os.path.abspath('..')
sys.path.insert(1, p)
from models.base_model import BaseModel"""
import json

class FileStorage:
    """FileStorage class that serializes instances to a JSON file
    and deserializes JSON file to instances
    Args:
        None
    Attributes:
        None
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        from models.base_model import BaseModel
        my_dict_copy = FileStorage.__objects.copy()
        for obj_key, obj_value in FileStorage.__objects.items():
            my_dict_copy[obj_key] = BaseModel(**obj_value)
        return my_dict_copy

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        FileStorage.__objects[type(obj).__name__ + "." + obj.id] = obj.to_dict()

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        with open(FileStorage.__file_path, "w", encoding='utf-8') as my_file:
            my_file.write(json.dumps(FileStorage.__objects))

    def reload(self):
        """ Deserializes the JSON file to __objects  """
        from models.base_model import BaseModel
        try:
            with open(FileStorage.__file_path, "r", encoding='utf-8') as my_file2:
                FileStorage.__objects = json.loads(my_file2.read())

        except:
            pass
