# Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.

 

# Example 1:

# Input: arr = [5,5,4], k = 1
# Output: 1
# Explanation: Remove the single 4, only 5 is left.
# Example 2:
# Input: arr = [4,3,1,1,3,3,2], k = 3
# Output: 2
# Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        # counter = Counter(arr)

        # minHeap = [(freq, item) for item, freq in counter.items()]
        # heapq.heapify(minHeap)

        # for i in range(k):
        #     if k <= 0:
        #         break
            
        #     freq, item = heapq.heappop(minHeap)  #Pop the element with the lowest frequency
        #     k -= freq

        #     if k < 0:
        #         heapq.heappush(minHeap, (abs(k), item)) #and if k is negative, means we removed too many, so add it back
        #         k = 0
                



        # return len(minHeap)

        #bucket sort
        freq = Counter(arr)

        frequencies = [[] for _ in range(len(arr) + 1)]

        #put occurence as index
        for key, occurence in freq.items():
            frequencies[occurence].append(key)
        
        unique = len(freq)

        for count in range(1,len(frequencies)):
            row = frequencies[count]
            if not row:
                continue
            for item in row:
                if k - count >= 0 :
                    del freq[item]
                    k -= count
                    unique -= 1
                else:
                    return unique
        return len(freq)
