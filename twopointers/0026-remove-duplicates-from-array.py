# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

# Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.

# The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        
        #have two pointers and do a check to compare the second pointer element to left pointer and if not equals
        #then increase and then set 
        l = 0

        for r in range(1, len(nums)):
            if nums[r] != nums[l]:
                l += 1
                nums[l] = nums[r]
        
        return l + 1