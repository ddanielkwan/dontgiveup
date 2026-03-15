# You are given an array of integers nums, 
# there is a sliding window of size k which 
# is moving from the very left of the array to the very right.
#  You can only see the k numbers in the window. 
# Each time the sliding window moves right by one position.

# Return the max sliding window.

 

# Example 1:

# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7



from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        # #brute force

        # res = []
        # for i in range(len(nums) - k + 1):
        #     res.append(max(nums[i:i+k]))
        
        # return res

        #intuition:  #[1,1,1,1,4,5,6]x
        #the largest will alwys be on q[0]
        #to keep track of all 1s is irrevelant because they will never be max if k = 5
        #so we removed it
        #keep a decreasing q
        q = deque() #stores the index because we need to compare the indices with l and r pointer

        maximums = []

        l = 0
        r = 0

        while r < len(nums):

            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            q.append(r) #index

            if l > q[0]: #
                q.popleft() #this is why we use q and not stack we need pop for window

            if (r-l+1) == k:
                maximums.append(nums[q[0]]) #largest is first
                l += 1
            
            r += 1
        
        return maximums
    
