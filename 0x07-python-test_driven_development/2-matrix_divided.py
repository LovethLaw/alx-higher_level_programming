#!/usr/bin/python3
"""This Module containd a Matrix divider that dives every element in Matrix if list
    Args:
            matrix(list): a list of elenent int or float
            div(int, float): number to divide with
    """
def matrix_divided(matrix, div):
    """ A function that divides every element in a matrix
        Args:
            matrix(list): a list of elenent int or float
            div(int, float): number to divide with
    """
    # Not Needed use list comprehension
    # new_row_1 = []
    # new_row_2 = []
    # new_list = []

    # if matrix is not a list a type error is raised
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

    matrix_size = len(matrix[0])
    # if row size is != to the row size raise type errors
    if not all(len(row) == matrix_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # if div is 0 raise zeroDivisionError or Div is not an int or float
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError('division by zero')

    return [[round((elem / div), 2) for elem in row] for row in matrix]

    # for index, rows in enumerate(matrix):
    #     for elem in rows:
    #         elem = round((elem / div), 2)
    #         if index == 0:
    #             new_row_1.append(elem)
    #         else:
    #             new_row_2.append(elem)
    # new_list.append(new_row_1)
    # new_list.append(new_row_2)
    # return new_list
