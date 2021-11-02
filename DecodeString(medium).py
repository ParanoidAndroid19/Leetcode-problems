# Approach 1: 

def decodeString(self, s):
    """
    :type s: str
    :rtype: str
    """
    # start from inside out
    # start from char inside the most inner []

    i = 0
    j = len(s)-1

    # i should point to [, j should point to ]
    # b/w i and j is the encoded_string
    # and k is at i-1

    # keep checking if [] exists b/w i and j
    # if both [] exist b/w i and j, then move j behind, till ]
    # if i == [ or j == ] 
    while j < len(s):
        # finish case, everything has been decoded
        if '[' not in s and ']' not in s:
            break
        
        elif s[i] == '[' and s[j] == ']':
            # sucess case
            if '[' not in s[i+1:j] and ']' not in s[i+1:j]:
                k = i-1
                num = ''
                # counting the number to which encoded_string has to be multiplied
                while s[k].isdigit():
                    num = s[k] + num
                    k = k - 1
                # num * encoded_string
                new = int(num)*s[i+1:j]
                # replacing the encoded string with decoded string in the full string
                s = s[:i-len(num)] + new + s[j+1:]
                # reset two pointers, to go over the modified string
                i = 0
                j = len(s)-1
            
            # if [ exists, move i forward till [
            elif '[' in s[i+1:j]:
                i = i + 1

            # if ] exists, move j behind till ]
            elif ']' in s[i+1:j]:
                j = j - 1

        elif s[i] == '[' and s[j] != ']' and ']' in s[i+1:j]:
            j = j - 1

        elif s[j] == ']' and s[i] != '[' and '[' in s[i+1:j]:
            i = i + 1

        # if neither i nor j is pointing to bracket
        else:
            i = i + 1
            j = j - 1

    return s



# Approach 2:

def decodeString(s):
    countStack = []
    stringStack = []
    k = ""
    currStr = ""
    decodedStr = ""
    
    for i in range(0, len(s)):
        char = s[i]
        
        if char.isdigit():
            k = k + char
            
        elif char.isalpha():
            currStr = currStr + char
            
        elif char == '[':
            countStack.append(int(k))
            stringStack.append(currStr)
            
            k = ""
            currStr = ""
            
        elif char == ']':
            currK = countStack.pop()
            ds = stringStack.pop()
            
            decodedStr = ds + currK*currStr
        
            currStr = decodedStr
            
    return currStr