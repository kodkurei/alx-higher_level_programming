#!/usr/bin/python3
"""defines a class student"""


class Student:
    """body of the class """
    def __init__(self, first_name, last_name, age):
        """instantiation
        Args:
            firs_name (str): firstname of the student
            last_name (str): lastname of the student
            age (int): age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """The to_json method now takes an optional parameter attrs,
            which is a list of strings representing the names of attr to be
            included in the output dictionary.
        Args:
            attrs (str):a list of str rep the name of the attr to be included
        Return:
        """
        if (type(attrs) == list and all(type(ele)
                                        == str for ele in attrs)):
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}
        return self.__dict__
