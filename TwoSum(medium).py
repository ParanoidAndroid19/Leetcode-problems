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




# more verbose solution:

def twoSum(nums, target):
    d = {}
    # 1st iteration
    # num1 = nums[i] = nums[0]
    # num2 = target - num1 = 9 - 2 = 7
    # d[num2] = index of num1 = i = 0
    
    for i in range(len(nums)):
        if nums[i] in d:
            num2 = nums[i]
            # index of num1
            j = d[num2]
            # i is index of num2
            return [j, i]
        
        else:
            num1 = nums[i]
            num2 = target - num1
            # index of num1
            d[num2] = i