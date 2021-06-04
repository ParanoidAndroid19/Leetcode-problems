# https://leetcode.com/problems/count-and-say/

def countAndSay(n):
    # base case 
    if n == 1:
        return "1"
    
    res = ""
    prevStr = countAndSay(n-1)
    count = 0
    
    for i in range(len(prevStr)):
        # regardless of char is repeating or not count will be at least 1
        count = count + 1
        
        # if char is not repeating, reset count to 0
        if(i+1 >= len(prevStr) or prevStr[i+1] != prevStr[i]):
            nstr = str(count) + prevStr[i]
            res = res + nstr
            count = 0
        
    return res


print(countAndSay(6))