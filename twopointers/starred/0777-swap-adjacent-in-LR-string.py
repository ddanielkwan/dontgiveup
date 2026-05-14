# # In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move consists of either replacing one occurrence of "XL" with "LX", or replacing one occurrence of "RX" with "XR". Given the starting string start and the ending string result, return True if and only if there exists a sequence of moves to transform start to result.

 

# Example 1:

# Input: start = "RXXLRXRXL", result = "XRLXXRRLX"
# Output: true
# Explanation: We can transform start to result following these steps:
# RXXLRXRXL ->
# XRXLRXRXL ->
# XRLXRXRXL ->
# XRLXXRRXL ->
# XRLXXRRLX


class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        #what is a property
        #intution: L can only move L, R can only move R
        #L and R can neve r pass through each other
        #L can never go to right of its position
        # If you remove all the Xs, the order of L and R must stay identical
        # start  = RXXLRXRXL
        # result = XRLXXRRLX
        # true
     #start  -> RLLR
        # result -> LRLR not possible

        #two pointers
        n = len(start)

        i = j = 0
        if start.replace("X", "") != result.replace("X", ""):
            return False
        while (i < n and j < n ):
            while i < n and start[i] == 'X':
                i += 1
            while j < n and result[j] == 'X':
                j += 1
            
            #i and j are indices representing next occurence of non x
            if i == n or j == n :
                return i == n and j == n 
            
            if start[i] != result[j]:
                return False
                # L started LEFT of where it needs to end up
            # Example: start:   L...index    0 result:  ..L.
            # # index    2
            if start[i] == 'L' and i < j:
                return False
            if start[i] == 'R' and i > j :
                return False
            
            i += 1
            j += 1
        
        return True
