# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

class Solution:
    def majorityElement(self, nums: list[int]) -> int:

        #we can do this two ways
        #1. use a hashmap to store the number of times we saw an element, we know its majority if its greater than half (n/2)

        # hashmap = defaultdict(int)

        # for n in nums:
        #     hashmap[n] += 1 
        #     if hashmap[n] >  len(nums)/ 2:
        #         return n

        #2. cooler method, rather than hashmap, store count and element, every time we see not that element, minus one from count
        #if count == 0 , the set that element as the element we track
        count = 0
        res = 0

        for n in nums:
            if count == 0:
                res = n 

            count += 1 if n == res else -1
        return res

