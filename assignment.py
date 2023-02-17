def find_max_in_row_min_in_col(mat):
    # Check that the input matrix satisfies the given constraints
    M = len(mat)
    N = len(mat[0])
    if not(1 <= M <= 50) or not(1 <= N <= 50):
        raise ValueError("The matrix dimensions must be between 1 and 50")
    for i in range(M):
        if len(mat[i]) != N:
            raise ValueError("All rows in the matrix must have the same length")
        for j in range(N):
            if not(1 <= mat[i][j] <= 105):
                raise ValueError("All elements in the matrix must be between 1 and 105")
    if len(set([elem for row in mat for elem in row])) != M * N:
        raise ValueError("All elements in the matrix must be distinct")

    # Find the maximum value in each row
    row_max = [max(row) for row in mat]

    # Find the minimum value in each column
    col_min = [min([mat[i][j] for i in range(M)]) for j in range(N)]

    # Find the numbers that are the maximum value in its row and the minimum in its column
    result = [mat[i][j] for i in range(M) for j in range(N) if mat[i][j] == row_max[i] and mat[i][j] == col_min[j]]

    return result
