def canJump(nums):    
    #  0. 1. 2. 3. 4
    # [2, 3, 1, 1, 4]
    #  .  .  .  G  G
    
    #  0. 1. 2. 3. 4  5. 6
    # [5, 4, 3, 2, 1, 0, 0]
    #                 B  G
    
    # good index is a index using which we can reach the goal index (len(nums)-1)
    # init the last index as lastGoodIndex
    lastGoodIndexPos = len(nums) - 1
    
    for i in range(len(nums) - 2, -1, -1):
        # check if lastGoodIndexPos can be reached from i
        if lastGoodIndexPos <= i + nums[i]:
            lastGoodIndexPos = i
            
    if lastGoodIndexPos == 0:
        return True
    else:
        return False
    
        