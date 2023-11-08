#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, div, mul

argument = len(argv)
if argument != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>".format(argv[0]))
    exit(1)

operator_dict = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div}

if argv[2] in operator_dict:
    a = int(argv[1])
    b = int(argv[3])
    op = operator_dict[argv[2]]
    result = op(a, b)
    print("{:d} {:s} {} = {:d}".format(a, op, b, result))
else:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
exit(0)
