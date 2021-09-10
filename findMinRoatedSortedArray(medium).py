def findMin(nums):
    
    if len(nums) == 1:
        return nums[0]
    
    left = 0
    right = len(nums) - 1
    
    # if the last element is greater than the first element then there is no rotation.
    # e.g. 1 < 2 < 3 < 4 < 5 < 7. Already sorted array.
    # Hence the smallest element is first element. A[0]
    if nums[left] < nums[right]:
        return nums[left]
    
    # modified binary search
    while left <= right:
        mid = (left+right)//2
        
        # success conditions
        # This point would be the point of change. From higher to lower value.
        if nums[mid] > nums[mid + 1]:
            return nums[mid + 1]
        
        if nums[mid - 1] > nums[mid]:
            return nums[mid]
        
        # deciding conditions
        # if the mid elements value is greater than the 0th element this means, point of inflection is yet to come
        # the least value is still somewhere to the right as we are still dealing with elements greater than nums[0]
        if nums[0] < nums[mid]:
            left = mid + 1
        
        # if nums[0] is greater than the mid value then this means, the point of inflection has passed us 
        # the smallest value is somewhere to the left
        else:
            right = mid - 1


print(findMin([4,5,6,7,0,1,2]))