#!/usr/bin/python3
""" A Rectangle class """


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
