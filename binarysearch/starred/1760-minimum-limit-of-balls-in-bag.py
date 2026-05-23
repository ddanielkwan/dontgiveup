# You are given an integer array nums where the ith bag contains nums[i] balls. You are also given an integer maxOperations.

# You can perform the following operation at most maxOperations times:

# Take any bag of balls and divide it into two new bags with a positive number of balls.
# For example, a bag of 5 balls can become two new bags of 1 and 4 balls, or two new bags of 2 and 3 balls.
# Your penalty is the maximum number of balls in a bag. You want to minimize your penalty after the operations.

# Return the minimum possible penalty after performing the operations.

 

# Example 1:

# Input: nums = [9], maxOperations = 2
# Output: 3
# Explanation: 
# - Divide the bag with 9 balls into two bags of sizes 6 and 3. [9] -> [6,3].
# - Divide the bag with 6 balls into two bags of sizes 3 and 3. [6,3] -> [3,3,3].
# The bag with the most number of balls has 3 balls, so your penalty is 3 and you should return 3.


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        
        def canDivide(threshold):
         #9 / 3 = 3 3 3
            #9/ 4 = 4 4 1
            operations = 0

            for num in nums:

                operations += math.ceil(num / threshold) - 1

            return operations <= maxOperations


        l = 1
        r = max(nums)
        res = 0
        while l <=r :
            threshold = l + (r-l)//2

            if canDivide(threshold):
                res = threshold
                r = threshold - 1
            else:
                l = threshold + 1
        return res
