# Solution 1: My sol, TLE

# def combinationSum4(self, nums: List[int], target: int) -> int:
#     res_set = set()

#     # dp[1] = [[1]]
#     # dp[2] = [[1, 1], [2]]
#     # dp[3] = [[1, 1, 1], [1, 2], [3]]
#     # dp[4] = [[1, 1, 1, 1], [1, 2, 1], [2, 2], [3, 1]]

    # for combinations, you don't actually have to make them
    # just look at the array size and calculate the no. of combinations possible, account for repeats 
    # too

#     dp = {}

#     # base case, when target is 0 you will have zero combos
#     dp[0] = 0

#     for num in nums:
#         dp[num] = [[num]]

#     for tar in range(1, target+1):
#         for num in nums:
#             currTar = tar
#             if num < currTar:
#                 temp = currTar
#                 currTar = currTar - num

#                 if currTar in dp:
#                     for comb in dp[currTar]:
#                         newComb = comb[:]
#                         newComb.append(num)
#                         if temp in dp:
#                             dp[temp].append(newComb)
#                         else:
#                             dp[temp] = [newComb]

#     # print(dp)
    
#     if target in dp:
#         return len(dp[target])
#     else:
        # return 0


# Solution 2: Don't actually make the combinations, the count them

def combinationSum4(self, nums: List[int], target: int) -> int:    
    dp = [0 for i in range(target+1)]
    dp[0] = 1
    
    for comb_sum in range(target+1):
        for num in nums:
            if comb_sum - num >= 0:
                # so for instance 2: dp[2] = dp[2-1] + dp[2-2] = d[1] + dp[0] = 2
                dp[comb_sum] = dp[comb_sum] + dp[comb_sum - num]
                
    return dp[target]