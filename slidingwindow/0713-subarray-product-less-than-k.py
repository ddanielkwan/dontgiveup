# Given an array of integers nums and an integer k,
#  return the number of contiguous subarrays where the product of all the elements 
# in the subarray is strictly less than k.

 

# Example 1:

# Input: nums = [10,5,2,6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are:
# [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
# Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
# Example 2:

# Input: nums = [1,2,3], k = 0
# Output: 0


class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        
        
        currentProduct = 1

        l = 0 

        res = 0
        for r in range(len(nums)):
            currentProduct *= nums[r]

            while l <= r and currentProduct >= k : #since [1,2,3] and k can be 0 ,keeps going l +=1 
                currentProduct //= nums[l]
                l += 1
            
            res += r - l + 1
            #because if [1,2,3,4] product = 100
            #if 1, then we have 1, if [1,2] then we have [1] and [2] and [1,2]
            #[1,2,3] = [1,2][2,3][1,3]
        
        return res
    

