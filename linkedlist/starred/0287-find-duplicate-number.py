# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and using only constant extra space.

 

# Example 1:

# Input: nums = [1,3,4,2,2]
# Output: 2

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        slow = 0
        fast = 0
        # This does NOT give the duplicate yet
# It only proves "a cycle exists"
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        head = 0
        # because the second loop has no idea where to start unless the first loop puts slow inside the cycle
        # Find the entrance of the cycle

# This only works if slow already sits inside the cycle.
        while True:
            slow = nums[slow]
            head = nums[head]
            if slow == head:
                return slow

