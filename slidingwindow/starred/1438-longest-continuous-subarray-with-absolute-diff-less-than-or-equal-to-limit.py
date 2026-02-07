from collections import deque
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxq = deque()
        minq = deque()


        res = 0

        l = 0

        for r in range(len(nums)):
            while minq and minq[-1] > nums[r]:
                minq.pop()
            while maxq and maxq[-1] < nums[r]:
                maxq.pop()
            
            minq.append(nums[r])
            maxq.append(nums[r])

            while maxq[0] - minq[0] > limit:
                if nums[l] == maxq[0]:
                    maxq.popleft()
                if nums[l] == minq[0]:
                    minq.popleft()
                l += 1
            res = max(res, r-l+1)
        return res

            