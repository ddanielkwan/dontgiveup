# Given an integer array nums, reorder it such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

# You may assume the input array always has a valid answer.

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # maxHeap = []
        # for num in nums:
        #     heappush(maxHeap, -num)

        # n = len(nums)
        # for i in range(1, n, 2):
        #     nums[i] = -heappop(maxHeap)
        # for i in range(0, n, 2):
        #     nums[i] = -heappop(maxHeap)

        nums.sort()
        for i in range(1, len(nums) - 1, 2):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
        
        #greedy approach o(n) and o(1) space

        #we just want items x< b > y like a peak
        #notice how even is always greater than one before it
        #and oddis less than one beforer it

        #[6,4,3,2,7]
          # ^
        
        for i in range(1,len(nums)):
            if i % 2 == 0 and nums[i] > nums[i-1]:
                nums[i], nums[i-1] = nums[i-1], nums[i]        
            if i % 2 != 0 and nums[i] < nums[i-1]:
                nums[i], nums[i-1] = nums[i-1], nums[i]        
        