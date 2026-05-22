# You are given an array of strings nums and an integer k. Each string in nums represents an integer without leading zeros.

# Return the string that represents the kth largest integer in nums.

# Note: Duplicate numbers should be counted distinctly. For example, if nums is ["1","2","2"], "2" is the first largest integer, "2" is the second-largest integer, and "1" is the third-largest integer.

 

# Example 1:

# Input: nums = ["3","6","7","10"], k = 4
# Output: "3"
# Explanation:
# The numbers in nums sorted in non-decreasing order are ["3","6","7","10"].
# The 4th largest integer in nums is "3".


class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        maxheap = [-int(num) for num in nums]
        heapq.heapify(maxheap)

        while k > 0:
            ans = heapq.heappop(maxheap)
            k-=1
        return str(-ans)


class Solution:
#     Quickselect is better when we only need the kth element once,
# because its average time complexity is O(n), which is faster than sorting.

# However, its worst case is O(n²) if the pivot choices are consistently bad
# (e.g. always splitting into n-1 and 0 elements).

#1,2,3,4,5
#suppose we want 1st smallest element
#but pivot is 5 so weloop 1234
#then 4, 123,..
# Heap is often preferred when:
# - we need repeated kth/top-k queries
# - streaming data
# - guaranteed performance

# since heap operations are predictably O(log n)./


    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        k = len(nums) - k
        nums = list(map(lambda x: int(x),nums))
        # Quickselect is better when we only need the kth element, not the fully sorted order
        def quickselect(l, r ):
            pivot = r 
            p = l

            for i in range(l,r):
                if nums[i] < nums[pivot]:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[pivot] = nums[pivot], nums[p]
        # p is the final position/index where the pivot ends up after partitioning
            if p > k :
                return quickselect(l, p-1)
            elif p < k:
                return quickselect(p+1,r)
            else:
                return nums[p]
        return str(quickselect(0, len(nums)-1))
