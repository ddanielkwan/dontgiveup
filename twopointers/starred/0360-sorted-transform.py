# Given a sorted integer array nums and three integers a, b and c, apply a quadratic function of the form f(x) = ax2 + bx + c to each element nums[i] in the array, and return the array in a sorted order.

 

# Example 1:

# Input: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
# Output: [3,9,15,33]
# Example 2:

# Input: nums = [-4,-2,2,4], a = -1, b = 3, c = 5
# Output: [-23,-5,1,7]

class Solution:
    def sortTransformedArray(self, nums, a, b, c):

        def f(x):
            return a*x*x + b*x + c
            #undersatnd parabola
            #a > 0 means right side
            #a < 0 means left side negative
        n = len(nums)

        res = [0] * n

        left = 0
        right = n - 1

        # where to fill
        idx = n - 1 if a >= 0 else 0

        while left <= right:

            left_val = f(nums[left])
            right_val = f(nums[right])

            if a >= 0:

                # bigger goes at back
                if left_val > right_val:
                    res[idx] = left_val
                    left += 1
                else:
                    res[idx] = right_val
                    right -= 1

                idx -= 1

            else:

                # smaller goes at front
                if left_val < right_val:
                    res[idx] = left_val
                    left += 1
                else:
                    res[idx] = right_val
                    right -= 1

                idx += 1

        return res