# You are given an integer array nums.
#  In one operation, you can replace any element in nums with any integer.

# nums is considered continuous if both of the following conditions are fulfilled:

# All elements in nums are unique.
# The difference between the maximum element and the minimum element in nums equals nums.length - 1.
# For example, nums = [4, 2, 5, 3] is continuous, but nums = [1, 2, 3, 5, 6] is not continuous.

# Return the minimum number of operations to make nums continuous.

 

# Example 1:

# Input: nums = [4,2,5,3]
# Output: 0
# Explanation: nums is already continuous.
# Example 2:

# Input: nums = [1,2,3,5,6]
# Output: 1
# Explanation: One possible solution is to change the last element to 4.
# The resulting array is [1,2,3,5,4], which is continuous.

class Solution:
    def minOperations(self, nums: list[int]) -> int:
        #brute force how about we sort and then we go through all possible elements and check if it lies between [i, i  +n ]
        #brute force, we know that [x, x + n - 1] because thats the difference
        #so [1,2,3,4,5,6] we are trying at every elemnet, can that be x?
        #and does it include every element within [2,7] etc.. and find min that needs change
        # return res
        # N = len(nums)
        # nums.sort()

        # res = float('inf')

        # for i in range(len(nums)):
        #     noChange = 1
        #     for j in range(i + 1, N):
        #         if nums[i] < nums[j] < nums[i] + N:
        #             noChange += 1
            
        #     res = min(res, len(nums) - noChange)
        
        # return res

        #imagine
        #[1, 2, 3, 5, 6]
        #we have sliding window l and r 
        #were going to move the left pointer(different from how we usually do it)
        #and were going to keep moving right pointer until it sout of bounds
        #the bounds for any left ptr is 
        #nums[l] to nums[l] + length - 1
        #we determine size of window, and assume that everythinginside window is valid 
        #so essentially we are missing length - window elements

        length = len(nums)
        res = length

        r = 0 #different from how we normally do it

        nums = sorted(set(nums))#note if we have duplicate 1, 2, 2, 3 , then we are assumming 2 and 2 are valid but only 1 is valid so it messes up our siwndow size

        for l in range(len(nums)):
            while r < len(nums) and nums[r] - nums[l] < length:
                r += 1 #keep adjusting until were outside
            
            windowSize = r - l
            res = min(res, length - windowSize)
        
        return res

