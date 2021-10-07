# https://leetcode.com/problems/maximum-product-of-three-numbers/

# approach 1: brute force, TC = O(n log n), i.e timsort complexity
def maximumProduct(nums):
    if len(nums) == 3:
        return nums[0]*nums[1]*nums[2]
    
    # desceding order sort
    nums.sort(reverse=True)
        
    # 3 biggest
    bigs = nums[0]*nums[1]*nums[2]
    
    # maybe 2 negs * 1 pos
    n = nums[-1]*nums[-2]*nums[0]
    
    return max(n, bigs)


# approach 2: TC = O(n), just one for loop
def maximumProduct(nums):
    if len(nums) == 3:
        return nums[0]*nums[1]*nums[2]
    
    max1 = max2 = max3 = -math.inf
    min1 = min2 = math.inf
    
    for num in nums:
        if num <= min1:
            min2 = min1
            min1 = num
        # num lies b/w min1 and min2
        elif num <= min2:
            min2 = num
        
        # num is greater than max1, max2, max3
        if num >= max1:
            max3 = max2
            max2 = max1
            max1 = num
        elif num >= max2:
            max3 = max2
            max2 = num
        elif num >= max3:
            max3 = num
    
    # 2 negs and 1 pos vs 3 biggest
    return max(min1*min2*max1, max1*max2*max3)