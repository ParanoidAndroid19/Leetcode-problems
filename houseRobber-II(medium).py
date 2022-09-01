def rob(nums):
    # same logic as house robber - I
    def robPart(nums):
        n = len(nums)

        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])

        dp = [0]*n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])

        return dp[-1]
    
    
    # edge case
    if len(nums) == 1:
        return nums[0]
    
    # Since House[0] and House[n-1] are adjacent, they cannot be robbed together.
    # Therefore, the problem becomes to rob either House[0]-House[n-2] or 
    # House[1]-House[n-1], depending on which choice offers more money.

    # array of houses excluding the last house
    firstNums = nums[:-1]
    # array of houses excluding the first house
    lastNums = nums[1:]
    
    return max(robPart(firstNums), robPart(lastNums))