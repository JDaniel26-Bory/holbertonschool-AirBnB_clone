#!/usr/bin/python3
'''Import several library'''
import json
import os
from models.base_model import BaseModel
'''Create to class call Filestorage'''


class FileStorage:
    '''Attributes for tha class'''

    __file_path = "file.json"
    __objects = {}

    '''Function that return a object'''

    def all(self):
        return FileStorage.__objects

    '''sets in __objects the obj with key'''

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj
        '''Function that serializes __objects to the JSON file '''

    def save(self):
        """Serialize __objects to the JSON file."""
        obj_dict = {
            key: obj.to_dict() for key, obj in FileStorage.__objects.items()
        }
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """Deserialize the JSON file to __objects."""
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name = value["__class__"]
                    obj = eval(class_name)(**value)
                    FileStorage.__objects[key] = obj
