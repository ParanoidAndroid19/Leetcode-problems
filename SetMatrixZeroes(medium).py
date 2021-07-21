# https://leetcode.com/problems/set-matrix-zeroes/

def setZeroes(matrix):
    rows = {}
    cols = {}

    # Step 1: Iterate through the matrix (2D array) and note the position
    # (i (row) and j (column)) of 0 elements.
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                rows[i] = True
                cols[j] = True

    # Again iterate through the matrix and if for an element, i or j
    # are in rows or cols dictionary then make that element 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if rows.get(i, False) or cols.get(j, False):
                matrix[i][j] = 0