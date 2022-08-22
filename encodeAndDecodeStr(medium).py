# def encode(strs):
#     """Encodes a list of strings to a single string.
#     """
#     singleStr = ''
#     for strr in strs:
#         n = len(strr)
#         singleStr = singleStr + strr + '|' + str(n) + '|'
        
#     return singleStr
    

# # eg: ['hello', 'world']
# # 'hello|5|world|5|'


# def decode(s):
#     """Decodes a single string to a list of strings.
#     """
#     res = []
#     n = len(s)
#     strr = ''
#     extraStrr = ''
#     snum = None
    
#     for i in range(n):
#         char = s[i]
#         if s[i] == '|':
#             extraStrr = extraStrr + s[i]
#             # closing |
#             if snum != None:
#                 num = int(snum)
#                 if num == len(strr):
#                     res.append(strr)
#                     strr = ''
#                     extraStrr = ''
#                     snum = None
#                 else:
#                     strr = strr + extraStrr
#                     extraStrr = ''
#             else:
#                 if i+1 != n and s[i+1].isdigit():
#                     snum = ''
#                 else:
#                     strr = strr + extraStrr
#                     extraStrr = ''
                    
        
#         elif snum != None:
#             extraStrr = extraStrr + s[i]
#             if s[i].isdigit():
#                 snum = snum + s[i]
#             else:
#                 strr = strr + extraStrr
#                 extraStrr = ''
#                 snum = None
        
#         else:
#             strr = strr + s[i]
#             snum = None
        
#     return res
    
    
# print(["","PJ|","Q.lF2 awD"])
# encodedStr = encode(["","PJ|","Q.lF2 awD"])
# print(encodedStr)
# print(decode(encodedStr))


def encode(self, strs: List[str]) -> str:
    """Encodes a list of strings to a single string.
    """
    singleStr = ''
    
    for strr in strs:
        snum = str(len(strr))
        
        while len(snum) < 3:
            snum = '0' + snum
        
        singleStr = singleStr + snum + strr
        
    return singleStr
    
# my sol
# eg: ['hello', 'world']
# 'hello|5|world|5|'

# better sol
# unlike my solution, this solution doesn't depend on chars at all, it 
# just knows for instance after 5 chars the word ends.
# '005hello005world'

def decode(self, s: str) -> List[str]:
    """Decodes a single string to a list of strings.
    """
    n = len(s)
    
    i = 0
    
    res = []
    
    while i < n:
        strLen = int(s[i:i+3])
        i = i + 3
        strr = s[i:i+strLen]
        res.append(strr)
        i = i + strLen
        
    return res
        