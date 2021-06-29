#!/usr/bin/python3
""" Module class Amenity
    This module is for the project 0x00. AirBnB clone - The console
    proposed by Holberton school to learn how a web page works.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class that inherits from
        BaseModel.
    Args:
        None
    Attributes:
        None
    """
    name = ""
