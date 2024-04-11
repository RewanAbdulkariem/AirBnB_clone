#!/usr/bin/python3
from models.base_model import BaseModel
"""
base user.py
Created by Rewan Abdulkariem @11/4/2024
"""
class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
