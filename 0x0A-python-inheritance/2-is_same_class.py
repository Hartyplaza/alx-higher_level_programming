#!/usr/bin/python3
""" A Function """


def is_same_class(obj, a_class):
    """ function that returns True if the object is exactly
    an instance of the specified class ; otherwise False """
    return type(obj) == a_class
