#!/usr/bin/python3
def uniq_add(my_list=[]):

    unique_sum = 0

    unique_item = set(my_list)

    for i in unique_item:

        unique_sum = unique_sum + i

    return unique_sum
