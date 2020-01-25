#!/usr/bin/python3
import json

class Base:

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            __class__.__nb_objects += 1
            self.id = __class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"

        to_json = json.dumps(list_dictionaries)
        return to_json

    @classmethod
    def save_to_file(cls, list_obj):
        name = cls.__name__
        filename = str(name + ".json")

        with open(filename, mode='w', encoding='utf-8') as f:
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
