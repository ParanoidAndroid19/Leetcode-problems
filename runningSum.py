class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        d = {}
        d[0] = nums[0]

        for i in range(1, len(nums)):
            d[i] = d[i-1] + nums[i]

        return d.values()
            
