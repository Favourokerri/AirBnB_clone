#!/usr/bin/python3
"""storage class"""
import json
import os


class FileStorage:
    """file storage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns __objects"""
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
            json.dump(obj_dict, f)

    def classes(self):
        """Dictionary of valid classes"""
        from models.base_model import BaseModel
        classes = {"BaseModel": BaseModel}
        return classes

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
        reloaded_objects = {}
        for key, value in obj_dict.items():
            class_name = value["__class__"]
            if class_name in self.classes():
                obj = self.classes()[class_name](**value)
                reloaded_objects[key] = obj
        FileStorage.__objects = reloaded_objects
