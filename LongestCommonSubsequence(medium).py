# Top-down memoization approach
def longestCommonSubsequence(text1, text2):

    @lru_cache(maxsize=None)
    def memo_solve(ptr1, ptr2):
        if ptr1 == len(text1) or ptr2 == len(text2):
            return 0
        
        # Case 1
        if text1[ptr1] == text2[ptr2]:
            return 1 + memo_solve(ptr1+1, ptr2+1)
    
        # Case 2
        else:     
            return max(memo_solve(ptr1+1, ptr2), memo_solve(ptr1,ptr2+1))
    
    
    # Start the recursion stack from str1[0] and str2[0]
    return memo_solve(0,0)



# Bottom-up tabulation approach
def lCS(text1, text2):
    # text1 is written vertically and text2 horizontally
    dp = [[0 for i in range(len(text2) + 1)] for j in range(len(text1) + 1)]
    
    text1 = " " + text1
    text2 = " " + text2
    
    for i in range(1, len(text1)):
        for j in range(1, len(text2)):
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
    return dp[-1][-1]
