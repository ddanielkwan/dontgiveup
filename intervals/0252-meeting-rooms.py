# You are given an array of meeting time intervals, where each interval is represented as intervals[i] = [starti, endi].
#  Each interval contains a start time and an end time for a meeting. Your task is to determine
#  whether a person can attend all the meetings without any time conflicts.

# A person can attend all meetings if no two meetings overlap in time.
#  Two meetings overlap if one meeting starts before the other meeting ends.

# For example:

# If you have meetings [0, 30] and [5, 10], these overlap because the second meeting starts at time 5,
#  which is before the first meeting ends at time 30. The person cannot attend both meetings.
# If you have meetings [0, 30] and [35, 50], these don't overlap because the second meeting starts after the first one ends. 
# The person can attend both meetings.
# The function should return true if the person can attend all meetings (no overlaps exist), and
#  false if there are any time conflicts between meetings.


"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)

        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]
            i2 = intervals[i]

            if i1.end > i2.start:
                return False
        return True
    

