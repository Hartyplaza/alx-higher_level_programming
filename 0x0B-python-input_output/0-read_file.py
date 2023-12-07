#!/usr/bin/python3
""" Function that reads a text file """


def read_file(filename=""):
    """ Reads UFT-8 File """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
