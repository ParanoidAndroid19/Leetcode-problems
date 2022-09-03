class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        
        # like 0th row has how many X's, that would be rows1[0]
        self.rows1 = [0 for _ in range(n)]
        # like 0th row has how many 0's, that would be rows2[0]
        self.rows2 = [0 for _ in range(n)]
        
        self.leftToRight1 = 0
        self.leftToRight2 = 0
        
        self.rightToLeft1 = 0
        self.rightToLeft2 = 0
        
        self.cols1 = [0 for _ in range(n)]
        self.cols2 = [0 for _ in range(n)]     
        

    def move(self, row: int, col: int, player: int) -> int:
        n = self.n
        
        if player == 1:
            # horizontal win
            self.rows1[row] = self.rows1[row] + 1
            if self.rows1[row] == n:
                return 1
            
            # vertical win
            self.cols1[col] = self.cols1[col] + 1
            if self.cols1[col] == n:
                return 1
            
            # diagonal win
            if row == col:
                self.leftToRight1 = self.leftToRight1 + 1
                if self.leftToRight1 == n:
                    return 1
                
            # anti diagonal win
            if col == n-row-1:
                self.rightToLeft1 = self.rightToLeft1 + 1
                if self.rightToLeft1 == n:
                    return 1
                
            return 0
        
        if player == 2:
            # horizontal win
            self.rows2[row] = self.rows2[row] + 1
            if self.rows2[row] == n:
                return 2
            
            # vertical win
            self.cols2[col] = self.cols2[col] + 1
            if self.cols2[col] == n:
                return 2
            
            # diagonal win
            if row == col:
                self.leftToRight2 = self.leftToRight2 + 1
                if self.leftToRight2 == n:
                    return 2
                
            # anti diagonal win
            if col == n-row-1:
                self.rightToLeft2 = self.rightToLeft2 + 1
                if self.rightToLeft2 == n:
                    return 2
                
            return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)