# You are given a 0-indexed array nums of distinct integers. You want to rearrange the elements in the array such that every element in the rearranged array is not equal to the average of its neighbors.

# More formally, the rearranged array should have the property such that for every i in the range 1 <= i < nums.length - 1, (nums[i-1] + nums[i+1]) / 2 is not equal to nums[i].

# Return any rearrangement of nums that meets the requirements.

 

# Example 1:

# Input: nums = [1,2,3,4,5]
# Output: [1,2,4,5,3]
# Explanation:
# When i=1, nums[i] = 2, and the average of its neighbors is (1+4) / 2 = 2.5.
# When i=2, nums[i] = 4, and the average of its neighbors is (2+5) / 2 = 3.5.
# When i=3, nums[i] = 5, and the average of its neighbors is (4+3) / 2 = 3.5.

class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        #intuition: guarantee the average will always be higher/not equal is if the neighbours beside is greater
        nums.sort()
        l = 0
        r = len(nums) - 1
        res = []
        
        #skip index next time
        # 1 _ 2 _ 3
        while len(res) != len(nums) :
            res.append(nums[l])

            l += 1
            if l <= r :
                res.append(nums[r])
                r -= 1
        return res