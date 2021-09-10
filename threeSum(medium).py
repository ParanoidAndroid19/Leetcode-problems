# https://leetcode.com/problems/3sum/

def threeSum(nums):
    # sorted array two pointers on extreme end method
    
    # a + b + c = 0
    # a + b = 0 - target
    
    # to avoid repeats
    res = set()
    nums.sort()
    
    if len(nums) < 3:
        return []
    
    for i in range(0, len(nums)):
        target = 0 - nums[i]
        l = i+1
        r = len(nums) - 1
        
        while l < r and r < len(nums):
            if nums[l] + nums[r] == target:
                res.add((nums[i], nums[l], nums[r]))
                l = l + 1
                r = r - 1
                
            elif nums[l] + nums[r] < target:
                l = l + 1
                
            else:
                r = r - 1
                
    return list(res)


print(threeSum([-1,0,1,2,-1,-4]))