# You are given a 0-indexed integer array nums and an integer p. Find p pairs of indices of nums such that the maximum difference amongst all the pairs is minimized. Also, ensure no index appears more than once amongst the p pairs.

# Note that for a pair of elements at the index i and j, the difference of this pair is |nums[i] - nums[j]|, where |x| represents the absolute value of x.

# Return the minimum maximum difference among all p pairs. We define the maximum of an empty set to be zero.

 

# Example 1:

# Input: nums = [10,1,2,7,1,3], p = 2
# Output: 1
# Explanation: The first pair is formed from the indices 1 and 4, and the second pair is formed from the indices 2 and 5. 
# The maximum difference is max(|nums[1] - nums[4]|, |nums[2] - nums[5]|) = max(0, 1) = 1. Therefore, we return 1.


# "Can I pick p pairs where every single pair has difference ≤ mid?"

# If yes → your maximum difference is at most mid
# If no → you need a bigger mid
# So you're shrinking mid as much as possible, while still being able to form p valid pairs.

class Solution:
    def minimizeMax(self, nums: list[int], p: int) -> int:
        #keep guessing the differences
        #maximum difference is minimized, means largest - smallest is maximum difference

        #we are trying to find all the minimal difference pairs p, so it makes sense that we would subtract the ones adjacent, since it is sorted,
        #we aredoing binary search to find the smallest possible amount of pairs
        def validPairs(threshold):
            count = 0
            i = 0
            while i < len(nums) - 1:
                if nums[i+1] - nums[i] <= threshold:
                    count += 1
                    i += 2
                    if count == p:
                        return True
                else:
                    i += 1
            return False

        nums.sort()

        l = 0
        r = 10 ** 9

        res = 0
        while l <= r :
            m = l + (r-l)//2

            if validPairs(m): #m here is minimized, max difference
                r = m - 1
                res = m
            else:
                l = m + 1
        return res
