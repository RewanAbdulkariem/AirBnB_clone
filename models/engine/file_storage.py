#!/usr/bin/python3
"""
file_storage.py
created by Rewan Abdulkariem @10/4/2024
"""
import os
import json
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Serializes instances to a JSON file and deserializes
    JSON file to instances."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        serialized = {}
        for key, val in FileStorage.__objects.items():
            serialized[key] = val.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(serialized, f)

    def reload(self):
        """Deserializes the JSON file to __objects if the file exists."""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                deserialized = json.load(f)
                for key, value in deserialized.items():
                    class_name, obj_id = key.split('.')
                    obj_dict = value
                    obj_dict['created_at'] = datetime.strptime(obj_dict['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
                    obj_dict['updated_at'] = datetime.strptime(obj_dict['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")

                    FileStorage.__objects[key] = eval(class_name)(**obj_dict)
