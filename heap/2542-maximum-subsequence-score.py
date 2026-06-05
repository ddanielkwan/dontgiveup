# You are given two 0-indexed integer arrays nums1 and nums2 of equal length n and a positive integer k. 
# You must choose a subsequence of indices from nums1 of length k.

# For chosen indices i0, i1, ..., ik - 1, your score is defined as:

# The sum of the selected elements from nums1 multiplied with the minimum of the selected elements from nums2.
# It can defined simply as: (nums1[i0] + nums1[i1] +...+ nums1[ik - 1]) * min(nums2[i0] , nums2[i1], ... ,nums2[ik - 1]).
# Return the maximum possible score.

# A subsequence of indices of an array is a set that can be derived from the set {0, 1, ..., n-1} by deleting some or no elements.

 

# Example 1:

# Input: nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3
# Output: 12
# Explanation:      
# The four possible subsequence scores are:
# - We choose the indices 0, 1, and 2 with score = (1+3+3) * min(2,1,3) = 7.
# - We choose the indices 0, 1, and 3 with score = (1+3+2) * min(2,1,4) = 6. 
# - We choose the indices 0, 2, and 3 with score = (1+3+2) * min(2,3,4) = 12. 
# - We choose the indices 1, 2, and 3 with score = (3+3+2) * min(1,3,4) = 8.
# Therefore, we return the max score, which is 12.

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        #  nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3
        #note that if k = 3 , then the min that is possible can only be either 2 or 1
        #in that case, since the minimum at doesnt change if you have more for examlike like 
        # [5,4,3,2,1] min is still 2 if you choose(5,3,2) or (4,3,2)
        #so then the second problem becomes, in numbers in n1, which ones are largest?
        #we use heap to pop smallest from num1

        pairs = [(n1,n2 ) for n1,n2 in zip(nums1, nums2)]
        #want to sort in descending for second num2
        pairs = sorted(pairs,key=lambda p:p[1], reverse = True)
        print(pairs)
        n1Sum = 0
        n2Min = float('inf')
        maxScore = 0

        minHeap = []

        for n1,n2 in pairs:
            n1Sum += n1
            n2Min = min(n2Min,n2) #not needed ssince we already sorted

            heapq.heappush(minHeap, n1)

            #have we gone over the length of k
            if len(minHeap) > k:
                #realization: once n2 is sorted in desc,
                #4,3,2,1 does it matter what we choice from 2 elements from [4,3,2] not because
                #the min is always 1, so now we want to optimize the remove the smallest n1 value
                #thats whywe have heap
                n1Pop = heapq.heappop(minHeap) #this pops the smallest n1, because we only care n1 if the min is alreadh set
                n1Sum -= n1Pop
            
            if len(minHeap) == k:
                maxScore = max(maxScore, n1Sum * n2Min)
            
        return maxScore

