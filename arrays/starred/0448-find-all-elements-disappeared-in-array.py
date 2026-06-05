# Given an array nums of n integers where nums[i] is in the range [1, n], 
# return an array of all the integers in the range [1, n] that do not appear in nums.

 

# Example 1:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]
# Example 2:

# Input: nums = [1,1]
# Output: [2]

class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        #[1,n] inclusive if n = 3 , then 1, 2, 3
        #brute force just loop and check if not in nums

        # res = []
        # n = len(nums)

        # for i in range(1, n+1):
        #     if i not in nums:
        #         res.append(i)
        # return res


        #use negative marking trick, since every element is 1-indexed you can substract -1 to get index and mark negative
        #then you can find which index has not been marked, then +1 to get the element

        # [4,3,2,7,8,2,3,1]
        # [0 -3 -2 -7 0 0 -3 -1]
        for num in nums:
            index = abs(num) - 1
            nums[index] = -1 * abs(nums[index]) #we use abs here because if its already marked negative then -> it turns to positive, we dont want that
        

        res = []
        for i , num in enumerate(nums):
            if num > 0:
                res.append(i+1) #+1 to get element
        return res

