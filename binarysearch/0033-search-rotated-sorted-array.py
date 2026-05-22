# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length)
#  such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
# For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        
        #its sorted

        l = 0 
        r = len(nums) - 1

        while l <= r :

            m = l + (r-l)//2 

            if nums[m] == target: #best case we find it 
                return m
            #four cases

            if nums[l] <= nums[m]:  #[4,5,6,7,0,1,2]
                if nums[l] <= target < nums[m]: #is the target within the left side?
                    r = m - 1
                else: #then it must be on the right side
                    l = m + 1
            else: #[7,0,1,2,3,4,5,6] nums[l] > nums[m] m is index 4 = 3
                if nums[m] < target <= nums[r]: #is 0 in right side? go right
                    l = m + 1
                else: #go left
                    r = m - 1
        return - 1




