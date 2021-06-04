# https://leetcode.com/problems/move-zeroes/

def moveZeroes(nums):
    p1 = 0
    p2 = 1
    
    while p1 < len(nums) and p2 < len(nums):
        # normal
        if nums[p1] == 0 and nums[p2] != 0:
            nums[p1], nums[p2] = nums[p2], nums[p1]
            p1 = p1 + 1
        
        elif nums[p1] != 0:
            p1 = p1 + 1
            
        p2 = p2 + 1
            
    return nums