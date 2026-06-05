# Given an integer array arr, partition the array into (contiguous) subarrays of length at most k.
#  After partitioning, each subarray has their values changed to become the maximum value of that subarray.

# Return the largest sum of the given array after partitioning. Test cases are generated so that the answer fits in a 32-bit integer.

 

# Example 1:

# Input: arr = [1,15,7,9,2,5,10], k = 3
# Output: 84
# Explanation: arr becomes [15,15,15,9,10,10,10]
# Example 2:

# Input: arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
# Output: 83
# Example 3:

# Input: arr = [1], k = 1
# Output: 1


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        

        #dynamic programming
        #why?
        #every elemnet becomes the max of that group
        #and we wnat to maximize the currnet k window

        #REALIZATION: have a for loop in the dfs dp

        # o(nxk)
        #space o(n)
        cache = {}
        def dfs(i):
            if i >= len(arr):
                return 0
            if i in cache:
                return cache[i]
            cache[i] = 0
            currmax = 0
            #so we are nont out of bounds
            for j in range(i, min(i+k, len(arr))):
                currmax = max(currmax, arr[j])
                windowsize = j - i + 1

                cache[i] = max(cache[i], currmax * windowsize + dfs(j+1))
            
            return cache[i]
        return dfs(0)
                


#tabulation
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            cur_max = 0
            for j in range(i, min(n, i + k)):
                cur_max = max(cur_max, arr[j])
                window_size = j - i + 1
                dp[i] = max(dp[i], dp[j + 1] + cur_max * window_size)

        return dp[0]