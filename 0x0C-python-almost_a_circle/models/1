#!/usr/bin/python3
"""
This is module define the base class (super class)
"""

import json


class Base:
    """Class Base

    Private attribute __nb_objects to count instances

    Attributes:
        attr1 (id): id of the instanc

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Validate the id and set it
        Args:
            param1 (id): Id for each intance of Base class

        """
        if id is not None:
            self.id = id
        else:
            __class__.__nb_objects += 1
            self.id = __class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ staticmethod to_json_string

            This method converts a lis of dictioanries to json string

            Args
                param1 (list_dictionaries): list of dictionaries

        """
        if list_dictionaries is None:
            return "[]"
        to_json = json.dumps(list_dictionaries)
        return to_json

    @staticmethod
    def from_json_string(json_string):
        """ static method from_json_string
            converts json in sting

            Args:
                param1 (json_string): string to convert

        """
        if json_string is None:
            return []
        to_str = json.loads(json_string)
        return to_str

    @classmethod
    def save_to_file(cls, list_obj):
        """classmethod save to file
            save a a file with a list of obects converted in dictionaries

            Args:
                param1 (cls): class reference
                parama2 (list_obj): list of objects

        """
        name = cls.__name__
        filename = str(name + ".json")

        with open(filename, mode='w', encoding='utf-8') as f:
            flag = 0

            if list_obj is None:
                f.write(json.dumps([]))
            else:
                f.write("[")
                for el in list_obj:
                    if flag > 0:
                        f.write(", ")
                    a = cls.to_json_string(el.to_dictionary())
                    flag += 1
                    f.write(a)
                f.write("]")

    @classmethod
    def create(cls, **dictionary):
        """ class method create
            create a new instance of the referencd class passed in cls
            and uptade the instance with **awkwards

            Args:
                param1 (cls): class reference
                param1 (**dictionary): awkwards

        """
        if cls.__name__ == 'Rectangle':
            dummy = cls(23, 4)
        if cls.__name__ == 'Square':
            dummy = cls(9)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
            calculate area of rectangle
        """
        name = cls.__name__
        filename = str(name + ".json")

        try:
            with open(filename, mode='r', encoding='utf-8') as f:
                lines = f.read()
                list_dictionaries = cls.from_json_string(lines)
            empty_list = []

            for dic in list_dictionaries:
                obj = cls.create(**dic)
                empty_list.append(obj)
            return empty_list
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_obj):
        """classmethod save to file
            save a a file with a list of obects converted in dictionaries

            Args:
                param1 (cls): class reference
                parama2 (list_obj): list of objects

        """
        name = cls.__name__
        filename = str(name + ".csv")

        with open(filename, mode='w', encoding='utf-8') as f:
            flag = 0

            if list_obj is None:
                f.write(json.dumps([]))
            else:
                f.write("[")
                for el in list_obj:
                    if flag > 0:
                        f.write(", ")
                    a = cls.to_json_string(el.to_dictionary())
                    flag += 1
                    f.write(a)
                f.write("]")

    @classmethod
    def load_from_file_csv(cls):
        """
            calculate area of rectangle
        """
        name = cls.__name__
        filename = str(name + ".csv")

        try:
            with open(filename, mode='r', encoding='utf-8') as f:
                lines = f.read()
                list_dictionaries = cls.from_json_string(lines)
            empty_list = []

            for dic in list_dictionaries:
                obj = cls.create(**dic)
                empty_list.append(obj)
            return empty_list
        except IOError:
            return []
