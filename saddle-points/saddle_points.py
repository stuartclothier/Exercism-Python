from typing import List, Dict


def saddle_points(matrix: List[List[int]]) -> List[Dict[str, int]]:

    # Check matrix has regular shape
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise ValueError("Matrix has irregular shape.")

    # Get transpose of matrix
    matrixT = list(zip(*matrix))

    # Get list of saddle point indices, where i and j refer to the row and column indices respectively
    res = [
        [i + 1, j + 1]
        for i, row_elements in enumerate(matrix)
        for j, value in enumerate(row_elements)
        if min(matrixT[j]) == max(row_elements)
    ]

    # Define Dictionary keys
    keys = ["row", "column"]

    return [dict(zip(keys, row)) for row in res]
