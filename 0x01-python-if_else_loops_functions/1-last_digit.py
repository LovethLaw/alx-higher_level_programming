#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num_2 = abs(number) % 10
if number < 0:
    num_2 = -num_2
if num_2 > 5:
    print(f"Last digit of {number} is {num_2} and is greater than 5")
elif num_2 == 0:
    print(f"Last digit of {number} is {num_2} and is 0")
elif num_2 < 6 and num_2 != 0:
    print(f"Last digit of {number} is {num_2} and is less than 6 and not 0")
