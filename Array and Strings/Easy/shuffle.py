# My solution:
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x = nums[:n]
        y = nums[n:]
        res = []
        a = -1
        b = -1

        if n==1:
            res.append(x[0])
            res.append(y[0])
            return res


        for i in range(0, len(nums)):
            if a<n and b<n:
                if i%2==0:
                    a=a+1
                    res.append(x[a])

                elif(i%2!=0):
                    b=b+1
                    res.append(y[b])


        return res



# Faster solution:
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x = nums[:n]
        y = nums[n:]
        res = []

        for i in range(0, n):
            res.append(x[i])
            res.append(y[i])

        return res
