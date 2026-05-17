# Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

# Return the number of nice sub-arrays.

 

# Example 1:

# Input: nums = [1,1,2,1,1], k = 3
# Output: 2
# Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].


class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        #3 ptr sliding window
        #we have to have 3 pointers and not two because
        #e.g 

        currentOdds = 0
        #we have a widnow
        # [2,2,1,1,2,1,]
        #.     ^

        # we want to be able to increase m pointer to first odd and then get difference of m - l
        # 

        l = 0 #were going to have l and m at same place initially once we find odds == k, then we can adjust m as much as possible
        m = 0
        numberOfNiceArrays = 0

        for r in range(len(nums)):
            if nums[r] % 2 != 0:
                currentOdds += 1
            
            while currentOdds > k:
                if nums[l] % 2 != 0:
                    currentOdds -= 1
                
                l += 1
                m = l
            
            if currentOdds == k:
                while not nums[m] % 2: #not odd
                    m += 1
                
                numberOfNiceArrays += (m-l) + 1
                
        return numberOfNiceArrays

