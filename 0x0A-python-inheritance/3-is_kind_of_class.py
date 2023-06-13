#!/usr/bin/python3
""" Defines a class-checking function"""


def is_kind_of_class(obj, a_class):
    """func that checks if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class.
    Args:
        obj (any): the obj to check
        a_class (type): The class to match the type of obj
    Returns:
        returns True if the object is an instance of, or if the object
        is an instance of a class that inherited from, the specified class
        otherwise - false
    """
    if isinstance(obj, a_class) or issubclass(type(obj), a_class):
        return True
    return False
