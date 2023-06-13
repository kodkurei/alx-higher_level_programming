#!/usr/bin/python3
""" Defines a class-cheking func """


def is_same_class(obj, a_class):
    """func to check if an object is an instance of the specified class
    Args:
        obj (any): The object to check
        a_class (type): the class to match the type of obj to.
    Returns:
        If obj is exactly an instance of a_class - True
        otherwise - false.
    """
    if type(obj) == a_class:
        return True
    return False
