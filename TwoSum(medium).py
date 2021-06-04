# https://leetcode.com/problems/two-sum/

def twoSum(nums, target):
    bufferr = {}
    
    for i in range(len(nums)):
        if nums[i] in bufferr:
            # then for every num we check if exists in the dictionary, if it does then
            # nums[j] = target - nums[i], the sol is then [i, j]
            # We can find i using the dict and we already have j
            return [bufferr[nums[i]], i]
        
        else:
            # first we create a dictionary of all the complements, 
            # where target - nums[i] is the key and the value is i the index
            bufferr[target - nums[i]] = i