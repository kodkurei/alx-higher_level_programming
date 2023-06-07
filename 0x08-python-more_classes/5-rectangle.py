#!/usr/bin/python3
"""Defination of a class Rectangle"""


class Rectangle
    """contents of class Rectangle"""
    def __init__(self, width=0, height=0):
        """Initialization of a rectangle
        Args:
            width (int) - width of the rectangle
            height (int) - height of the rectangle
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """get/set the value of width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get/set the value of width"""
        return (self.__width)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """func to find the area of Rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """func to find the perimeter of Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return((self.__height * 2) + (self.__width * 2))
    def __str__(self):
        """return the printable represenrtation of the rectangle.

        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")

        return ("".join(rect))
    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self_):
        """Print a message for every deletion of a Rectangle."""
        print("Bye rectangleBye rectangle...")
