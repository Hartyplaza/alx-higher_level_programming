#!/usr/bin/python3
""" A class """


class BaseGeometry:
    """ A basegeomerty class who's instance method:
    def area(self): that raises an Exception with the message
    area() is not implemented """
    def area(self):
        raise Exception("area() is not implemented")
