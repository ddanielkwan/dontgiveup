# Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i),
#  find the minimum number of rooms required to schedule all meetings without any conflicts.

# Note: (0,8),(8,10) is NOT considered a conflict at 8.

# Example 1:

# Input: intervals = [(0,40),(5,10),(15,20)]

# Output: 2
# Explanation:
# day1: (0,40)
# day2: (5,10),(15,20)

# Example 2:

# Input: intervals = [(4,9)]

# Output: 1


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        tracker = []
        for interval in intervals:
            start = interval.start
            end = interval.end
            tracker.append([start,'start'])
            tracker.append([end,'end'])
        
        tracker.sort(key=lambda x : (x[0], x[1] == 'start'))
        max_days = 0
        res = 0
        for time, event in tracker:
            if event == 'start':
                max_days += 1
                res = max(res,max_days)

            elif event == 'end' :
                max_days -= 1
        return res
    
class Solution:

    def minMeetingRoom(self, intervals):
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        res = 0
        count = 0

        s, e = 0, 0

        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1

            else:
                e += 1
                count -= 1
            res = max(res,count)
        
        return res

