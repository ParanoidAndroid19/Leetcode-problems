def rotate(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    
    # Transpose + reverse
    n = len(matrix[0])
    
    for row in range(0, n):
        for col in range(row, n):
            # transpose
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        # reverse
        matrix[row] = matrix[row][::-1]


matrix = [[1,2,3],[4,5,6],[7,8,9]]
rotate(matrix)