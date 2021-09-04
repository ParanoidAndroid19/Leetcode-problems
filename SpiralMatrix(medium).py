def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
    # basic idea:
    # move left to right till you hit a wall, then up to down, then right to left
    # then down to up. Then the walls move inwards by one unit on each side. Repeat!
    
    m_rows = len(matrix)
    n_cols = len(matrix[0])
    
    # total number of elements that would be in the output array
    total =  m_rows * n_cols
    inwards = 0
    output = []
    row = col = 0
    
    direction = ['lr', 'ud', 'rl', 'du']
    
    d = 0
    
    while len(output) < total:
        if direction[d] == 'lr':
            while col < n_cols - inwards:
                output.append(matrix[row][col])
                col = col+1
            # to keep in bounds
            col = col - 1
            # to avoid repetition in output array, this is for the next direction loop
            row = row + 1
        
        elif direction[d] == 'ud':
            while row < m_rows - inwards:
                output.append(matrix[row][col])
                row = row+1
            # to keep in bounds
            row = row - 1
            # to avoid repetition in output array, this is for the next direction loop
            col = col - 1
            
        elif direction[d] == 'rl':
            while col >= inwards:
                output.append(matrix[row][col])
                col = col-1
            # to keep in bounds
            col = col + 1
            # to avoid repetition in output array, this is for the next direction loop
            row = row - 1
            
        else:
            # incrementing inwards here since from here the walls move closer by 1 row
            inwards = inwards + 1
            while row >= inwards:
                output.append(matrix[row][col])
                row = row-1
            # to keep in bounds
            row = row + 1
            # to avoid repetition in output array, this is for the next direction loop
            col = col + 1
            
        # for cyclic itertion in directions array
        d = (d+1)%len(direction)
        
    return output