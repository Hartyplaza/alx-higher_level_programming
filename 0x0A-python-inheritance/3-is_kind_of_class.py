#!/usr/bin/python3
""" A Function """


def is_kind_of_class(obj, a_class):
    """ function that returns True if the object is an
    instance of, or if the object is an instance of a class 
    that inherited from, the specified class ; otherwis
    False """
    return isinstance(obj, a_class)
