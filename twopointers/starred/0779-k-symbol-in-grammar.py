# We build a table of n rows (1-indexed). 
# We start by writing 0 in the 1st row. Now in every subsequent row, 
# we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

# For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.
# Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a table of n rows.

 

# Example 1:

# Input: n = 1, k = 1
# Output: 0
# Explanation: row 1: 0
# Example 2:

# Input: n = 2, k = 1
# Output: 0
# Explanation: 
# row 1: 0
# row 2: 01

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # We simulate walking down the grammar tree WITHOUT building the string
        # Start from the root value (row 1), which is always 0
        curr = 0

        # Each row has 2^(row-1) elements.
        # We treat the final row as a range [1, 2^(n-1)]
        # and use binary search to see whether k falls in the left
        # or right half at each level.
        l = 1
        r = 2 ** (n - 1) #max

        #if you write down a tree for 0 becomes 01 and 1 becoemes 10
        #youll notice that for each previous row, if you go left, the element is the same
        #if you go right thelement is not same
        for _ in range(n - 1):
            mid = l + (r - l) // 2

            if k <= mid:
                #going left is same as parent no flip
                r = mid
            else:
                # right child is the FLIPPED value of the parent,
                # so we toggle curr
                l = mid + 1
                if curr == 1: 
                    curr = 0 
                else: 
                    curr = 1

        return curr

