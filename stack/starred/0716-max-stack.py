# Design a max stack data structure that supports the stack operations and supports finding the stack's maximum element.

# Implement the MaxStack class:

# MaxStack() Initializes the stack object.
# void push(int x) Pushes element x onto the stack.
# int pop() Removes the element on top of the stack and returns it.
# int top() Gets the element on the top of the stack without removing it.
# int peekMax() Retrieves the maximum element in the stack without removing it.
# int popMax() Retrieves the maximum element in the stack and removes it. If there is more than one maximum element, only remove the top-most one.
# You must come up with a solution that supports O(1) for each top call and O(logn) for each other call.

 

# Example 1:

# Input
# ["MaxStack", "push", "push", "push", "top", "popMax", "top", "peekMax", "pop", "top"]
# [[], [5], [1], [5], [], [], [], [], [], []]
# Output
# [null, null, null, null, 5, 5, 1, 5, 1, 5]
class MaxStack:

    def __init__(self):

        # unique id for every pushed element
        # helps us know which exact element was removed
        self.count = 0

        # normal stack
        # stores: [value, unique_id]
        self.stack = []

        # max heap (python only has min heap so use negative values)
        # stores: (-value, -unique_id)
        #
        # why negative unique_id?
        # if values are equal, larger index should come first
        # because popMax removes the TOP-MOST maximum
        self.minheap = []

        # stores ids of elements already removed
        #
        # because an element can be removed from stack first
        # OR from heap first
        #
        # we use "lazy deletion":
        # mark deleted first, physically remove later
        self.removed = set()

    def push(self, x: int) -> None:

        # add element to stack
        self.stack.append([x, self.count])

        # add to max heap
        #
        # use negatives to simulate max heap
        heapq.heappush(self.minheap, (-x, -self.count))

        # next unique id
        self.count += 1
    

    def pop(self) -> int:

        # remove stale elements from top of stack
        #
        # stale = already removed through popMax()
        while self.stack and self.stack[-1][1] in self.removed:
            self.stack.pop()

        # actual top element
        num, count = self.stack.pop()

        # mark as removed so heap knows later
        self.removed.add(count)

        return num

    def top(self) -> int:

        # clean stale elements first
        while self.stack and self.stack[-1][1] in self.removed:
            self.stack.pop()

        # return top value only
        return self.stack[-1][0]

    def peekMax(self) -> int:

        # remove stale heap elements
        #
        # these were already removed from stack
        while self.minheap and -self.minheap[0][1] in self.removed:
            heapq.heappop(self.minheap)

        # heap stores negatives
        return -self.minheap[0][0]

        

    def popMax(self) -> int:

        # remove stale heap elements first
        while self.minheap and -self.minheap[0][1] in self.removed:
            heapq.heappop(self.minheap)

        # get largest element
        num, index = heapq.heappop(self.minheap)

        # mark this element as deleted
        #
        # stack will clean it later lazily
        self.removed.add(-index)

        # convert back from negative
        return -num