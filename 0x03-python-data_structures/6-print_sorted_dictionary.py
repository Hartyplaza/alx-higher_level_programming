#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sot = dict(sorted(a_dictionary.items()))
    for key, value in sot.items():
        print("{} : {}".format(key, value))
