# Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.

 

# Example 1:

# Input: arr = [3,1,2,4]
# Output: 17
# Explanation: 
# Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
# Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
# Sum is 17.
# Example 2:

# Input: arr = [11,81,94,43,3]
# Output: 444


class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:

        #the algorithm here is:
        #1. we keep a mono increasing stack (index, value)
        #2. once we see a smaller next value, we know that the right side of that value in the stack should be larger and the left side to the value should all be larger too
        #3. to find all subarrays with current value as min, we get all subarrays to left and to right of it
        #left x right
        
        # Modulo required by the problem to avoid overflow
        MOD = 10 ** 9 + 7

        # This will store the final sum of minimums
        res = 0

        # Monotonic increasing stack
        # Each element is (index, value)
        stack = []

        # We iterate through the array left -> right
        for i, n in enumerate(arr):

            # While the current number is smaller than the stack top,
            # the stack top can NO LONGER extend to the right
            while stack and n < stack[-1][1]:

                # Pop the element whose minimum range is now fixed
                j, m = stack.pop()

                # LEFT count:
                # If stack is not empty, distance to previous smaller element
                # If stack is empty, it can extend all the way to index 0
                left = j - stack[-1][0] if stack else j + 1

                # RIGHT count:
                # Distance to the current index (first smaller on right)
                right = i - j

                # Contribution of m as minimum
                res = (res + m * left * right) % MOD

            # Push current element with its index
            stack.append((i, n))

        # After processing all elements,
        # remaining stack elements extend to the END of the array
        while stack:
            j, m = stack.pop()

            # LEFT boundary same logic as before
            left = j - stack[-1][0] if stack else j + 1

            # RIGHT boundary is the end of array
            right = len(arr) - j

            # Final contribution
            res = (res + m * left * right) % MOD

        return res
