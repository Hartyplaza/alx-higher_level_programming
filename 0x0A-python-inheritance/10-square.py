#!/usr/bin/python3
""" A Class """


class BaseGeometry:
    """ A base class"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """ A Derive class"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Return the sum of geometry """
        return self.__height * self.__width

    def __str__(self):
        """ String representation """
        return "[{}] {}/{}".format(
                self.__class__.__name__, self.__width, self.__height)


class Square(Rectangle):
    """ Derive class"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        """ super class """
        super().__init__(size, size)
