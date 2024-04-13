#!/usr/bin/python3
"""
test User.py
Created by Rewan Abdulkariem @9/4/2024
"""
import os
import unittest
from models.engine.file_storage import FileStorage
from models.user import User
from models import storage


class TestUser(unittest.TestCase):
    """Unit tests for the User class."""
    def setUp(self):
        """Set up test environment"""
        self.user = User()
        self.user.email = "rewan.khaled21@gmail.com"
        self.user.password = "password"
        self.user.first_name = "Rewan"
        self.user.last_name = "Khaled"

    def test_attributes(self):
        """Test User attributes"""
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))

    def test_attributes_types(self):
        """Test method for attributes"""
        key = f'{self.user.__class__.__name__}.{self.user.id}'

        self.assertIn(key, storage.all())
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)

    def test_save(self):
        """Test method for save"""
        old_update = self.user.updated_at
        self.user.save()
        self.assertNotEqual(self.user.updated_at, old_update)

    def test_str(self):
        """Test __str__ method of User"""
        self.assertEqual(str(self.user), f"[User] ({self.user.id}) {self.user.__dict__}")

if __name__ == '__main__':
    unittest.main()