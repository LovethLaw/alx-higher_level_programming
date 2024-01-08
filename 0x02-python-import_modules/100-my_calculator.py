#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
if __name__ == "__main__":
    my_list = sys.argv
    my_list.pop(0)
    list_length = len(my_list)

    if list_length != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(my_list[0])
    operator = my_list[1]
    b = int(my_list[2])

    if operator == "+":
        result_add = add(a, b)
        print(f"{a} {operator} {b} = {result_add}")

    elif operator == "-":
        result_sub = sub(a, b)
        print(f"{a} {operator} {b} = {result_sub}")

    elif operator == "*":  # Handle "*" as multiplication

        result_mul = mul(a, b)
        print(f"{a} {operator} {b} = {result_mul}")

    elif operator == "/":
        result_div = div(a, b)
        print(f"{a} {operator} {b} = {result_div}")

    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
