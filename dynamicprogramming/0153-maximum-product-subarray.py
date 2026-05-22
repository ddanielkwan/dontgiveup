# Given an integer array nums, find a subarray that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.

# Note that the product of an array with a single element is the value of that element.

 

# Example 1:

# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:

# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.



#negatives flip everything
#negative x negative -> positve
#need to track both min and max
#important here is continuous subarray
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = max(nums)

        currentMin = 1
        currentMax = 1
            #can not use the ones before it 
        for n in nums:
            tmp = currentMin 
            currentMin = min(n, n*currentMin, n*currentMax)
            currentMax = max(n, n * tmp, n*currentMax)

            res = max(res,currentMax)
        
        return res

