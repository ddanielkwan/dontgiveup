# You are given an array of integers nums of length n and a positive integer k.

# The power of an array is defined as:

# Its maximum element if all of its elements are consecutive <---
# and sorted in ascending order.
# -1 otherwise.
# You need to find the power of all subarrays of nums of size k.

# Return an integer array results of size n - k + 1, where results[i] is the power of nums[i..(i + k - 1)].

 

# Example 1:

# Input: nums = [1,2,3,4,3,2,5], k = 3

# Output: [3,4,-1,-1,-1]

# Explanation:

# There are 5 subarrays of nums of size 3:

# [1, 2, 3] with the maximum element 3.
# [2, 3, 4] with the maximum element 4.
# [3, 4, 3] whose elements are not consecutive.
# [4, 3, 2] whose elements are not sorted.
# [3, 2, 5] whose elements are not consecutive.


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        #nums 
        # k positive int

        #power is 
        #- max element if all of its elemnts are cosnecutive andsorted in asce
        #-1 else

        #find power of all subarrays of nums of size k

        #what is valid window?
        #valid window is if elements are sorted
        #so new element is > prev by 1 
        #window size is k
        #if thats the case the the power is always the right element in array

        l = 0

        results = []

        for r in range(len(nums)):

            # break in consecutiveness
            if r > 0 and nums[r] - nums[r - 1] != 1:
                l = r

            # keep window size at most k
            if r - l + 1 > k:
                l += 1

            if r - l + 1 == k:
                results.append(nums[r])
            elif r >= k - 1:
                results.append(-1)
        return results