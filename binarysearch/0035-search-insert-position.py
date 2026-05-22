# Given a sorted array of distinct integers and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2



class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        

        l = 0
        r = len(nums) - 1
        
        # This will store the index where target should be inserted
        # if we never find target exactly
        res = 0

        while l <= r:
            
            m = l + (r - l) // 2

            # case 1: mid value is greater than target
            # -> target must be on the LEFT side
            if nums[m] > target:
                r = m - 1

            # case 2: mid value is smaller than target
            # -> target must be on the RIGHT side
            elif nums[m] < target:
                l = m + 1

                # If target is not found,
                # it should be inserted at the current left pointer
                res = l
            #                 At any point in binary search, l is the first index where target could legally go without breaking the sort order.
            # That’s why res = l
            # What does l actually mean?
            # During binary search:
            # Everything left of l is definitely < target
            # Everything right of r is definitely > target
            # The valid insert position is between those two zones
            # So l always points to the earliest safe insertion inde

            else:
                return m

        return res

