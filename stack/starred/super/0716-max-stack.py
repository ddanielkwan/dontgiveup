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
        self.count = 0
        self.stack = []
        self.minheap = []
        self.removed = set()

    def push(self, x: int) -> None:
        self.stack.append([x, self.count])
        heapq.heappush(self.minheap, (-x, -self.count))
        self.count += 1
    

    def pop(self) -> int:
        while self.stack and self.stack[-1][1] in self.removed:
            self.stack.pop()
        num, count = self.stack.pop()
        self.removed.add(count)
        return num

    def top(self) -> int:
        while self.stack and self.stack[-1][1] in self.removed:
            self.stack.pop()
        return self.stack[-1][0]

    def peekMax(self) -> int:
        while self.minheap and -self.minheap[0][1] in self.removed:
            heapq.heappop(self.minheap)
        return -self.minheap[0][0]

        

    def popMax(self) -> int:
        while self.minheap and -self.minheap[0][1] in self.removed:
            heapq.heappop(self.minheap)
        num, index = heapq.heappop(self.minheap)
        self.removed.add(-index)
        return -num
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()