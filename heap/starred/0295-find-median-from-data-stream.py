# The median is the middle value in an ordered integer list. If the size of the list is even, 
# there is no middle value, and the median is the mean of the two middle values.

# For example, for arr = [2,3,4], the median is 3.
# For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
# Implement the MedianFinder class:

# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data structure.
# double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
 

# Example 1:

# Input
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# [[], [1], [2], [], [3], []]
# Output
# [null, null, null, 1.5, null, 2.0]

# Explanation
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(1);    // arr = [1]
# medianFinder.addNum(2);    // arr = [1, 2]
# medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
# medianFinder.addNum(3);    // arr[1, 2, 3]
# medianFinder.findMedian(); // return 2.0



class MedianFinder:
    #note, just use two heaps one for left and one for right
    #makes sense the left is max heap because when we pop it should be greatest of left side
    #right side is min heap when we pop its min of right 
    def __init__(self):
        self.left = [] #max heap [1,2]
        self.right = [] #min heap [ 3,4]
        #where all elements in right is greater than left

        

    def addNum(self, num: int) -> None:
        #default insert into a side and check afterwards
        #step 1 insert
        heapq.heappush(self.left, -num) #maxheap
        #left = [1,7] right = [2] this case 7 is not correct need to be in right
        #self.left[0] is max
        #self.right[0] is min
        if (self.left and self.right and -self.left[0] > self.right[0]):
            val = -heapq.heappop(self.left)
            heapq.heappush(self.right, val)
        #case where unbalanced heap but order satisfy left < right
        # left = [1,2,3] right = [4] #we want at least 1 not 2 diff


        #[3,2,1], [4]
        #[2,1], [3,4]
        if len(self.left) > len(self.right) + 1:
            val = -heapq.heappop(self.left)
            heapq.heappush(self.right, val)
        
        elif len(self.right) > len(self.left) + 1:
            val = heapq.heappop(self.right)
            heapq.heappush(self.left, -val) #dont forget -

        
    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0] #max
        elif len(self.right) > len(self.left):
            return self.right[0]#min of right
        else:
            return (-self.left[0]+ self.right[0])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

