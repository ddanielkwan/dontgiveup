# Given an integer array nums and an integer k, return the number of good subarrays of nums.

# A good array is an array where the number of different integers in that array is exactly k.

# For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
# A subarray is a contiguous part of an array.

 

# Example 1:

# Input: nums = [1,2,1,2,3], k = 2
# Output: 7
# Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]

from collections import defaultdict


class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:

        def countAtMostKDistinct(nums, k):
            l = 0
            res = 0

            count = defaultdict(int)
            for r in range(len(nums)):
                count[nums[r]] += 1

                while len(count) > k :
                    count[nums[l]] -= 1
                    if count[nums[l]] == 0:
                        del count[nums[l]]
                    l += 1
                
                res += (r-l+1)
            
            return res
        
        return countAtMostKDistinct(nums,k) - countAtMostKDistinct(nums, k - 1)