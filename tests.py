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