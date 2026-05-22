# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

 

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # dp = [False] * len(nums) 
        # dp[-1] = True

        # for i in range(len(nums)-2,-1,-1):
        #     end = min(len(nums), nums[i] + 1 + i) #this is the min betwen which one can go farthest

        #     for j in range(i+1,end): #we have to do i+1 because infinite loop
        #         if dp[j] == True:
        #             dp[i] = True
        #             break
        # return dp[0]


        goal = len(nums) - 1

        for i in range(len(nums)-1,-1,-1):
            if i + nums[i] >= goal:
                goal = i
        return True if goal == 0 else False