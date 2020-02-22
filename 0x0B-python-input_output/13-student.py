#!/usr/bin/python3


class Student:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            d = self.__dict__
            return {z: d[z] for atr in attrs for z in d if z == atr}

    def reload_from_json(self, json):
        for k, v in json.items():
            setattr(self, k, v)
           
