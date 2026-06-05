# Given an array of n integers nums,
#  a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

# Return true if there is a 132 pattern in nums, otherwise, return false.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: false
# Explanation: There is no 132 pattern in the sequence.
# Example 2:

# Input: nums = [3,1,4,2]
# Output: true
# Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
# Example 3:

# Input: nums = [-1,3,2,0]
# Output: true
# Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].



class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        #keep a monodecreasing stack
        #easy hint: what we if just keep track of the most minimal value? because we know that nums[i] must be the smallest of the three?

        #store val, currentSeenMinimum

        stack = [] #(val, currentSeenMinimum)

        currentSeenMinimum = nums[0]

        for number in nums:
            #if prev value is less than current number lets pop, to ensure decreasing stack
            while stack and stack[-1][0] < number:
                stack.pop()
            
            if stack and stack[-1][1] < number and number < stack[-1][0]:
                return True
            
            stack.append((number, currentSeenMinimum))
            currentSeenMinimum = min(currentSeenMinimum, number) #update minimum
        
        return False



