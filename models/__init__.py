#!/usr/bin/python3
"""
__init__.py
created by Rewan Abdulkariem
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
