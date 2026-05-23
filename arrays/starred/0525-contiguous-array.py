# Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

 

# Example 1:

# Input: nums = [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
# Example 2:

# Input: nums = [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        #intuitoon here
        #keep track of when we see excess ones
        #e.g [1,1,1, 0,0]
        #start at i = 0, we see 1:1 so thats hashmap[excess=1] = starts at 0 index

        zeroes = 0
        ones = 0
        res = 0
        excessMap = {}
        for i, n in enumerate(nums):
            if n == 1 :
                ones += 1
            else:
                zeroes += 1
            
            #we only want to add it once because its on left side
            # Because we want the LONGEST possible subarray and to maximize length, we want the EARLIEST occurrence of an excess
            if ones - zeroes not in excessMap:
                excessMap[ones-zeroes] = i
            
            if ones == zeroes:
                res  = ones + zeroes
            else:
                firstIndex = excessMap[ones-zeroes]
                res = max(res, i - firstIndex)
        
        return res