#!/usr/bin/python3
from models.base_model import BaseModel
"""
user.py
Created by Rewan Abdulkariem @11/4/2024
"""
class User(BaseModel):
    """
    A class representing a user.

    Attributes:
        email (str): The email address of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initializes a new User instance."""
        super().__init__(*args, **kwargs)
