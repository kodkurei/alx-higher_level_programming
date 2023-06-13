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

    def to_json(self):
        """returns a dictionary with keys corresponding to the instance
        variables of the Student class and their respective values
        """
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
            }
