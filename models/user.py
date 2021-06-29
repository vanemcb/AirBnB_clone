#!/usr/bin/python3
""" Module class User
    This module is for the project 0x00. AirBnB clone - The console
    proposed by Holberton school to learn how a web page works.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class that inherits from
        BaseModel.
    Args:
        None
    Attributes:
        None
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
