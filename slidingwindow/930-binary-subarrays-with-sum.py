# Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

# A subarray is a contiguous part of the array.

 

# Example 1:

# Input: nums = [1,0,1,0,1], goal = 2
# Output: 4
# Explanation: The 4 subarrays are bolded and underlined below:
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# Example 2:

# Input: nums = [0,0,0,0,0], goal = 0
# Output: 15

class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        
        def helper(goal):
            if goal < 0 : return 0

            l = 0
            res = 0
            curr = 0
            #we are calculating the number of subarrsys which are less <= goal
            #and then caclualting unmber of subarrays which are less than or equal to goal - 1
            #and then subtracting it from first one to get all that goal == goal
            #we shrink window when curr is > goal
            #else we are adding number to res r - l + 1 because
            #if you have array [0] theres. 1 subarray, [0,1] theres +2 so 3 subarrys because theres [0,1] and [1] and [0,1,2] is + 3 becuse [0,1][0,1][1,2]
            for r in range(len(nums)):
                curr += nums[r]

                while curr > goal:
                    curr -= nums[l]
                    l += 1
                res += (r-l+1)
            return res
        return helper(goal) - helper(goal-1)
        #limitation is beacuse tehre is 0, adding or subtracting 0 doesnt change sum
