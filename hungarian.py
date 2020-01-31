import numpy as np

class Point(object):
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value

def brute_force(matrix, selected=None):
    matrix_size = matrix.shape[0]
    if matrix_size == 1:
        return matrix[0], selected
    first_layer = False
    if selected != None:
        selected_index = len(selected)
        total = 0
        for point in selected:
            total += point.value
        sub_total = total
    else:
        selected_index = 0
        first_layer = True
        selected = []
        total = float("inf")
        sub_total = 0
    for i in range(matrix_size):
        p = Point(i, 0, matrix[0, i])
        sub_matrix = np.delete(matrix, 0, 0)
        sub_matrix = np.delete(sub_matrix, i, 1)

        sub_total += p.value
        if first_layer:
            print("sub_matrix", p.value,"\n", sub_matrix)
        selected.append(p)
        new_sub_total, selected = brute_force(sub_matrix, selected)
        sub_total += new_sub_total
        if sub_total < total:
            total = sub_total
            print("!!!!!!1")
        else:
            selected.remove(p)
    return total, selected

def hungarian(matrix):
    min_rows = row_reduction(matrix)
    print("min_rows:\n", min_rows)
    print("row_reduction matrix:\n", matrix)
    min_cols = col_reduction(matrix)
    print("min_cols:\n", min_cols)
    print("col_reduction matrix:\n", matrix)

def row_reduction(matrix):
    matrix_size = matrix.shape[0]
    min_rows = []
    for i in range(matrix_size):
        min_row = float("inf")
        for j in range(matrix_size):
            if matrix[i, j] < min_row:
                min_row = matrix[i, j]
        min_rows.append(min_row)
        matrix[i, :] -= min_row
    return min_rows

def col_reduction(matrix):
    matrix_size = matrix.shape[0]
    min_cols = []
    for j in range(matrix_size):
        min_col = float("inf")
        for i in range(matrix_size):
            if matrix[i, j] < min_col:
                min_col = matrix[i, j]
        min_cols.append(min_col)
        matrix[:, j] -= min_col
    return min_cols


if __name__ == "__main__":
    matrix = np.array([[3,6,4,2],[9,10,7,0],[2,10,0,7],[6,3,3,7]])
    print("matrix:\n", matrix)
    matrix = 10-matrix
    print("inverse matrix:\n", matrix)
    total, selected = brute_force(matrix)
    print("total", total)
    for point in selected:
        print("{}x {}y: {}".format(point.x, point.y, point.value))