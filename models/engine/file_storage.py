#!/usr/bin/python3
"""
This module contains the class FileStorage
"""
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json
import os


class FileStorage:
    """
    FileStorage class
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Public method that returns all objects from 
        the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """Public method that sets in __objects
        with key <obj class name>.id
        """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """Public method that serializes __objects
        to the JSON file (path: __file_path)
        """
        with open(self.__file_path, "w", encoding="UTF-8") as f:
            obj_dict = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(obj_dict, f)

    def reload(self):
        """Public method that deserializes the 
        JSON file to __objects, only if the JSON
        file (__file_path) exists. Otherwise, do nothing.
        """
        classes = {
                "BaseModel": BaseModel,
                "User": User,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Place": Place,
                "Review": Review
                }
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r", encoding="UTF-8") as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    name = key.split('.')[0]
                    if name in classes:
                        obj = classes[name](**value)
                    self.__class__.__objects[key] = obj
