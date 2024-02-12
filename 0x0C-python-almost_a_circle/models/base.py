#!/usr/bin/python3
"""A module a parent module """
import json


class Base(object):
    """A base module"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        json_list = [objs.to_dictionary() for objs in list_objs]
        with open(filename, 'w') as file:
            file.write(cls.to_json_string(json_list))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or not json_string:
            return "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        # print(cls.__name__)
        if cls.__name__ == "Rectangle":
            instance = cls(3, 5, 1)
        elif cls.__name__ == "Square":
            instance = cls(3)
        return instance

    @classmethod
    def load_from_file(cls):
        list_obj = list()
        filename = cls.__name__ + ".json"
        if not filename:
            return "[]"
        with open(filename, 'r') as f:
            json_data = f.read()
            py_dict = cls.from_json_string(json_data)
            for value in py_dict:
                list_obj.append(cls.create(**value))
            return list_obj
