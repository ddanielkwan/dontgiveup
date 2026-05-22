# Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array.
#  The result should also be sorted in ascending order.

# An integer a is closer to x than an integer b if:

# |a - x| < |b - x|, or
# |a - x| == |b - x| and a < b
 

# Example 1:

# Input: arr = [1,2,3,4,5], k = 4, x = 3

# Output: [1,2,3,4]


class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        
        l = 0
        r = len(arr) - k #because we cant have r at the very end, we can only have r at most len(arr) - k, because thats where the last window lies

        res = []

        while l < r : #we are comparing against the middle and checking if the difference on outside the window is less than the inner side, then we must move that way
            m = l + (r-l)//2
            #m here represents the left most value in window
            # The leftmost number currently inside the window
        # is farther from x
        # than the next number just outside the window on the right
            if x - arr[m] > arr[m+k] - x : #means the left most value in window has a greater difference than the next value outside of right side
                l = m + 1

            else:
                r = m
        
        res = arr[l:l+k]
        return res

