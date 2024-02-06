#!/usr/bin/python3
"""pascal triangle"""


def pascal_triangle(n):
    """Returns the Pascal triangle of n.
    Args:
        - n: size of the triangle (rows)
    Returns: a list of list of integers
    """

    if n <= 0:
        return []

    triangle = [[0 for column in range(row + 1)] for row in range(n)]
    triangle[0] = [1]

    for i in range(1, n):
        triangle[i][0] = 1
        for j in range(1, i + 1):
            if j < len(triangle[i - 1]):
                triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            else:
                triangle[i][j] = triangle[i - 1][0]
    return triangle