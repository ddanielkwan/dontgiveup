# Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.

# Return the minimized largest sum of the split.

# A subarray is a contiguous part of the array.

 

# Example 1:

# Input: nums = [7,2,5,10,8], k = 2
# Output: 18
# Explanation: There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.

# class Solution:
#     def splitArray(self, nums: List[int], k: int) -> int:

#         n = len(nums)
#         #dp = [[-1] * (k + 1) for _ in range(n)]
#         # cache
#         dp = [[-1] * (k + 1) for _ in range(n)]
#         #backtracking

#         #what is the state, index, and m, m is how many splits
#         #we will decrement on each split

#         def dfs(i, m):
#             if i == n :
#                 # If we used all numbers:if we ALSO used exactly all groups → valid
# # otherwise invalid
#                 return 0 if m == 0 else float("inf")
#                 #No numbers left but still need 2 groups” impossible
            
#             if m == 0: #If we still have numbers left but no groups left,that’s impossibletoo
#                 return float("inf")
#             if dp[i][m] != -1:
#                 return dp[i][m]
            
#             res = float("inf")
#             curSum = 0

#             for j in range(i , n - m + 1): #thi sis tricky, this loop tries to tell us all possible indices j that the group can end, why n - m + 1? we have to make sure that there is at one element for each of the remaining (m - 1) groups
#                 curSum += nums[j]
            
#                 res = min(res, max(curSum, dfs(j + 1, m - 1)))
#             dp[i][m] = res
#             return res
        
#         return dfs(0, k)

        

#observation: the minimal is the max element of the entire array, because worst case its one elemnt
#the max is sum of all elements if groups = 1
#so we can do binary search

#and we just check if there exists(is it possible) that mid point (value) can be crraeated

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l = max(nums)
        r = sum(nums)

        def canSplit(largest):
            subarray = 0
            currSum = 0
            for n in nums:
                currSum += n
                if currSum > largest:
                    subarray += 1
                    currSum = n
            #is number of subarrays less than or equal to m

            return subarray + 1 <= k


        res = r

        while l <= r :
            m = l + (r-l)//2
            if canSplit(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        
        return res
