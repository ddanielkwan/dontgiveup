class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        hashmap = {}
        #have a hashmap store the difference between target and n, index
        for index, n in enumerate(nums):
            if target - n in hashmap:
                return [hashmap[target-n], index]
            
            hashmap[n] = index
        