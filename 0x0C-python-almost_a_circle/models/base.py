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
    """ staticmethod to_json_string

        This method converts a lis of dictioanries to json string

        Args
            param1 (list_dictionaries): list of dictionaries

    """
    def to_json_string(list_dictionaries):

        if list_dictionaries is None:
            return "[]"
        to_json = json.dumps(list_dictionaries)
        return to_json

    @staticmethod
    """ static method from_json_string
        converts json in sting

        Args:
            param1 (json_string): string to convert

    """
    def from_json_string(json_string):

        if json_string is None:
            return "[]"
        to_str = json.loads(json_string)
        return list(to_str)

    @classmethod
    """ classmethod save to file 
        save a a file with a list of obects converted in dictionaries

        Args:
            param1 (cls): class reference
            parama2 (list_obj): list of objects

    """
    def save_to_file(cls, list_obj):
        name = cls.__name__
        filename = str(name + ".json")

        with open(filename, mode='a', encoding='utf-8') as f:
            flag = 0

            if list_obj is None:
                f.write("[]")
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
    """ class method create
        create a new instance of the referencd class passed in cls
        and uptade the instance with **awkwards

        Args:
            param1 (cls): class reference
            param1 (**dictionary): awkwards

    """
    def create(cls, **dictionary):
        dummy = cls(1, 1, 1, 1,)
        dummy.update(**dictionary)
       return dummy

    @classmethod
    def load_from_file(cls):
        name = cls.__name__
        filename = str(name + ".json")

        with open(filename, encoding='utf-8') as f:
            from_json_string()
