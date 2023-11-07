#!/usr/bin/python3
def no_c(my_string):
    modified_char = ""
    for char in my_string:
        if char != "c" and char != "C":
            modified_char += char
    return modified_char
