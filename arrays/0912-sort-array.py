# Given an array of integers nums, sort the array in ascending order and return it.

# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

 

# Example 1:

# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).



class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:

        #merge sort
        #two parts to merge sort
        #merge part which does the sorting
        #partition part, which does the splitting from middle

        def merge(arr, l, m , r):
            left = arr[l : m + 1]
            right = arr[m + 1 : r + 1]

            #in place 
            startptr = l #tracks where to insert in

            leftptr = 0
            rightptr = 0

            while leftptr < len(left) and  rightptr < len(right):
                if left[leftptr] < right[rightptr]:
                    arr[startptr] = left[leftptr]
                    leftptr += 1
                else:
                    arr[startptr] = right[rightptr]
                    rightptr += 1
                startptr += 1
            
            #remaining because we could have just merged all of one side, and never moved the other
            while leftptr < len(left):
                arr[startptr] = left[leftptr]
                leftptr += 1
                startptr += 1
                
            while rightptr < len(right):
                arr[startptr] = right[rightptr]
                rightptr += 1
                startptr += 1



        def mergeSort(arr, l , r): #splits middle

            if l == r :
                return arr
            
            m = (l + r )// 2
            mergeSort(arr, l, m)
            mergeSort(arr, m + 1, r)

            merge(arr, l, m , r)

            return arr

        return mergeSort(nums, 0, len(nums) - 1)


        

      

