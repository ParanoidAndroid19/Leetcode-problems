# https://leetcode.com/problems/first-unique-character-in-a-string/

# Remember in python 2 dictionary keys are rearranged in alphabetical order

def firstUniqChar(s):
    freqDict = {}
        
    for char in s:
        freqDict[char] = freqDict.get(char, 0) + 1
        
    for i in range(len(s)):
        if freqDict[s[i]] == 1:
            return i
        
    return -1