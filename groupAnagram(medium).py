# https://leetcode.com/problems/group-anagrams/

# Approach 1 and 2:

def groupAnagrams(self, strs):
    keyDict = {}
    op = []
    
    for strr in strs:
        # countDict = self.getCount(strr)
        # flat = tuple(sorted(countDict.items()))
        flat = tuple(sorted(strr))
        if flat not in keyDict:
            keyDict[flat] = [strr]
        else:
            keyDict[flat].append(strr)
        
    # for key in keyDict:
    #     op.append(keyDict[key])
        
    return keyDict.values()
    
    
#     def getCount(self, strr):
#         d = {}
    
#         for char in strr:
#             d[char] = d.get(char, 0) + 1
        
#         return d
    

# Approach 3: ASCII ord values

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    # ord() style
    
    keyDict = {}
    
    for strr in strs:
        count = [0]*26
        
        for char in strr:
            index = ord(char) - ord('a')
            count[index] = count[index] + 1
            
        # key is the count pattern for strr
        k = tuple(count)
        
        if k in keyDict:
            keyDict[k].append(strr)
        else:
            keyDict[k] = [strr]
            
    return keyDict.values()