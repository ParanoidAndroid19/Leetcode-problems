def countSubstrings(self, s: str) -> int:
    n = len(s)
    
    # at least every char in str is a palindrome
    count = n
    
    # init nxn dp matrix with all values set as False
    dp = [[False]*n for _ in range(n)]
    
    # every char in itself is a palindrome, mark as true
    for i in range(n):
        dp[i][i] = True
        
    # starting from bottom right
    # only considering cases where start < end
    for start in range(n-1, -1, -1):
        for end in range(start+1, n):
            # palindrome condition
            if s[start] == s[end]:
                # if s(start, end) is just two chars or substring inside is palindrome 
                if end - start == 1 or dp[start+1][end-1]:
                    count = count + 1
                    dp[start][end] = True
                    
    return count