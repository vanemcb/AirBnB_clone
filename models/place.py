#!/usr/bin/python3
""" Module class Place
    This module is for the project 0x00. AirBnB clone - The console
    proposed by Holberton school to learn how a web page works.
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Place class that inherits from
        BaseModel.
    Args:
        None
    Attributes:
        None
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
