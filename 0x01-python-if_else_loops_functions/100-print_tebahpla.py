#!/usr/bin/python3
for i in range(ord('z'), ord('a') -1, -2):
    print("{}{}".format(ord(i), chr(i -1 - 33)), end='')
