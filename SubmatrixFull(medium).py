def isSubmatrixFull(matrix):
    pos = 0
    n = len(matrix[0])
    
    output = []
    
    for pos in range(0, n-2):
        # 1 to 9 adds up to 45, check for that
        ssum = 0
        
        for row in range(0, 3):
            for col in range(pos, pos+3):
                ssum = ssum + matrix[row][col]
        
        if ssum == 45:
            output.append(True)
        else:
            output.append(False)
            
    return output
    
    
numbers = [[1, 2, 3, 2, 5, 7],
           [4, 5, 6, 1, 7, 6],
           [7, 8, 9, 4, 8, 3]]

print(isSubmatrixFull(numbers))