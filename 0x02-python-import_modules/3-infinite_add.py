#!/usr/bin/python3
import sys

if __name__ == "__main__":
    my_list = sys.argv

    my_list.pop(0)

    my_sum = 0

    for list_items in my_list:

        new_list = int(list_items)
        my_sum += new_list

    print(my_sum)
