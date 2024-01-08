#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

a = 10
b = 5
my_sum = add(a, b)
my_sub = sub(a, b)
my_mul = mul(a, b)
my_div = div(a, b)

if __name__ == '__main__':
    print("{} + {} = {}".format(a, b, my_sum))
    print("{} - {} = {}".format(a, b, my_sub))
    print("{} * {} = {}".format(a, b, my_mul))
    print("{} / {} = {}".format(a, b, my_div))
