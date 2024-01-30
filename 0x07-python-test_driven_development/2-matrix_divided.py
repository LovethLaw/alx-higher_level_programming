#!/usr/bin/python3
"""
    This module contains a function that divides elements of a matrix
    It takes in a list of matrix and and intege as a divisor
    returns a new metrix where elements are divided by the diviosr
"""


def matrix_divided(matrix, div):
    """
    divides elements of a matrix
    """
    new_matrix = []

    if not isinstance(matrix, list):

        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if len(matrix) == 0 or not all(isinstance(row, list) and len(row) > 0 for row in matrix):

        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(num, (int, float)) for row in matrix for num in row):

        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):

        raise TypeError("div must be a number")

    if div == 0:

        raise ZeroDivisionError("division by zero")

    for row in matrix:

        new_list = []

        for num in row:

            result = round(num / div, 2)

            new_list.append(result)

        new_matrix.append(new_list)

    return new_matrix
