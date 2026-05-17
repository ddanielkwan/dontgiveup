# Given an array of integers nums, calculate the pivot index of this array.

# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

# Return the leftmost pivot index. If no such index exists, return -1.

#RUNNING TOTAL
class Solution:
    def pivotIndex(self, nums: list[int]) -> int:

        #find index where left and right sums of this index is same

        #use kind of a sliding sum approach
        #if we know the total sum, then the right sum is just sum - left sum - current element
        #and then check if leftsum == rightsum

        leftSum = 0

        totalSum = sum(nums) #o(n)

        for index, value, in enumerate(nums):
            rightSum = totalSum - leftSum - nums[index]

            if rightSum == leftSum:
                return index
        
            leftSum += nums[index]
        return -1
        

