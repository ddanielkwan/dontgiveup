# A ramp in an integer array nums is a pair (i, j) for which i < j and nums[i] <= nums[j]. The width of such a ramp is j - i.

# Given an integer array nums, return the maximum width of a ramp in nums. If there is no ramp in nums, return 0.

 

# Example 1:

# Input: nums = [6,0,8,2,1,5]
# Output: 4
# Explanation: The maximum width ramp is achieved at (i, j) = (1, 5): nums[1] = 0 and nums[5] = 5.
# Example 2:

# Input: nums = [9,8,1,0,1,9,4,0,4,1]
# Output: 7
# Explanation: The maximum width ramp is achieved at (i, j) = (2, 9): nums[2] = 1 and nums[9] = 1.

class Solution:
    def maxWidthRamp(self, nums: list[int]) -> int:
        
        # build a monotonic decreasing stack of indices
        # stores left indices, stores all the possible starting ramp
        stack = []

        for i in range(len(nums)):
            # Only push index if it creates a new minimum
            # If nums[i] is >= last stack value, it is useless
            # because earlier index is smaller and further left
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)

        # 2. traverse from the right to find farthest valid j
        maxRampWidth = 0

        for j in range(len(nums) - 1, -1, -1):
            
            # While we can form a valid ramp
            # nums[i] <= nums[j] ensures ramp condition
            while stack and nums[stack[-1]] <= nums[j]:
                
                i = stack.pop()  # left index
                maxRampWidth = max(maxRampWidth, j - i)

                # Once popped, this i will never form a wider ramp
                # because future j will only move left

        return maxRampWidth

