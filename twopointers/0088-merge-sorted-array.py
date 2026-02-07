# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
# and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, 
# but instead be stored inside the array nums1. To accommodate this, 
# nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
# and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

# Example 1:

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # intuition: rather than us starting from the beginning, let us start backwards, since the ends of nums1 have 0s
        #and we know that the largest has to go at the end, and they are both sorted
        #we use two pointers one for each array, and have a pointer that starts from the end

        total = m + n #get total number of elements
        zeroes = total - m #total number of zeroes

        pointer = total - 1 #since were dealing with indices 

        nums2ptr = n - 1
        nums1ptr = m - 1

        while nums1ptr >= 0 and nums2ptr >= 0:
            if nums1[nums1ptr] > nums2[nums2ptr]: #get whichever one is larger
                nums1[pointer] = nums1[nums1ptr]
                nums1ptr -= 1
                
            else:
                nums1[pointer] = nums2[nums2ptr]
                nums2ptr -= 1

            pointer -= 1
        
        while nums2ptr >= 0 :
            nums1[pointer] = nums2[nums2ptr]
            pointer -= 1
            nums2ptr -= 1

            
        
