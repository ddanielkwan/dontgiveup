# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

from collections import defaultdict


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        res = 0
        currentSum = 0
        #we cant use a sliding window because it can have negative numbers, so it will ruin the add calculation
        prefixCount = defaultdict(int)
        prefixCount[0] = 1

        #we can store the cumulative sum, and then use that to subtract k from it
        #that means, e.g 10 - k = 6, do we have a array in prefixCount hashmap, that has 6 as the key and how many
        #so we store th e sum : count 

        for number in nums:
            currentSum += number 
            diff = currentSum - k #what is the sum we need in order to to make it work
            if diff in prefixCount:
                res += prefixCount[diff]
            prefixCount[currentSum] += 1
        return res

