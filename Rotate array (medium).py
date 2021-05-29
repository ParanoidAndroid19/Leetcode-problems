def rotate(nums, k):
    indexDict = {}

    for i in range(0, len(nums)):
        # indexDict[newIndex] = num
        indexDict[(i+k)%len(nums)] = nums[i]

    for newIndex in indexDict:
        # assigning the corresponding num to newIndex in nums array
        nums[newIndex] = indexDict[newIndex]

    return nums