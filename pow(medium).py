# https://leetcode.com/problems/powx-n/

# iterative
def myPow(self, x, n):
    # default 
    poww = 1
    
    if n < 0:
        x = 1/x
        n = -n
        
    while n > 0:
        # odd or the last iteration
        if n % 2 == 1:
            poww = x * poww
            n = n - 1
        # even
        else:
            x = x * x
            n = n/2
            
    return poww


# recursive
def myPow(self, x, n):
    if n == 0:
        return 1
    
    elif n < 0:
        # making x = 1/x and n positive
        return self.myPow(1/x, -n)
    
    # even
    elif n % 2 == 0:
        return self.myPow(x * x, n / 2)
    
    # odd
    else:
        return x * self.myPow(x, n - 1)
    