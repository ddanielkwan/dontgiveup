# You are part of a university admissions office and need to keep track of the kth highest test score from applicants in real-time. This helps to determine cut-off marks for interviews and admissions dynamically as new applicants submit their scores.

# You are tasked to implement a class which, for a given integer k, maintains a stream of test scores and continuously returns the kth highest test score after a new score has been submitted. More specifically, we are looking for the kth highest score in the sorted list of all scores.

# Implement the KthLargest class:

# KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of test scores nums.
# int add(int val) Adds a new test score val to the stream and returns the element representing the kth largest element in the pool of test scores so far.
 

# Example 1:

# Input:
# ["KthLargest", "add", "add", "add", "add", "add"]
# [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]

# Output: [null, 4, 5, 5, 8, 8]



# KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
# kthLargest.add(3); // return 4
# kthLargest.add(5); // return 5
# kthLargest.add(10); // return 5
# kthLargest.add(9); // return 8
# kthLargest.add(4); // return 8

import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # k = which largest element we want to track
        self.k = k
        
        # we will use nums itself as a min heap
        self.nums = nums
        
        # turn the list into a min-heap in O(n)
        # IMPORTANT: heap[0] will always be the SMALLEST element
        heapq.heapify(self.nums)

        # We only want to keep the k largest elements in the heap
        # If there are more than k elements, remove the smallest
        # This ensures the heap always contains the TOP k largest numbers
        while len(self.nums) > k:
            heapq.heappop(self.nums)   # remove smallest element

        # After this loop:
        # - heap size == k
        # - heap contains the k largest numbers seen so far
        # - heap[0] = smallest among those k numbers
        #           = kth largest overall

    def add(self, val: int) -> int:
        # Add the new value into the heap
        heapq.heappush(self.nums, val)

        # If heap grows bigger than k,
        # remove the smallest element
        # This keeps only the k largest numbers
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)

        # The heap stores the k largest elements.
        # The smallest among them sits at index 0.
        # That smallest-of-the-top-k is exactly the kth largest overall.
        return self.nums[0]
