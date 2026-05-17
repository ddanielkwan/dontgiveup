# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        #sorted

        #find starting and ending position of target number

        #binary search and then increment left and right? cant because nums = [2,2,2,2,2,2,2] may be o(n)


        # use two binary searches:
# 1) find the leftmost index where nums[i] == target
# 2) find the rightmost index where nums[i] == target

        left = self.binarySearch(nums, target, True)
        right = self.binarySearch(nums, target, False)
        return [left,right]

    def binarySearch(self, nums, target, leftBias):
        l = 0
        r = len(nums) - 1

        i = - 1

        while l <= r :
            m = (l+r)//2

            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                i = m
                if leftBias:
                    r = m - 1 #left bias means we want to find the smallest index that is equal to target
                else:
                    #right bias means, right most index that is also target
                    l = m + 1
        
        return i

