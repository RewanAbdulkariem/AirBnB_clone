#!/usr/bin/python3
"""
base model.py
Created by Rewan Abdulkariem @9/4/2024
"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    Base class for models.

    Attributes:
        id (str): Unique identifier for the model instance.
        created_at (datetime): Date and time when the instance was created.
        updated_at (datetime): Date and time when it was last updated.
    """
    def __init__(self):
        """Initialize a new BaseModel instance."""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """Update the `updated_at` attribute with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Return a dictionary representation of the BaseModel instance.

        Returns:
            dict: Dictionary containing instance attributes for serialization.
                  Includes '__class__' key with the class name.
                  'created_at' and 'updated_at' are ISO-formatted strings.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__

        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()

        return obj_dict

    def __str__(self):
        """
        Return a string representation of the BaseModel instance.

        Format:
            [ClassName] (id) {attribute1: value1, attribute2: value2, ...}
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)
