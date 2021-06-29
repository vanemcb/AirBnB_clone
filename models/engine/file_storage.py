#!/usr/bin/python3
""" Module class FileStorage
    This module is for the project 0x00. AirBnB clone - The console
    proposed by Holberton school to learn how a web page works.
"""
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
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        FileStorage.__objects[type(obj).__name__ + "." + obj.id] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        from models.base_model import BaseModel
        with open(FileStorage.__file_path, "w", encoding='utf-8') as my_file:
            my_dict_copy = FileStorage.__objects.copy()

            for obj_key, obj_value in FileStorage.__objects.items():
                my_dict_copy[obj_key] = obj_value.to_dict()
            my_file.write(json.dumps(my_dict_copy))

    def reload(self):
        """ Deserializes the JSON file to __objects  """
        from models.base_model import BaseModel
        try:
            with open(FileStorage.__file_path, "r") as my_file2:
                my_dict = json.loads(my_file2.read())

            for obj_key, obj_value in my_dict.items():
                FileStorage.__objects[obj_key] = BaseModel(**obj_value)

        except FileNotFoundError:
            pass
