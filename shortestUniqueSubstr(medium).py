def get_shortest_unique_substring(arr, s):
    p1 = 0
    p2 = len(arr) # 3
    op = s
    flag = 0
    
    while p2 <= len(s): 
        sub = s[p1:p2] 
        if helper(arr, sub) == True:
          flag = 1
          if len(sub) < len(op):
            op = sub
          p1 = p1 + 1
        else:
          p2 = p2 + 1
      
    if flag == 0:
        return ""
      
    return op
    
# arr: x y z, s: x k y
def helper(arr, substr):
    for char in arr:
        if char not in substr:
            return False
    return True
    
    
print(get_shortest_unique_substring("ABC", "ADOBECODEBANC"))