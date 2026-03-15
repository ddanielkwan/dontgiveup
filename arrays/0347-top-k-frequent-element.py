# Given an integer array nums and an integer k, 
# return the k most frequent elements. 
# You may return the answer in any order.


from collections import Counter

#USE ARRRATY FOR BUCKETSORT
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        #bucket sort using array indices, each index represents the bucket (times of occurence)
        #the max occurence is len(nums) + 1

        frequency = Counter(nums)

        buckets = [[] for _ in range(len(nums)+1)]

        for element, count in frequency.items():
            buckets[count].append(element)

        res = []

        for i in range(len(buckets)-1, -1, -1):

            for element in buckets[i]:
                res.append(element)
                k -= 1
                if k == 0:
                    return res



            

