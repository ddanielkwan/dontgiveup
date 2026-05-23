# Given an array of n integers nums and an integer target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

 

# Example 1:

# Input: nums = [-2,0,1,3], target = 2
# Output: 2
# Explanation: Because there are two triplets which sums are less than 2:
# [-2,0,1]
# [-2,0,3]
# Example 2:

# Input: nums = [], target = 0
# Output: 0
# Example 3:

# Input: nums = [0], target = 0
# Output: 0


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        
        nums.sort()

        #fix the index then use two pointesr
        numberOfTriplets = 0
        for i in range(len(nums)-2):
            

            low = i + 1
            high = len(nums) - 1
            while low < high:

                if nums[i] + nums[low] + nums[high] >= target:
                    high -= 1
                else:
                    #[-2,0,1,3], target = 2
                    # [-2,0,1] 
                    # [-2,0,3]
                    numberOfTriplets += high - low
                    low += 1
        
        return numberOfTriplets