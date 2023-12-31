#!/usr/bin/env python3
""" Class FileStorage that serializes instances to a JSON file
    and deserializes JSON file to instances in prog
"""

import json
from os import read
from models.base_model import BaseModel
from models.city import City
from models.state import State
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os.path


class FileStorage:
    """ Class FileStorage that serilizes
    and deserialize instances to JSON
        __file_path: the path of the json file
        __objs: a dict of all objs"
    """
    def __init__(self):
        """ inits FileStorage
        """
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """Returns a dict of all objs"""
        return self.__objects

    def new(self, obj):
        """sets in __objs the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """serializes __objs to the JSON file (path: __file_path)
            dict: an empty dict
                Open the dict in write mode
                dump the dict in the file f
        """
        dictionary = {}
        with open(self.__file_path, 'w') as f:
            for obj in self.__objects.values():
                key = obj.__class__.__name__ + "." + obj.id
                dictionary[key] = obj.to_dict()
            json.dump(dictionary, f)

    def reload(self):
        """deserializes the JSON file to __objs
        (only if the JSON file (__file_path) exists
        otherwise, do nothing in prog.
        If the file doesn’t exist, no exception should be raised)
            Open in read mode"
            load the file f and read it
            """
        try:
            with open(self.__file_path, 'r') as f:
                my_dict = json.load(f)
            for key, value in my_dict.items():
                """this for loop utilise a key value pair to run
                    my_dict.items() and create a dictionary of key and value"""
                new_object = key.split('.')
                class_name = new_object[0]
                """new_object is equal to key.split('.')[0]
                    this split the key and take the first part of the key"""
                self.new(eval("{}".format(class_name))(**value))
                """this if statement is used to create a new object
                    with the class name of new_object and its val"""
        except FileNotFoundError:
            pass
