# We stack glasses in a pyramid, where the first row has 1 glass, the second row has 2 glasses, and so on until the 100th row.  Each glass holds one cup of champagne.

# Then, some champagne is poured into the first glass at the top.  When the topmost glass is full, any excess liquid poured will fall equally to the glass immediately to the left and right of it.  When those glasses become full, any excess champagne will fall equally to the left and right of those glasses, and so on.  (A glass at the bottom row has its excess champagne fall on the floor.)

# For example, after one cup of champagne is poured, the top most glass is full.  After two cups of champagne are poured, the two glasses on the second row are half full.  After three cups of champagne are poured, those two cups become full - there are 3 full glasses total now.  After four cups of champagne are poured, the third row has the middle glass half full, and the two outside glasses are a quarter full, as pictured below.



# Now after pouring some non-negative integer cups of champagne, return how full the jth glass in the ith row is (both i and j are 0-indexed.)

 

# Example 1:

# Input: poured = 1, query_row = 1, query_glass = 1
# Output: 0.00000
# Explanation: We poured 1 cup of champange to the top glass of the tower (which is indexed as (0, 0)). There will be no excess liquid so all the glasses under the top glass will remain empty.


class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        
        #simulation bottom up

        previous_row = [poured] #flow

        for row in range(1, query_row + 1):
            #note that each row is index i and i + 1 for its child
            current_row = [0] * (row+1) # 1 has 2 , row 2 has 3, row 3 has 4

            for i in range(row):
                extra = previous_row[i] - 1 #1 means glasses filled, so thsi is whats left
                if extra > 0 :
                    current_row[i] += 0.5 * extra
                    current_row[i+1] += 0.5 * extra
            previous_row = current_row
        return min(1,previous_row[query_glass])

