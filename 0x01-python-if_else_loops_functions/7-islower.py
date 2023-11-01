#!/usr/bin/python3
def islower(c):
    lower_case = ord(c)
    if lower_case in range(97, 123):
        return True
    else:
        return False
