# The frequency of an element is the number of times it occurs in an array.

# You are given an integer array nums and an integer k. In one operation, you can choose an index of nums and increment the element at that index by 1.

# Return the maximum possible frequency of an element after performing at most k operations.

 

# Example 1:

# Input: nums = [1,2,4], k = 5
# Output: 3
# Explanation: Increment the first element three times and the second element two times to make nums = [4,4,4].
# 4 has a frequency of 3.
# Example 2:

# Input: nums = [1,4,8,13], k = 5
# Output: 2
# Explanation: There are multiple optimal solutions:
# - Increment the first element three times to make nums = [4,4,8,13]. 4 has a frequency of 2.
# - Increment the second element four times to make nums = [1,8,8,13]. 8 has a frequency of 2.
# - Increment the third element five times to make nums = [1,4,13,13]. 13 has a frequency of 2.


class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        
        #intuition, window size should be sum(window) + k, beacuse 
        #if window is [1,3,3] and k = 1, since we are incrementing, the highest sum we can go is [2, 3, 3] = 8 so the size is 8, not possible if [3,3,3], we will need a running sum variable

        l = 0

        maxPossibleFrequency = 0

        runningSum = 0

        nums.sort() #why do we need to sort , because formula is window*largest <- nums[r]


        for r in range(len(nums)):

            runningSum += nums[r]

            while (r-l+1) * nums[r] > runningSum + k :

                runningSum -= nums[l]
                l += 1
            
            maxPossibleFrequency = max(maxPossibleFrequency, r-l+1)
        
        return maxPossibleFrequency



