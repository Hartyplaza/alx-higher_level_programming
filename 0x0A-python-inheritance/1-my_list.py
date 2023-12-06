#!/usr/bin/python3
""" a class """


class MyList(list):
    """ class MyList that inherits from list """
    def print_sorted(self):
        print(sorted(self))
