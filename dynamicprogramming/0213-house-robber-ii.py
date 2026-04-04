class Solution:
    def rob(self, nums: List[int]) -> int:
        

        def houserobberi(nums):
            rob1 = 0
            rob2 = 0

            for n in nums:
                tmp = max(rob1 + n , rob2)
                rob1 = rob2
                rob2 = tmp
            return rob2
        
        return max(nums[0],max(houserobberi(nums[1:]), houserobberi(nums[:-1])))