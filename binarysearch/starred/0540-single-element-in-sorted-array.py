# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

# Return the single element that appears only once.

# Your solution must run in O(log n) time and O(1) space.

 

# Example 1:

# Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2
# Example 2:

# Input: nums = [3,3,7,7,10,11,11]
# Output: 10


class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        
        l = 0

        r = len(nums) - 1

        #intuition: if every element appears twice, there should be a pattern to how we split
        #we want to search on the side that has odd count because even + 1
    
        while l <= r :

            m = l + (r-l)//2

            if m + 1 <= r and nums[m+1] == nums[m]:
                if (r - m + 1) % 2 != 0: #count the range 
                    l = m + 1 + 1
                else:
                    r = m - 1
            
            elif m - 1 >= 0 and nums[m-1] == nums[m]:
                if (m - l + 1) % 2 != 0:
                    r = m - 1 -1
                else:
                    l = m + 1
            
            else:
                return nums[m]
        
        return -1


