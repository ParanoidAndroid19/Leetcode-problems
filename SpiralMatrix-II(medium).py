# https://leetcode.com/problems/spiral-matrix-ii/

def generateMatrix(self, n: int) -> List[List[int]]:
    # initialise matrix
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    
    i = 1
    
    directions = ['lr', 'ud', 'rl', 'du']
    d = 0
    inwards = 0
    
    row = col = 0
    
    while i <= n*n:
        if directions[d] == 'lr':
            while col < n - inwards:
                matrix[row][col] = i
                col = col + 1
                i = i + 1
            
            col = col - 1
            row = row + 1
            
            
        elif directions[d] == 'ud':
            while row < n - inwards:
                matrix[row][col] = i
                row = row + 1
                i = i + 1
                
            row = row - 1
            col = col - 1
            
            
        elif directions[d] == 'rl':
            while col >= inwards:
                matrix[row][col] = i
                col = col - 1
                i = i + 1
                
            col = col + 1
            row = row - 1
            
        else:
            inwards = inwards + 1
            while row >= inwards:
                matrix[row][col] = i
                row = row - 1
                i = i + 1
                
            row = row + 1
            col = col + 1
            
        d = (d+1)%len(directions)
        
    return matrix