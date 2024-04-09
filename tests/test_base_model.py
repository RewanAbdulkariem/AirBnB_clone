#!/usr/bin/python3
"""
test BaseModel
Created by Rewan Abdulkariem @9/4/2024
"""
import os
import sys
import unittest
from models.base_model import BaseModel
from datetime import datetime

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))


class TestBaseModel(unittest.TestCase):
    """Unit tests for the BaseModel class."""
    def setUp(self):
        """Set up a BaseModel instance for testing."""
        self.model = BaseModel()

    def test_id(self):
        """
        Test the id attribute of BaseModel.

        Assert that `id` is a string and has a length of 36 characters,
        which is the length of a UUID.
        """
        self.assertIsInstance(self.model.id, str)
        self.assertEqual(len(self.model.id), 36)  # UUID length check

    def test_created_at(self):
        """
        Test the created_at attribute of BaseModel.

        Assert that `created_at` is an instance of datetime.
        """
        self.assertIsInstance(self.model.created_at, datetime)

    def test_save(self):
        """
        Test the save method of BaseModel.

        Assert that calling `save()` updates the `updated_at` attribute.
        """
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_to_dict(self):
        """
        Test the to_dict method of BaseModel.

        Assert that `to_dict()` returns a dictionary with
        the expected keys and values,including '__class__',
         'id', 'created_at', and 'updated_at'.
        """
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], self.model.id)
        self.assertEqual(
            model_dict['created_at'], self.model.created_at.isoformat())
        self.assertEqual(
            model_dict['updated_at'], self.model.updated_at.isoformat())

    def test_str(self):
        """
        Test the string representation of BaseModel.

        Assert that `str(model)` returns a string in the expected format:
        "[BaseModel] (id) {'attribute1': value1, 'attribute2': value2, ...}".
        """
        expected_str = "[BaseModel] ({}) {}".format(
            self.model.id, self.model.__dict__)
        self.assertEqual(str(self.model), expected_str)


if __name__ == '__main__':
    unittest.main()
