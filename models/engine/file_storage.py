#!/usr/bin/python3
"""storage class"""
from base_model import BaseModel
import json


class FileStorage:
    """file storage """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns __object """
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        obj_dict = {}
        for key, value in FileStorage.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(obj_dict)

    def classes(self):
        """Dictionary of valid classes """
        classes = {"BaseModel": BaseModel}
        return classes
