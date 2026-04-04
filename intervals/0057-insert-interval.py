# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

# Return intervals after the insertion.

# Note that you don't need to modify intervals in-place. You can make a new array and return it.

 

# Example 1:

# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# Example 2:

# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].



class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # #linear o(n) search
        # n = len(intervals)
        # i = 0
        # res = []
        # #while new interval's endtime isless than start time
        # while i < n and intervals[i][1] < newInterval[0]:
        #     res.append(intervals[i])
        #     i += 1
        # #iterate all large rand merge
        # while i < n and newInterval[1] >= intervals[i][0]:
        #     newInterval[0] = min(newInterval[0], intervals[i][0])
        #     newInterval[1] = max(newInterval[1], intervals[i][1])
        #     i += 1
        # res.append(newInterval)
        # #add remaining
        # while i < n:
        #     res.append(intervals[i])
        #     i += 1

        # return res


        #binary searchb ut still o(n) cause merge

        if not intervals:
            return [newInterval]
        
        l = 0
        r = len(intervals) - 1

        while l <= r :
            m = l + (r-l)//2

            start, end = intervals[m]

            if start < newInterval[0]:  #[1,3] [6,9]. inserting [2,5] 
                l = m + 1 #go right
            else:
                r = m - 1
        intervals.insert(l, newInterval)

        res = [intervals[0]]

        for start, end in intervals[1:]:
            if start <= res[-1][1]:
                res[-1][1] = max(end, res[-1][1])
            else:
                res.append([start,end])
        return res
