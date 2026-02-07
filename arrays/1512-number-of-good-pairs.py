# Given an array of integers nums, return the number of good pairs.

# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

 

# Example 1:

# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.


from collections import defaultdict


class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        


        pairs = 0
        hashmap = defaultdict(int)

        #if you have 1 item > 1 count
        #if you see another 1 that means you can make +1 pair (1,1) now that 1 count is 2
        #if you see another 1, previous you alreay had (1,1) now since count is 2 you can do 2 addition pairs because a x (pair1) a x (pair2)
        
        for n in nums:
            if n in hashmap: #only for that element like 1s only
                pairs += hashmap[n]

            hashmap[n] += 1
            #like a sum

        return pairs