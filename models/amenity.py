#!/usr/bin/python3
"""
base amenity.py
Created by Rewan Abdulkariem @11/4/2024
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Represents an amenity.

    Attributes:
        name (str): The name of the amenity.
    """
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)