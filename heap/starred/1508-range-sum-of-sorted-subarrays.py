
# You are given the array nums consisting of n positive integers. You computed the sum of all non-empty continuous subarrays from the array and then sorted them in non-decreasing order, creating a new array of n * (n + 1) / 2 numbers.

# Return the sum of the numbers from index left to index right (indexed from 1), inclusive, in the new array. Since the answer can be a huge number return it modulo 109 + 7.

 

# Example 1:

# Input: nums = [1,2,3,4], n = 4, left = 1, right = 5
# Output: 13 
# Explanation: All subarray sums are 1, 3, 6, 10, 2, 5, 9, 3, 7, 4. After sorting them in non-decreasing order we have the new array [1, 2, 3, 3, 4, 5, 6, 7, 9, 10]. The sum of the numbers from index le = 1 to ri = 5 is 1 + 2 + 3 + 3 + 4 = 13. 

# class Solution:
    # def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        #solu 1
#         MOD = 10 ** 9 + 7
#         subarr_sums =[]
# #genereates lal sum for all subarrays
# # [1]       -> 1
# # [1,2]     -> 3
# # [1,2,3]   -> 6
# # [2]       -> 2
# # [2,3]     -> 5
# # [3]       -> 3
#         for i in range(n):
#             currsum = 0
#             for j in range(i, n):
#                 currsum = (currsum + nums[j]) % MOD
#                 subarr_sums.append(currsum)

#         subarr_sums.sort()
#         res = 0
#         #only get sums from left and right
#         for i in range(left-1, right):
#             res = (res + subarr_sums[i]) % MOD
        
#         return res

#solu 2
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        # We want the sum of the subarray sums ranked from left to right
        # in sorted order.
        
        MOD = 10 ** 9 + 7

        # Min heap stores tuples:
        # (current subarray sum, ending index of that subarray)
        # Initially, each element alone is a subarray.
        minHeap = [(value, index) for index, value in enumerate(nums)]
        heapq.heapify(minHeap)

        res = 0

        # We only need the first 'right' smallest subarray sums
        for i in range(right):
            # Get the smallest subarray sum currently available
            curr_sum, end_index = heapq.heappop(minHeap)

            # Only add if within desired range (1-indexed adjustment)
            if i >= left - 1:
                res = (res + curr_sum) % MOD

            # If we can extend this subarray further,
            # push the next extended version into heap
            if end_index + 1 < n:
                new_sum = curr_sum + nums[end_index + 1]
                heapq.heappush(minHeap, (new_sum, end_index + 1))

        return res
