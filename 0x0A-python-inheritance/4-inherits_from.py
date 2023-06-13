#!/usr/bin/python3
"""Defines a class-cheking func."""


def inherits_from(obj, a_class):
    """func that checks if a class in same class or inherited

    Args:
        obj (any): The obj to check
        a_class (type): The class to check againist.
    Returns:
        if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class-True
        otherwise-False
    """
    if any(issubclass(type(obj), c) for c in a_class.__mro__):
        return (True)
    return False
