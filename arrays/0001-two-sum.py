# 1. What are we trying to solve?
#    Given an array of integers and a target, find two indices whose values sum to target.
#    Return those two indices.

# 2. What data structure should we use?
#    A hashmap — we can store each number and its index as we scan through.
#    This lets us look up whether the "complement" (target - current number) already exists in O(1).

# 3. What approach?
#    For each number n, the number we need is (target - n).
#    If (target - n) is already in the hashmap, we found our pair — return both indices.
#    Otherwise, store n with its index and keep going.
#    This avoids the O(n^2) brute force of checking every pair.

# 4. Walk through example: nums = [2, 7, 11, 15], target = 9
#    i=0, n=2  -> need 7, not in map yet -> store {2: 0}
#    i=1, n=7  -> need 2, found in map at index 0 -> return [0, 1]

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        hashmap = {}
        #have a hashmap store the difference between target and n, index
        for index, n in enumerate(nums):
            if target - n in hashmap:
                return [hashmap[target-n], index]

            hashmap[n] = index
        
