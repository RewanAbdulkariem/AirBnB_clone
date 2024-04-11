#!/usr/bin/python3
"""
place.py
Created by Rewan Abdulkariem @11/4/2024
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Represents a place.

    Attributes:
        city_id (str): The id of the city where the place is located.
        user_id (str): The id of the user who owns the place.
        name (str): The name of the place. Default is an empty string.
        description (str): The description of the place.
        number_rooms (int): The number of rooms in the place.
        number_bathrooms (int): The number of bathrooms in the place.
        max_guest (int): The maximum number of guests the place can accommodate.
        price_by_night (int): The price per night for the place.
        latitude (float): The latitude coordinate of the place.
        longitude (float): The longitude coordinate of the place.
        amenity_ids (list): The list of ids of amenities associated with the place.
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