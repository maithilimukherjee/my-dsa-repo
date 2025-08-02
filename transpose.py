def transpose(matrix):
    """
    Transpose a 2D matrix (list of lists).

    Args:
        matrix (List[List[int]]): The input matrix.

    Returns:
        List[List[int]]: The transposed matrix.
    """
    if not matrix or not matrix[0]:
        return []

    rows = len(matrix)
    cols = len(matrix[0])

    # Transposing using list comprehension
    transposed = [[matrix[row][col] for row in range(rows)] for col in range(cols)]
    return transposed
