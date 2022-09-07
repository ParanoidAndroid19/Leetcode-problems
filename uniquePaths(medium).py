def uniquePaths(self, m: int, n: int) -> int:
    
    dp = [[0 for _ in range(n)] for _ in range(m)]
    
    # since bot is already at this pos
    dp[0][0] = 1

    # bot is at top left corner
    
    # because in the first (0th) row, bot can come from only 1 direction, that is left, since a top cell
    # doesn't exist
    for col in range(1, n):
        dp[0][col] = 1
    
    # because in the first (0th) col, bot can come from only 1 direction, that is top, since right cell
    # doesn't exist
    for row in range(1, m):
        dp[row][0] = 1
        
    for row in range(1, m):
        for col in range(1, n):
            # the bot can move to the cell(row, col) either from left or top
            dp[row][col] = dp[row][col-1] + dp[row-1][col]
            
    return dp[m-1][n-1]
