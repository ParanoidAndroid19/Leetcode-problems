# https://leetcode.com/problems/maximum-product-subarray/

def maxProduct(self, nums: List[int]) -> int:
    # APPROACH : KADANES ALGORITHM
    
    # Edge Case : Negative * Negative = Positive
    # So we need to keep track of minimum values also, 
    # as they can yield maximum values.
    
    global_max = prev_max = prev_min = nums[0]
    
    for num in nums[1:]:
        # recording min, as it can lead to maximum in edge case
        curr_min = min(prev_min*num, prev_max*num, num)
        # recording max
        curr_max = max(prev_min*num, prev_max*num, num)
        # this value will be returned
        global_max = max(global_max, curr_max)
        
        prev_min = curr_min
        prev_max = curr_max
        
    return global_max