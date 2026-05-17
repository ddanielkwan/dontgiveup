# You are given a 0-indexed integer array nums. You have to partition the array into one or more contiguous subarrays.

# We call a partition of the array valid if each of the obtained subarrays satisfies one of the following conditions:

# The subarray consists of exactly 2, equal elements. For example, the subarray [2,2] is good.
# The subarray consists of exactly 3, equal elements. For example, the subarray [4,4,4] is good.
# The subarray consists of exactly 3 consecutive increasing elements, that is, the difference between adjacent elements is 1. For example, the subarray [3,4,5] is good, but the subarray [1,3,5] is not.
# Return true if the array has at least one valid partition. Otherwise, return false.

 

# Example 1:

# Input: nums = [4,4,4,5,6]
# Output: true
# Explanation: The array can be partitioned into the subarrays [4,4] and [4,5,6].
# This partition is valid, so we return true.
# Example 2:

# Input: nums = [1,1,1,2]
# Output: false
# Explanation: There is no valid partition for this array.



#At every index, you only have 3 valid moves you can make:1. Take 2 equal numbers        [2, 2]
# 2. Take 3 equal numbers        [3, 3, 3]
# 3. Take 3 consecutive numbers  [3, 4, 5]That's it. If none of those work, it's invalid.
class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        
        cache = {}
        #brute force all combo then cache
        def dfs(i):
            if i == len(nums):
                return True
            
            if i in cache:
                return cache[i]
            
            res = False
            if i < len(nums) - 1 and nums[i] == nums[i+1]: #case 1 two are equal
                res = dfs(i + 2)

            if i < len(nums) - 2 and nums[i] == nums[i+1] == nums[i+2]:
                res = res or dfs(i+3)
            
            if i < len(nums) - 2 and nums[i] + 1 == nums[i+1] == nums[i+2] - 1:
                res = res or dfs(i+3)
            
            cache[i] = res
            return res
        return dfs(0)

