# Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

# You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

 

# Example 1:

# Input: nums = [1,2,0]
# Output: 3
# Explanation: The numbers in the range [1,2] are all in the array.
# Example 2:

# Input: nums = [3,4,-1,1]
# Output: 2
# Explanation: 1 is in the array but 2 is missing.

class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:

        # n = len(nums) #0 - n elements [0,n] 
        # seen = [False] * n 

        # for number in nums:
        #     if number > 0 and number <= n: #if positive and inside the range set seen as true
        #         seen[number - 1] = True
        
        # for num in range(1, n+1):
        #     if not seen[num - 1]:
        #         return num

        # return n + 1

        #second approach: trick - Use the array itself as a “seen” map by marking indices negative.

        #Step 1: Clean the array (replace negatives with 0)
        # We’re going to use the sign of nums[index] to mean “seen”.
        # Negative -> seen
        # Non-negative -> not seen yet
        # But negatives already in the input would mess up the meaning, so we normalize them to 0.
        # After this step, every value is >= 0.
        for i in range(len(nums)):
            if nums[i] < 0 :
                nums[i] = 0
        
        #Step 2: Mark numbers that exist by flipping signs at their “home index”
        #If a value val exists in the array (and 1 <= val <= n), then we mark: val - 1 as negative
        for i in range(len(nums)):
            val = abs(nums[i])
            if 1 <= val <= len(nums):
                index = val - 1
                if nums[index] > 0:
                    nums[index] = -1 * nums[index]

                elif nums[index] == 0:
                    nums[index] = -1 * (len(nums) + 1)

        #Step 3: Find the first index that wasn’t marked
        for i in range(1,len(nums)+1):
            if nums[i-1] >= 0:
                return i
        
        return len(nums) + 1 
        
    