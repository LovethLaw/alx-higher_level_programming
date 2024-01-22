#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):

    try:
        no_of_elements = 0

        for i in range(x):

            print(my_list[i], end="")

            no_of_elements += 1

        print()

        return no_of_elements

    except (IndexError):

        print()

        return no_of_elements
