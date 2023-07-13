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
        """"Serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, "w") as file:
            obj_dict = {
                key: obj.to_dict() for key, obj
                in FileStorage.__objects.items()
            }
            json.dump(obj_dict, file)

    '''deserializes the JSON file to __objects'''

    def reload(self):
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path) as file:
                loaded = json.load(file)
                for k, v in loaded.items():
                    obj = eval(v["__class__"])(**v)
                    self.__objects[k] = obj
        else:
            return
