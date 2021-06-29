#!/usr/bin/python3
""" Module class State
    This module is for the project 0x00. AirBnB clone - The console
    proposed by Holberton school to learn how a web page works.
"""
from models.base_model import BaseModel


class State(BaseModel):
    """State class that inherits from
        BaseModel.
    Args:
        None
    Attributes:
        None
    """
    name = ""
