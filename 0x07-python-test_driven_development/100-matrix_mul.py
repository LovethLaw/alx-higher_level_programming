#!/usr/bin/python3


"""this module contains an implementation of a mtrix multiplication."""


def matrix_mul(m_a, m_b):
    """this function multiplies two matrices

       Args:
           m_a (list(list)): this is the first matrix operand.
           m_b (list(list)): this is the second matrix operand.

       Returns:
           A new matrix list product of matrices m_a and m_b
    """

    new_matrix_list = []

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

    mat_a_size = len(m_a)

    mat_b_size = len(m_b)

    mat_b_col_size = len(m_b[0])

    # Try except a ValueError occured during multiplication.
    try:
        err_ma = "m_a should contain only integers or floats"

        err_mb = "m_b should contain only integers or floats"

        for i in range(mat_a_size):
            new_row = []
            for j in range(mat_b_col_size):
                element_prod = 0
                for k in range(mat_b_size):
                    if not isinstance(m_a[i][k], (int, float)):
                        raise TypeError(err_ma)

                    if not isinstance(m_b[k][j], (int, float)):
                        raise TypeError(err_mb)
                    element_prod += m_a[i][k] * m_b[k][j]
                new_row.append(element_prod)

            new_matrix_list.append(new_row)
    except ValueError:
        raise ValueError("m_a and m_b can't be multiplied")
    # print(f"mat a size: {mat_a_size}")
    # print(f"mat b size: {mat_b_size}")
    # print(f"mat b col size: {mat_b_col_size}")
    # print(f"m_a[i][k] -> {type(m_a[i][k])}")
    # print(f"m_b[k[j] -> {type(m_b[k][j])}")

    return (new_matrix_list)
