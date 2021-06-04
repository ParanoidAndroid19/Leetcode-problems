# https://leetcode.com/problems/valid-palindrome/

def isPalindrome(s):
    p1 = 0
    p2 = len(s) - 1

    while p1 < p2:
        # if char at p1 is not alphabet or number
        if s[p1].isalnum() == False:
            p1 = p1 + 1
        
        # if char at p2 is not alphabet or number
        if s[p2].isalnum() == False:
            p2 = p2 - 1

        # if both are alphabet or number
        if s[p1].isalnum() and s[p2].isalnum():    
            if s[p1].lower() == s[p2].lower():
                p1 = p1 + 1
                p2 = p2 - 1
            else:
                return False

    return True

print(isPalindrome("A man, a plan, a canal: Panama"))