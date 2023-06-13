#!/usr/bin/python3
"""Define a class BaseGeometry """


class BaseGeometry:
    """Body of the class """
    def area(self):
        """func that returns raise an Exception """
        raise Exception("area() is not implimented")

    def integer_validator(self, name, value):
        """func that validates value
        Args:
            name (string):name of the string
            value (int): Value to validate
        Raises:
            TypeError: The name of the parameter
            ValueError: If value is <= 0
        """
        if isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
