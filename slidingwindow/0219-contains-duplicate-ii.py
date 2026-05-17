# Given an integer array nums and an integer k, 
# return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true
# Example 2:

# Input: nums = [1,0,1,1], k = 1
# Output: true
# Example 3:

# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        #when you see the same number again, you only care how far it is from the last time you saw it

        l = 0
        tracker = set()
        if k == 0:
            return False
        for r in range(len(nums)):
            if nums[r] in tracker:
                return True
            
            if r - l >= k:
                tracker.remove(nums[l])
                l += 1
            
            tracker.add(nums[r])
        
        return False


