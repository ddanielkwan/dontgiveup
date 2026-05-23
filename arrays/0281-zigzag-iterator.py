# Given two vectors of integers v1 and v2, implement an iterator to return their elements alternately.

# Implement the ZigzagIterator class:

# ZigzagIterator(List<int> v1, List<int> v2) initializes the object with the two vectors v1 and v2.
# boolean hasNext() returns true if the iterator still has elements, and false otherwise.
# int next() returns the current element of the iterator and moves the iterator to the next element.
 

# Example 1:

# Input: v1 = [1,2], v2 = [3,4,5,6]
# Output: [1,3,2,4,5,6]
# Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,3,2,4,5,6].



class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.v1 = deque(v1)
        self.v2 = deque(v2)
        self.first = True
    def next(self) -> int:
        if self.first:
            if len(self.v1):
                self.first = False
                return self.v1.popleft()
            else:
                self.first = False
                return self.v2.popleft()
        else:
            if len(self.v2):
                self.first = True
                return self.v2.popleft()
            else:
                self.first=False
                return self.v1.popleft()

    def hasNext(self) -> bool:
        return self.v1 or self.v2
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())