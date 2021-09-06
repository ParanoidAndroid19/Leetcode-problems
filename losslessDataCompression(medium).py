# https://app.codesignal.com/company-challenges/dropbox/7mqgw4QPQwPPgpRgu

def losslessDataCompression(s, width):
    i = 0
    res = ''
    
    while i < len(s):
        if i < width:
            window = s[0:i]
            offset = 0
        else:
            window = s[i-width:i]
            offset = i-width
        
        start = i
        end = i+1
        
        if s[i] in window:
            while s[start:end] in window and end <= len(s):
                ss = s[start:end]
                end = end + 1
            end = end - 1
        else:
            res = res + s[i]
            i = i + 1
            # move to the next iteration, without going any further
            continue
        
        length = len(s[start:end])
        startIndex = window.find(s[start:end]) + offset
        
        res = res + '(' + str(startIndex) + ',' + str(length) + ')'
        
        i = i + length
        
    return res
        
    
print(losslessDataCompression("abacabadabacaba"))
# expected output: "ab(0,1)c(0,3)d(4,3)c(8,3)"

