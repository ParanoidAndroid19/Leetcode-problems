# https://leetcode.com/problems/coin-change/

# Approach: Bottom-up tabulation

import math

def coinChange(coins, amount):
    # math.inf so that min comparison works
    # amount + 1, so that amount is covered in index
    arr = [math.inf]*(amount+1)

    # base case: to make 0 change 0 coins are required
    arr[0] = 0

    # solving for all subproblems, from 1 to amount+1
    for i in range(1, amount+1):
        # exploring all coin options to get the fewest coins required
        for coin in coins:
            # consider coin as an option only if it's less than or equal to amt
            if coin <= i:
                change = i - coin
                # +1 because I just used 1 coin, arr[change] is used to get subproblem sol
                # this is compared with existing no. of coins required to make i change, that is arr[i]
                minn = min(1+arr[change], arr[i])
                # so that min value is updated
                arr[i] = minn

    if arr[amount] == math.inf:
        return -1

    return arr[amount]