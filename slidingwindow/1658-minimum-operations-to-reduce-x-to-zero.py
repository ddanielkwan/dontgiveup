# You are given an integer array nums and an integer x. 
# In one operation, you can either remove the leftmost or the rightmost element from
#  the array nums and subtract its value from x. Note that this modifies the array for future operations.

# Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.

 

# Example 1:

# Input: nums = [1,1,4,2,3], x = 5
# Output: 2
# Explanation: The optimal solution is to remove the last two elements to reduce x to zero.
# Example 2:

# Input: nums = [5,6,7,8,9], x = 4
# Output: -1


class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        
        #remove left most or right most element
        #intuition: basically find the inner window that equals totalsum - extracted left and right
        #the target will be totalsum - x
        #we want to maximize this window

        totalSum = sum(nums)
        target = totalSum - x 
    
        l = 0

        currentSum = 0

        windowSize = -1

        for r in range(len(nums)):
            currentSum += nums[r]

            while l <= r and currentSum > target:
                currentSum -= nums[l]
                l += 1
            
            if currentSum == target:
                windowSize = max(windowSize, r - l + 1)
            

        return -1 if windowSize == -1 else len(nums) - windowSize

