def rob(nums):

    n = len(nums)

    # base cases
    if n == 0:
        return 0
    elif n == 1:
        return nums[0]
    elif n == 2:
        return max(nums[0], nums[1])

    # init dp array and base cases
    # at index i, means that's the max profit till ith point
    # dp[i] represent the maximum value stolen so
    # far after reaching house i, at dp[n] we have the final solutions after reaching last house
    dp = [0]*n

    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    # starting from 2 since we already know the answer for dp[0] and dp[1]
    for i in range(2, n):
        # either rob ith house and i-2 or
        # rob i-1 house
        # either take ith house and alternate one before, or take previous house
        # choose the max of two choices for every ith house
        dp[i] = max(nums[i] + dp[i-2], dp[i-1])

    return dp[-1]