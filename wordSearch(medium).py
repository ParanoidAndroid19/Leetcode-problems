# https://leetcode.com/problems/word-search/

def exist(self, board: List[List[str]], word: str) -> bool:
    # for every cell check all 4 neighbours, left, down, right, up
    directions = [[0, -1], [1, 0], [0, 1], [-1, 0]]
    
    
    def backtrack(row, col, suffix):
        if len(suffix) == 0:
            return True
        
        if row not in range(0, len(board)) or col not in range(0, len(board[0])) or board[row][col] != suffix[0]:
            return False
        
        
        # mark visited, so that when checking board[row][col] != suffix[0], same letter is not counted again
        board[row][col] = '#'
        
        # explore all 4 neighbours
        for d in directions:
            n_row = row + d[0]
            n_col = col + d[1]
            
            if backtrack(n_row, n_col, suffix[1:]):
                return True
            
        # if row, col didn't lead to word, mark it as unvisited again
        board[row][col] = suffix[0]
        
        return False
                
        
    
    for r in range(len(board)):
        for c in range(len(board[0])):
            if(board[r][c] == word[0]):
                if backtrack(r, c, word):
                    return True
            
    return False
            