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