# top-down: memoization
def climbStairs(n):
    # base cases: 0 step and 1 step can be done in 1 unique way
    d = {0: 1, 1: 1}

    recur(n)

def recur(n):
    # if the unique ways has already been calculated for n
    if n in d:
        return d[n]

    else:
        # since the sol for n is the sum of unique steps required for n-1 steps and n-2 steps
        d[n] = recur(n-1) + recur(n-2)


# bottom up
def climbStairs(n):
    if n == 0 or n == 1:
        return 1

    # base cases
    prev2 = 1
    prev1 = 1

    for i in range(2, n+1):
        curr = prev2 + prev1
        prev2 = prev1
        prev1 = curr

    return curr

