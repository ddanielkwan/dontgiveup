# Given a binary array nums, 
# return the maximum number of consecutive 1's in the array if you can flip at most one 0.

 

# Example 1:

# Input: nums = [1,0,1,1,0]
# Output: 4
# Explanation: 
# - If we flip the first zero, nums becomes [1,1,1,1,0] and we have 4 consecutive ones.
# - If we flip the second zero, nums becomes [1,0,1,1,1] and we have 3 consecutive ones.
# The max number of consecutive ones is 4.
# Example 2:

# Input: nums = [1,0,1,1,0,1]
# Output: 4
# Explanation: 
# - If we flip the first zero, nums becomes [1,1,1,1,0,1] and we have 4 consecutive ones.
# - If we flip the second zero, nums becomes [1,0,1,1,1,1] and we have 4 consecutive ones.
# The max number of consecutive ones is 4.


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        #sliding window

        #[1,0,1,1,0]

        #try to grow your window, window is valid as long as
        #number of zeroes in window <= 1
        #we need to shrink until valid if not valid

        zeroes = 0
        ones = 0

        l = 0
        res = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                zeroes += 1
            else:
                ones += 1
            while zeroes > 1:
                if nums[l] == 0:
                    zeroes -= 1
                   
                else:
                    ones -= 1
                l += 1
            
            res = max(res, r-l+1)
        
        return res 