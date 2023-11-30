#!/usr/bin/python3
""" A Rectangel class """


class Rectangle:
    """ defines a rectangle """

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    """ width setter """

    @property
    def width(self):
        return self.__width

    """ width getter """

    @width.setter
    def width(self, value):

        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """ height setter """

    @property
    def height(self):
        return self.__height

    """ height getter """

    @height.setter
    def height(self, value):

        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    """ Area of Rectangle"""

    def area(self):
        return self.__height * self.__width

    """ Perimeter of a Rectangle"""

    def perimeter(self):
        if self.width == 0:
            return 0
        if self.height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    """ String representation"""

    def __str__(self):
        empty_string = ""

        if self.__width == 0 or self.__height == 0:
            return empty_string

        return (('#' * self.width) + "\n") * self.height

    """ string representation of the rectangle """

    def __repr__(self):
         return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))
