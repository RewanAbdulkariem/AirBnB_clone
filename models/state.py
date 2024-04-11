#!/usr/bin/python3
from models.base_model import BaseModel
"""
base state.py
Created by Rewan Abdulkariem @11/4/2024
"""
class State(BaseModel):
    """
    Represents a state.

    Attributes:
        name (str): The name of the state.
    """
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
