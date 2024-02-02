#!/usr/bin/python3


"""this module contains an implementation of a mtrix multiplication."""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """this function multiplies two matrices

       Args:
           m_a (list(list)): this is the first matrix operand.
           m_b (list(list)): this is the second matrix operand.

       Returns:
           A new matrix list product of matrices m_a and m_b
    """

    # validate both matrices are a list.
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    def valid_matrix_lists(mat: [[]]) -> bool:
        """This function validates the object of the matrix list.
           it checks the sub items of the matrix to check if it's a list.

           Args:
               mat (list[list]): a list of lists objects.
           Returns:
                True
        """

        if not isinstance(mat, list):
            return False

        for sub_list in mat:
            if not isinstance(sub_list, list):
                return False

        return True

    if not valid_matrix_lists(m_a):
        raise TypeError("m_a must be a list of lists")

    if not valid_matrix_lists(m_b):
        raise TypeError("m_b must be a list of lists")

    # check for empty lists.
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")

    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    # validate the matrices rows.
    mat_a_row_size = len(m_a[0])

    for row in m_a:
        if len(row) != mat_a_row_size:
            raise ValueError("each row of m_a must be of the same size")

    mat_b_row_size = len(m_b[0])

    for row in m_b:
        if len(row) != mat_b_row_size:
            raise ValueError("each row of m_b must be of the same size")

    mat_arr_result = None

    # Try except a ValueError occured during multiplication.
    try:
        err_ma = "m_a should contain only integers or floats"

        err_mb = "m_b should contain only integers or floats"

        m_a_arr = np.array(m_a)

        m_b_arr = np.array(m_b)

        # validate all elements in the array.
        def validate_mat_arr(mat_arr, err_msg):
            """This function checks if the elements of the matrix is valid.

               Args:
                   mat_arr (list[list]): this is the matrix list of lists.
                   err_msg (str): Error message to be printed.

               Returns:
                   None
            """

            for outter_row in mat_arr:
                for item in outter_row:
                    if not isinstance(item, (int, float)):
                        raise TypeError(err_msg)

        validate_mat_arr(m_a, err_ma)

        validate_mat_arr(m_b, err_mb)

        mat_arr_result = np.dot(m_a_arr, m_b_arr)

    except ValueError:
        raise ValueError("m_a and m_b can't be multiplied")

    return (mat_arr_result)
