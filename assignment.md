# ASSIGNMENT SOLUTIONS

## Write an algorithm that given an M X N  matrix return all numbers that are the maximum value inits row but the minimum in its column

```python
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
```

## What is the space and time complexity of your solution?

The time complexity of the algorithm is O(m * n^2), where m is the number of rows and n is the number of columns in the matrix.
The space complexity of the optimized algorithm is also O(1)

## Write 1-2 tests that you run to validate your answer

### Test case

```python
import pytest
from assignment import find_max_in_row_min_in_col

def test_valid_input():
    mat = [[5, 16, 20], [9, 11, 18], [15, 16, 17]]
    assert find_max_in_row_min_in_col(mat) == [17]

    mat = [[100, 60, 20, 50], [70, 80, 10, 90], [10, 50, 44, 30]]
    assert find_max_in_row_min_in_col(mat) == [50]

def test_empty_matrix():
    mat = []
    with pytest.raises(ValueError):
        find_max_in_row_min_in_col(mat)

def test_matrix_with_zero_rows():
    mat = [[]]
    with pytest.raises(ValueError):
        find_max_in_row_min_in_col(mat)

def test_matrix_with_different_row_lengths():
    mat = [[1, 2, 3], [4, 5], [6, 7, 8]]
    with pytest.raises(ValueError):
        find_max_in_row_min_in_col(mat)

def test_matrix_with_out_of_range_elements():
    mat = [[1, 2, 106], [4, 5, 6], [7, 8, 9]]
    with pytest.raises(ValueError):
        find_max_in_row_min_in_col(mat)

def test_matrix_with_duplicate_elements():
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 8]]
    with pytest.raises(ValueError):
        find_max_in_row_min_in_col(mat)

def test_matrix_with_max_values():
    mat = [[105] * 50] * 50
    assert find_max_in_row_min_in_col(mat) == [105]

def test_matrix_with_min_values():
    mat = [[1] * 50] * 50
    assert find_max_in_row_min_in_col(mat) == [1]

def test_matrix_with_all_max_values():
    mat = [[105] * 50] * 50
    mat[0][0] = 100
    assert find_max_in_row_min_in_col(mat) == []

def test_matrix_with_all_min_values():
    mat = [[1] * 50] * 50
    mat[0][0] = 2
    assert find_max_in_row_min_in_col(mat) == []
```
