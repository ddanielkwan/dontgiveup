# Given an array nums of n integers, 
# return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        
        # fix two numbers, then use two pointers to find the remaining two numbers that complete the target sum

        nums.sort()

        fourSums = []
        doubles = []

        def kSum(k, start, target):
            #base case
            if k == 2:
                l = start
                r = len(nums) - 1

                while l < r :
                    if nums[l] + nums[r] < target:
                        l += 1

                    elif nums[r] + nums[l] > target:
                        r -= 1
                    
                    else:
                        #equals to target
                        fourSums.append(doubles + [nums[l], nums[r]])
                        l += 1
                        r -= 1
                        
                        #want to check if the current left element is same as previous, since we already added, just move pointer
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        
                        #same thing for the right side
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1

                return
            

            #else k > 2 
            for i in range(start, len(nums) - k + 1):
                #this loop goes to len(nums) - k because if k is 4, we want the end to have at least 3 more elements, to be picked
                if i > start and nums[i] == nums[i - 1]:
                    continue
                
                doubles.append(nums[i])
                kSum(k-1, i + 1, target - nums[i])
                doubles.pop()
            return
        
        kSum(4, 0, target)
        return fourSums

