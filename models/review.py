#!/usr/bin/python3
"""
review.py
Created by Rewan Abdulkariem @11/4/2024
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Represents a review.

    Attributes:
        place_id (str): The id of the place being reviewed.
        user_id (str): The id of the user who wrote the review.
        text (str): The text content of the review.
    """
    place_id = ""
    user_id = ""
    text = ""