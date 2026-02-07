# You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

# You are given an integer array nums representing the data status of this set after the error.

# Find the number that occurs twice and the number that is missing and return them in the form of an array.

from collections import Counter


class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        #0 count is missing 2 is duplicate

        
        tracker = Counter(nums)
        res = [0,0]
        for i in range(1, len(nums)+1):
            if tracker[i] == 0:
                res[1] = i
            if tracker[i] == 2:
                res[0] = i
        return res