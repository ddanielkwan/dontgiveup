# You are given a circular array nums and an array queries.

# For each query i, you have to find the following:

# The minimum distance between the element at index queries[i] and any other index j in the circular array, where nums[j] == nums[queries[i]]. If no such index exists, the answer for that query should be -1.
# Return an array answer of the same size as queries, where answer[i] represents the result for query i.

 

# Example 1:

# Input: nums = [1,3,1,4,1,3,2], queries = [0,3,5]

# Output: [2,-1,3]

# Explanation:

# Query 0: The element at queries[0] = 0 is nums[0] = 1. The nearest index with the same value is 2, and the distance between them is 2.
# Query 1: The element at queries[1] = 3 is nums[3] = 4. No other index contains 4, so the result is -1.
# Query 2: The element at queries[2] = 5 is nums[5] = 3. The nearest index with the same value is 1, and the distance between them is 3 (following the circular path: 5 -> 6 -> 0 -> 1).
# Example 2:

# Input: nums = [1,2,3,4], queries = [0,1,2,3]

# Output: [-1,-1,-1,-1]

# Explanation:

# Each value in nums is unique, so no index shares the same value as the queried element. This results in -1 for all queries.


# class Solution:
#     def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
#         hashmap = defaultdict(list)
#         for i,element in enumerate(nums):
#             hashmap[element].append(i)

#         result = []
#         for q in queries:
#             #if only itself not possible
#             if len(hashmap[nums[q]]) == 1:
#                 result.append(-1)
#                 continue

#             best = float('inf')
#             for idx in hashmap[nums[q]]:

#                 if idx == q:
#                     continue
#                 #direct difference non circular
#                 direct = abs(q - idx)
#                 #other way
#                 circular = len(nums) - direct

#                 best = min(best, direct, circular)
#             result.append(best)
#         return result
        


from collections import defaultdict

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:

        n = len(nums)

        positions = defaultdict(list)
        #value: [index1, index2]
        for i, num in enumerate(nums):
            positions[num].append(i)

# For the element at index i, what is the nearest same-value index on the left
        leftNeighbor = [-1] * n 
        rightNeighbor = [-1] * n

        # build neighbor relationships
        for arr in positions.values():

            m = len(arr)

            if m == 1:
                continue

            for i in range(m):

                curr = arr[i] #index

                leftNeighbor[curr] = arr[(i - 1) % m]
                rightNeighbor[curr] = arr[(i + 1) % m]

        result = []

        for q in queries:

            if leftNeighbor[q] == -1:
                result.append(-1)
                continue

            best = float('inf')

            for neighbor in [leftNeighbor[q], rightNeighbor[q]]:

                d = abs(q - neighbor)

                best = min(best, d, n - d)

            result.append(best)

        return result