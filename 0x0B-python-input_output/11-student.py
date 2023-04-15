#!/usr/bin/python3
"""Student Class"""


class Student:
    """Represent a student"""
    def __init__(self, first_name, last_name, age):
        """Initialize a new Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) is list and all(type(elem) is str for elem in attrs):
            return {key: value for key, value in self.__dict__.items() \
if  key in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        self.first_name = json['first_name']
        self.last_name = json['last_name']
        self.age = json['age']
        return self.__dict__
