def isOk(self, line: list) -> bool:
    dots = line.count('.')
    num_nums = len(line) - dots
    # checks for repetitions
    if dots == 0:
        set_dots = 0
    else:
        set_dots = 1
        
    return num_nums == len(set(line))-set_dots

def isValidSudoku(self, board: List[List[str]]) -> bool:
    # use set to check repetition
    
    for row in board:
        if self.isOk(row) == False:
            print(row)
            return False
    
    # row is col and col is row
    col_board = list(zip(*board))
    for col in col_board:
        if self.isOk(col) == False:
            print(col)
            return False
        
    squares = []
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            sq = []
            for r in board[row:row+3]:
                sq = sq + r[col:col+3]
                if self.isOk(sq) == False:
                    print(sq)
                    return False
            
        
    return True
    # board = [["5","3",".",".","7",".",".",".","."]
    #         ,["6",".",".","1","9","5",".",".","."]
    #         ,[".","9","8",".",".",".",".","6","."]
    #         ,["8",".",".",".","6",".",".",".","3"]
    #         ,["4",".",".","8",".","3",".",".","1"]
    #         ,["7",".",".",".","2",".",".",".","6"]
    #         ,[".","6",".",".",".",".","2","8","."]
    #         ,[".",".",".","4","1","9",".",".","5"]
    #         ,[".",".",".",".","8",".",".","7","9"]]