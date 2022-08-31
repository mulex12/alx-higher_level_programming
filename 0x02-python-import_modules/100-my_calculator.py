#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    if len(argv) < 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    ops = {"+": add, "-": sub, "*": mul, "/": div}
    if argv[2] in list(ops.keys()):
        print("{} {} {} = {}".format(a, argv[2], b, ops[argv[2]](a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
