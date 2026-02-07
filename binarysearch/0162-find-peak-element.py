# A peak element is an element that is strictly greater than its neighbors.

# Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

# You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

# You must write an algorithm that runs in O(log n) time.

 

# Example 1:

# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.
# Example 2:

# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.


class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        #find a peak element

        l = 0

        r = len(nums) - 1

        #wouldn't it make sense to always go to the side which is higher and potentially be a peak

        while l <= r :

            m = l + (r-l)//2

            if m + 1 <= r and nums[m+1] > nums[m]:
                l = m + 1
            elif m - 1 >= 0 and nums[m-1] > nums[m]:
                r = m - 1
            else:
                return m
    