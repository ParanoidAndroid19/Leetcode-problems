# https://leetcode.com/problems/decode-ways/

# Approach 1: Top down memoization

memo = {}

def numDecodings(s):
    """
    :type s: str
    :rtype: int
    """
    # count = 0
    # i = 0
    
    return recur(s)
    
    
def recur(s):
    # if I make it till the end of string
    if len(s) == 0:
        return 1

    if s in memo:
        return memo[s]

    count1 = count2 = 0

    # grouping 1 char
    # if 1 char, then it should be b/w 1 to 9
    # if s[:1][0] != '0' and len(s[:1]) >= 1:
    if 1 <= int(s[:1]) and int(s[:1]) <= 9:
        # print(s[:1])
        count1 = recur(s[1:])

    # grouping 2 char
    # if 2 char, then it should be b/w 10 to 26
    # if s[:2][0] != '0' and len(s[:2]) >= 2:
    if 10 <= int(s[:2]) and int(s[:2]) <= 26:
        # print(s[:2])
        count2 = recur(s[2:])

    # count = count1 + count2
    memo[s] = count1 + count2

    return memo[s]
    

print(numDecodings("11106"))


# Approach 2: Bottom up dp

def numDecodings(self, s: str) -> int:
    # remember you don't even have to decode it, just count the number of ways
    # this is similar to word break
    # here at every point there is an option, either you can condsider 1 char or 2 char str
    # since all alphabets have at most 2 char len str code
    
    # def isValid to check if we are not considering thing like "06" and num <= 26
    
    # or a dp sol
    # "1. 2"
    # [1, 2] (final arr[-1] +1 if entire str can be considered as valid code)
    
    # "2  2  6"
    # [1, 2, 3]
    
    # "0. 6"
    # [0, 0]
    
    # "1. 1. 1  0. 6" (if zero always join it with preceeding num?)
    # [1, 2, 2, 2, 2]
    
    # dp[i-1] + 1(if entire str[i-1:i+1] is valid code)
    
    # soooo close
    
    #s    2  1. 0  1
    # [1, 1, 2, 1, 1]
    
    # so dp[i] would contain num of ways to decode the string s[:i] 
    # technically till s[i-1]
    dp = [0 for _ in range(len(s)+1)]
    dp[0] = 1
    
    if s[0] != "0":
        dp[1] = 1
        
    for i in range(2, len(dp)):
        
        # for ways to decode single digit, that would be dp leading to it
        if s[i-1] != "0":
            dp[i] = dp[i-1]
            
        doubleDigit = int(s[i-2:i])
        
        # no. of ways to decode two digits, that would be the dp leading to the 1st digit
        if 10 <= doubleDigit and doubleDigit <= 26:
            dp[i] = dp[i] + dp[i-2]
            
    return dp[-1]
    
#         dp = [0 for _ in range(len(s))]
    
#         if s[0] != "0":
#             dp[0] = 1
        
#         for i in range(1, len(s)):
#             print(s[i])
#             dp[i] = dp[i-1]
        
#             two = int(s[i-1:i+1])
        
#             if 11 <= two and two <= 26:
#                 dp[i] = dp[i] + 1
    
#         print('dp', dp)
            
#         return dp[-1]