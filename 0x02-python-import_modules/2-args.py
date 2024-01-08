#!/usr/bin/python3
import sys

if __name__ == "__main__":

    my_list = sys.argv

    my_list.pop(0)

    list_length = len(my_list)

    arg = ""

    if list_length == 0:

        arg = "arguments" + "."

    elif list_length == 1:

        arg = "argument" + ":"

    else:

        arg = "arguments" + ":"

    print(f"{list_length} {arg}")

    length = list_length + 1

    for num in range(list_length):

        print(f"{num + 1}: {my_list[num]}")
