# you are given an integer array nums and an integer k. You can partition the array into at most k non-empty adjacent subarrays. 
# The score of a partition is the sum of the averages of each subarray.

# Note that the partition must use every integer in nums, and that the score is not necessarily an integer.

# Return the maximum score you can achieve of all the possible partitions. Answers within 10-6 of the actual answer will be accepted.

 

# Example 1:

# Input: nums = [9,1,2,3,9], k = 3
# Output: 20.00000
# Explanation: 
# The best choice is to partition nums into [9], [1, 2, 3], [9]. The answer is 9 + (1 + 2 + 3) / 3 + 9 = 20.
# We could have also partitioned nums into [9, 1], [2], [3, 9], for example.
# That partition would lead to a score of 5 + 2 + 6 = 13, which is worse.
# Example 2:

# Input: nums = [1,2,3,4,5,6,7], k = 4
# Output: 20.50000



class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        
        #top down

        #dp
        #state is index and groups left

       
        cache = {}
        def dfs(index, groupsLeft):
            if groupsLeft == 1: #we have oen group left to make 
                return sum(nums[index:]) / (len(nums) - index)
            if (index,groupsLeft) in cache:
                return cache[(index,groupsLeft)]
            
            cache[(index,groupsLeft)] = 0
            currentSum =0 #to help do calcualtion
            for j in range(index, len(nums) - groupsLeft + 1): #
            #so we jhave enoguh elements for remaining groups

                currentSum += nums[j]

                cache[(index,groupsLeft)] = max(cache[(index,groupsLeft)], currentSum/(j-index+1) + dfs(j+1, groupsLeft - 1))
            return cache[(index,groupsLeft)]
        
        return dfs(0,k)
