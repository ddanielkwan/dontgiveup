# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

 

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        
        #the idea here is to use binary search
        #we want to imagine one left box and one right box for each array
        #so mid point, and that mid point determines how many elements from that array should be on the left side of the merged array
        #because its median, we must compare the left box to the other array's right box and left must be smaller than all of the other array's right box 
        #else we adjust
        nums1.sort() 
        nums2.sort()

        a, b = nums1, nums2

        if len(a) > len(b):
            a, b = b, a

        totalLength = len(a) + len(b)
        half = totalLength//2
        
        l = 0
        r = len(a) - 1

        while True:
            midPointA = l + (r-l)//2
            midPointB = half - midPointA - 2 #we know midpointB, box must be this size because it must all add up to half which is the total number of elements on the left side

            bRight = b[midPointB + 1] if midPointB + 1 < len(b) else float('inf')
            aRight = a[midPointA + 1] if midPointA + 1 < len(a) else float('inf')
            bLeft = b[midPointB] if midPointB >= 0 else float('-inf')
            aLeft = a[midPointA] if midPointA >= 0 else float('-inf')

            if aLeft <= bRight and bLeft <= aRight:
                #happy case
                if totalLength % 2 == 0: #even
                    #then the median is the average between max of left and min of right
                    return (max(aLeft, bLeft) + min(bRight, aRight))/2
                return min(aRight,bRight) #else odd take the min since its on left
            elif aLeft > bLeft:
                # l and r control the binary search on a's partition
# moving r left (r = midPointA - 1) → take FEWER elements from a
# moving l right (l = midPointA + 1) → take MORE elements from a
                r = midPointA - 1
            else:
                l = midPointA + 1
