#!/usr/bin/python3
"""
base model.py
Created by Rewan Abdulkariem @9/4/2024
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    Base class for models.

    Attributes:
        id (str): Unique identifier for the model instance.
        created_at (datetime): Date and time when the instance was created.
        updated_at (datetime): Date and time when it was last updated.
    """
    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance."""
        if kwargs:
            self.id = kwargs.get('id', str(uuid4()))
            self.created_at = self.parse_datetime(kwargs.get('created_at', datetime.now()))
            self.updated_at = self.parse_datetime(kwargs.get('updated_at', datetime.now()))

            for key, value in kwargs.items():
                if key not in ['id', 'created_at', 'updated_at', '__class__']:
                    setattr(self, key, value)

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def parse_datetime(self, value):
        """Convert value to datetime object if it's a string."""
        if isinstance(value, str):
            return datetime.fromisoformat(value)
        return value

    def save(self):
        """Update the `updated_at` attribute with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

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
