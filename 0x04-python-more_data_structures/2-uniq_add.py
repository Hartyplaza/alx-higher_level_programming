#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = set()
    for number in my_list:
        if number != uniq:
            uniq.add(number)
    return sum(uniq)
