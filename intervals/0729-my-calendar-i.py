# You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.

# A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).

# The event can be represented as a pair of integers startTime and endTime that represents a booking on the half-open interval [startTime, endTime), the range of real numbers x such that startTime <= x < endTime.

# Implement the MyCalendar class:

# MyCalendar() Initializes the calendar object.
# boolean book(int startTime, int endTime) Returns true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.
 

# Example 1:

# Input
# ["MyCalendar", "book", "book", "book"]
# [[], [10, 20], [15, 25], [20, 30]]
# Output
# [null, true, false, true]

# Explanation
# MyCalendar myCalendar = new MyCalendar();
# myCalendar.book(10, 20); // return True
# myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked by another event.
# myCalendar.book(20, 30); // return True, The event can be booked, as the first event takes every time less than 20, but not including 20.



class Tree: #tree (10,15) , and if candidate  (15,20) has to go right (5,10) goes left
# 7,16 -> reutrns false cant go either
    def __init__(self, start,end):
        self.left = None
        self.right = None
        self.start = start
        self.end = end
    
    def insert(self, start, end):
        curr = self
        while True:
            if start >= curr.end: #were safe go right,
                if not curr.right:
                    curr.right = Tree(start,end)
                    return True
                curr = curr.right
            elif end <= curr.start: #were safe go left
                if not curr.left:
                    curr.left = Tree(start,end)
                    return True

                curr = curr.left
            else: #there is a merge return false
                return False


class MyCalendar:
    def __init__(self):
        
        self.root = None
    
    def book(self, startTime, endTime):
        if not self.root:
            self.root = Tree(startTime, endTime)
            return True
        
        return self.root.insert(startTime,endTime)


    # def __init__(self):
        
    #     self.events = []
    # def book(self, startTime: int, endTime: int) -> bool:
    #     for s, e in self.events:
    #         if startTime < e and s < endTime:
    #             return False
    #     self.events.append((startTime,endTime))
    #     return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)

