# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

 

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.


#DETERMINE what is a sequence and a hashset
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        #what is a sequence? a sequence means the numbers come consecutively , 1 , 2 , 3 
        #how do we know what is a beginning of a sequence?
        #  if the element - 1 is not in the nums, then we can start tracking

        longestConsecutiveElements = 0

        nums = set(nums)

        for number in nums:
            if number - 1 not in nums:
                sequenceNumber = number
                total = 0
                while sequenceNumber in nums:
                    total += 1
                    sequenceNumber += 1
                
                longestConsecutiveElements = max(total,longestConsecutiveElements)
        return longestConsecutiveElements
        

