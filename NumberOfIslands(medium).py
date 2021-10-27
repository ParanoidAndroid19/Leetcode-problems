# https://leetcode.com/problems/number-of-islands/

from collections import deque

def numIslands(grid):
    islands = 0
    # visited = set()
    rows = len(grid)
    cols = len(grid[0])
    
    #             down,   right,    up,     left
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    
    # Basically for every row, col position do bfs 
    # (add down, right, up, left cells to queue like you usually 
    # do for left and right child nodes). Also maintain a set of 
    # visited cells or after visiting a land cell make it 
    # '0' to mark as visited.

    def bfs(r, c):
        queue = deque()
        grid[r][c] = '0'
        # visited.add((r, c))
        queue.append((r, c))
        
        while len(queue) != 0:
            curr_row, curr_col = queue.popleft()
            
            for dr, dc in directions:
                n_row = curr_row + dr
                n_col = curr_col + dc
                
                if (n_row in range(rows) and 
                    n_col in range(cols) and 
                    grid[n_row][n_col] == '1'):
                    queue.append((n_row, n_col))
                    grid[n_row][n_col] = '0'
                    # visited.add((n_row, n_col))
    
    
    for r in range(rows):
        for c in range(cols):
            # remember we'll enter this part only if land cell is not visited
            # if it is visited then it's '0'
            if grid[r][c] == '1':
                bfs(r, c)
                islands = islands + 1
                
    return islands