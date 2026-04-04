# Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

 

# Example 1:

# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# Example 2:

# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.
 
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #If total sum is odd → immediately return False. You can never split odd number equally.
        #You don't actually need to find BOTH subsets. Just ask:
        # an I find ANY subset that sums to exactly total/2

        total = sum(nums)

        if total % 2 != 0:
            return False
        #first step jsut do without cache
        #second step we see the key is index and target
        cache = {}
        def solve(index, target):
            if target == 0:
                return True
            if target < 0 or index == len(nums):
                return False
            
            if index in cache:
                if target in cache[index]:
                    return cache[index][target]

            else:
                cache[index] = {}
            cache[index][target] = solve(index+1, target - nums[index]) or solve(index+1, target) 
            
            return cache[index][target]

        
        return solve(0, total // 2)