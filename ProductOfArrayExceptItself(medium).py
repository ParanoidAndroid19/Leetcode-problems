# https://leetcode.com/problems/product-of-array-except-self/

def productExceptSelf(self, nums: List[int]) -> List[int]:
    ans = []

    # product before the ith element
    p = 1
    for i in range(0, len(nums)):
        ans.append(p)
        p = p * nums[i]

    # product after the ith element
    p = 1
    for j in range(len(nums)-1, -1, -1):
        ans[j] = ans[j] * p
        p = p * nums[j]

    return ans


