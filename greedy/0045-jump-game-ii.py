# You are given a 0-indexed array of integers nums of length n. You are initially positioned at index 0.

# Each element nums[i] represents the maximum length of a forward jump from index i. 
# In other words, if you are at index i, you can jump to any index (i + j) where:

# 0 <= j <= nums[i] and
# i + j < n
# Return the minimum number of jumps to reach index n - 1. The test cases are generated such that you can reach index n - 1.

 

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [2,3,0,1,4]
# Output: 2

class Solution:
    def jump(self, nums: List[int]) -> int:
        #this is so cool
        #think about 2,3,1,1,4
        #if we start at 2 thats the first section
        #where can index 0 jump to? [3 and 1]
        #thats teh second section
        #where can each 3 and 1 jump to? [1,4] thats third section
        #we want t ofind windows like bfs and get the farthest for each window

        
        l = 0
        r = 0
        #greedy
        farthest = 0
        res = 0


        # [2, 3, 1, 1, 4]
        #first iteration [2] you can either jump any of [3,1]
        #pick the largest
        #so far can now jump to [1,4]

        #these arelevels
        # [2, 3, 1, 1, 4]
        #. lr

        #[2, 3, 1, 1 , 4]
        #.   l. r

        # [2, 3 , 1 ,1 ,4]
        #.          l   r
        # l is r + 1 ,so otuside of current window
        while r < len(nums) - 1 :

            for i in range(l,r+1):
                farthest = max(farthest, nums[i] + i)
            
            l = r + 1
            r = farthest 
            res += 1
        return res 

