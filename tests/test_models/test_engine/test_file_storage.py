import os
import json
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    """Unit tests for the FileStorage class."""
    def setUp(self):
        """Set up a FileStorage instance for testing."""
        self.storage = FileStorage()

    def test_file_path(self):
        self.assertEqual(str, type(self.storage._FileStorage__file_path))

    def test_objects(self):
        self.assertEqual(dict, type(self.storage._FileStorage__objects))
    
    def test_all(self):
        self.assertEqual(dict, type(self.storage.all()))

    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            self.storage.all(None)
    def test_new(self):
        obj = BaseModel()
        self.storage.new(obj)
        self.assertIn(f"BaseModel.{obj.id}", self.storage.all())

    def test_save(self):
        self.storage = FileStorage()
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()

        file_path = self.storage._FileStorage__file_path
        self.assertTrue(os.path.exists(file_path), f"File {file_path} does not exist")
        
        with open(file_path) as f:
            data = json.load(f)
        self.assertIn(f"BaseModel.{obj.id}", data)

    def test_reload(self):
        self.storage = FileStorage()
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()

        FileStorage._FileStorage__objects = {}
        self.storage.reload()
        self.assertIn(f"BaseModel.{obj.id}", self.storage.all())

if __name__ == "__main__":
    unittest.main()
