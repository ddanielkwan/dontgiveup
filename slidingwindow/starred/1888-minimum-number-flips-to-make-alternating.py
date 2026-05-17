# You are given a binary string s. You are allowed to perform two types of operations on the string in any sequence:

# Type-1: Remove the character at the start of the string s and append it to the end of the string.
# Type-2: Pick any character in s and flip its value, i.e., if its value is '0' it becomes '1' and vice-versa.
# Return the minimum number of type-2 operations you need to perform such that s becomes alternating.

# The string is called alternating if no two adjacent characters are equal.

# For example, the strings "010" and "1010" are alternating, while the string "0100" is not.
 

# Example 1:

# Input: s = "111000"
# Output: 2
# Explanation: Use the first operation two times to make s = "100011".
# Then, use the second operation on the third and sixth elements to make s = "101010".

#brute force, generate every string at every index for type 1 ops, and then compare diffs for type 2
# class Solution:
#     def minFlips(self, s: str) -> int:
#         res = n = len(s)
#         alt1, alt2 = [], []
#         for i in range(n):
#             alt1.append("0" if i % 2 == 0 else "1")
#             alt2.append("1" if i % 2 == 0 else "0")

#         def diff(A, B):
#             cnt = 0
#             for i in range(n):
#                 cnt += 1 if (A[i] != B[i]) else 0
#             return cnt

#         for i in range(n):
#             newS = s[i:] + s[:i]
#             res = min(res, min(diff(alt1, newS), diff(alt2, newS)))
#         return res


class Solution:
    def minFlips(self, s: str) -> int:
        res = len(s)
        windowsize = len(s)
        s = s + s #line up the string for later
        
        #if string is 1011 then if you move all to the right its 10111011
        alt1 = ""
        alt2 = ""
        #theres only two solutions ti can be eiher 1010101 or 0101010
        
        for i in range(len(s)): #generate the good models
            alt1 += "0" if i % 2 == 0 else "1" #evem
            alt2 += "0" if i % 2 != 0 else "1" #odd

        #since we are moving front to back, were just removing the last element,
        #so have two vairables to keep track of window swaps

        diff1 = 0
        diff2 = 0

        l = 0
        for r in range(len(s)): #remember s is now s + s
            if s[r] != alt1[r]:
                diff1 += 1 #count differences of first string
            if s[r] != alt2[r]:
                diff2 += 1

            if (r-l+1) > windowsize:
                if s[l] != alt1[l]:
                    diff1 -= 1
                if s[l] != alt2[l]:
                    diff2 -= 1
                l += 1
            if (r-l+1) == windowsize:
                res = min(res, diff1, diff2)
                
        return res


