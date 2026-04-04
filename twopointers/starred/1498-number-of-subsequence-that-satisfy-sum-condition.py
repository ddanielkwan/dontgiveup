# You are given an array of integers nums and an integer target.

# Return the number of non-empty subsequences of nums such that the sum of the minimum and 
# maximum element on it is less or equal to target. 
# Since the answer may be too large, return it modulo 109 + 7.


class Solution:
    def numSubseq(self, nums: list[int], target: int) -> int:
        #brute force is backtracking, do we include it or not
        # MOD = 10**9 + 7
        # cache = {}
        # def dfs(i, currmax, currmin):
        #     if (i,currmax,currmin) in cache:
        #         return cache[(i,currmax,currmin)]

        #     if i == len(nums):
        #         if currmax + currmin <= target:
        #             return 1 
        #         else: 
        #             return 0

        #     skip = dfs(i+1, currmax, currmin)
        #     include = dfs(i+1, max(currmax,nums[i]), min(currmin,nums[i]))
        #     cache[(i,currmax,currmin)] = (skip + include) % MOD
        #     return cache[(i,currmax,currmin)]

        # return dfs(0, float('-inf'), float('inf'))
    
        
        MOD = 10**9 + 7
        nums.sort()
        #binary search
        #we sort the input
        #3,3,5,6,8
        #for each element, how many elemnts to right can be added
        #we have to add 2^(r-left+1)  #because each in between can be in or out

        #why
        r = len(nums) - 1
        l = 0
        res = 0
        #because we only care about the minimum(left value) and the maximum(right value) 
        #min(subsequence) + max(subsequence) ≤ target
        #similar to greedy, move right pointer if too big
        for left_index, left_val in enumerate(nums):
            while (left_val+ nums[r]) > target and left_index <= r:
                r -= 1
            
            if left_index <= r:
                res += (2**(r-left_index))  #because each in between can be in or out
                res %= MOD

                #mainly math and two pointer
        return res