# Given an array of positive integers nums and a positive integer target,
#  return the minimal length of a subarray whose sum is greater than or equal to target.
#  If there is no such subarray, return 0 instead.

 

# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        

        minSize = float("inf")

        l = 0

        currSum = 0

        for r in range(len(nums)):

            currSum += nums[r]

            while currSum >= target:
                minSize = min(minSize, r - l + 1)
                
                currSum -= nums[l]
                l += 1
            
        
        return minSize if minSize != float('inf') else 0

