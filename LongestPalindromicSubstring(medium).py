
# DP top-down tabulation approach

def longestPalindrome(s):
    n = len(s)
    
    # creating dp table, n*n 2d array
    # dp[i][j] will be true if string from index i to j is a palindrom
    # i.e s[i:j+1] is a palindrome
    dp = [[False]*n for _ in range(n)]
    
    ans = ''
    # base case
    # every string with single char is palindrome
    # The diagonal in dp table is true
    for i in range(n):
        dp[i][i] = True
        # in case of s is single char str or just two char
        ans = s[i]
        
    maxLen = 1
    
    # not traversing the bottom part of the diagonal because
    # start cannot be greater than end
    # starting from bottom right cell because we need to do 
    # start+1 and end-1 to check for palindrome
    # the pairs would be like: 3:4, 2:3, 2:4, 1:2, etc
    for start in range(n-1, -1, -1):
        for end in range(start+1, n):
            # palindrome condition
            if s[start] == s[end]:
                # if two char string or if remaining str is palindrome
                if end - start == 1 or dp[start+1][end-1]:
                    dp[start][end] = True
                    # longest
                    if maxLen < end - start + 1:
                        maxLen = end - start + 1
                        ans = s[start:end+1]
                        
    return ans
    

print(longestPalindrome('cbbd'))