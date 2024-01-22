#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):

    no_of_int = 0

    try:
        for i in range(x):

            if isinstance(my_list[i], int):

                print("{:d}".format(my_list[i]), end="")

                no_of_int += 1

        print()

        return no_of_int

    except IndexError as e:

        return e
