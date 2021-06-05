# Solution 1: The brute force intuitive solutions I came up with:

# highestSum = -10**5
# subArray = []
# nums = [-2,1,-3,4,-1,2,1,-5,4]

# if(len(nums) == 1):
#     return nums[0]
#     print(nums)

# else:
#     for i in range(0, len(nums)+1):
#         for j in range(i+1, len(nums)+1):
#             parr = nums[i:j]
#             psum = sum(parr)
#             if(psum > highestSum):
#                 highestSum = psum
#                 subArray = parr
    
#     return highestSum



# Solution 2: The correct solution using dynamic programming, 
# Kadane's Algorithm, complexity O(N)

nums = [-2,1,-3,4,-1,2,1,-5,4]
currentSubsum = nums[0]
maxSubsum = nums[0]

# starting with 1st since, 0th is already considered in current and max subsum
for num in nums[1:]:
    # here we are getting rid or negatives which bring down the sum
    currentSubsum = max(num, currentSubsum + num)
    
    # this is the value which will be returned
    maxSubsum = max(maxSubsum, currentSubsum)

return maxSubsum
