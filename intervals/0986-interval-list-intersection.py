
# You are given two lists of closed intervals,
#  firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. 
# Each list of intervals is pairwise disjoint and in sorted order.

# Return the intersection of these two interval lists.

# A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

# The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. 
# For example, the intersection of [1, 3] and [2, 4] is [2, 3].

 

# Example 1:


# Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
# Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
# Example 2:

# Input: firstList = [[1,3],[5,9]], secondList = []
# Output: []



class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        #two pointers?

        #brute force
        # res = []
        # for i in range(len(firstList)):
        #     startA, endA = firstList[i][0], firstList[i][1]
        #     for j in range(len(secondList)):
        #         startB, endB = secondList[j][0], secondList[j][1]
        #         if (startA <= startB <= endA) or (startB <= startA <= endB):
        #             res.append([max(startA, startB), min(endA, endB)])
        # return res

        #line sweep
        store = defaultdict(int)
        for s, e in firstList:
            store[s] += 1
            store[e + 1] -= 1 #this interval just ended, we dont want e = -1 because e is inclusive
        for s, e in secondList:
            store[s] += 1
            store[e + 1] -= 1

        res = []
        active = 0
        prev = None
        for x in sorted(store):
            if active == 2:
                res.append([prev, x - 1])
            active += store[x]
            prev = x #Because after processing position x, 
            # you need to remember where the next potential intersection would start
        return res


        #two pointers
        res = []
        i = 0 #first
        j = 0 #second
        while i < len(firstList) and j < len(secondList):
            startA, endA = firstList[i]
            startB, endB = secondList[j]

            start = max(startA, startB) #the later of the two starts
            end = min(endA, endB) #the earlier of the two ends

            if start <= end: #[1,4] , [2,3] -> (2,3) start <= end they intersect
                res.append([start, end])
            # endA < endB -> interval A ends first -> advance i
# endA >= endB -> interval B ends first (or tie) -> advance j

# You always advance the pointer whose interval ends sooner, because that interval is "finished" — it can't intersect anything further ahead in the other list
            if endA < endB: 
                i += 1
            else:
                j += 1

        return res

