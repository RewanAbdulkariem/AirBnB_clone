import os
import json
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    """Unit tests for the FileStorage class."""
    def test_new(self):
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        self.assertIn(f"BaseModel.{obj.id}", storage.all())

    def test_save(self):
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        storage.save()

        file_path = storage._FileStorage__file_path
        self.assertTrue(os.path.exists(file_path), f"File {file_path} does not exist")
        
        with open(file_path) as f:
            data = json.load(f)
        self.assertIn(f"BaseModel.{obj.id}", data)

    def test_reload(self):
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        storage.save()

        FileStorage._FileStorage__objects = {}
        storage.reload()
        self.assertIn(f"BaseModel.{obj.id}", storage.all())

if __name__ == "__main__":
    unittest.main()
