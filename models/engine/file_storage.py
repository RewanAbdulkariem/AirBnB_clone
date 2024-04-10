#!/usr/bin/python3
"""
file_storage.py
created by Rewan Abdulkariem @10/4/2024
"""
import os
import json


class FileStorage:
    """Serializes instances to a JSON file and deserializes
     JSON file to instances."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                return (json.load(f))
        else:
            return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        serialized = {}
        for key, val in FileStorage.__objects.items():
            serialized = {key: val.to_dict()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(serialized, f)

    def reload(self):
        """Deserializes the JSON file to __objects if the file exists."""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                deserialized = json.load(f)
                for key, value in deserialized.items():
                    class_name, obj_id = key.split('.')
                    obj_dict = value

                    obj_dict['__class__'] = class_name
                    FileStorage.__objects[key] = eval(class_name)(**obj_dict)
        except:
            pass
