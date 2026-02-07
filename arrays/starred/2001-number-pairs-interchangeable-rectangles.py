# You are given n rectangles represented by a 0-indexed 2D integer array rectangles, where rectangles[i] = [widthi, heighti] denotes the width and height of the ith rectangle.

# Two rectangles i and j (i < j) are considered interchangeable if they have the same width-to-height ratio. More formally, two rectangles are interchangeable if widthi/heighti == widthj/heightj (using decimal division, not integer division).

# Return the number of pairs of interchangeable rectangles in rectangles.


from collections import defaultdict


class Solution:
    def interchangeableRectangles(self, rectangles: list[list[int]]) -> int:
        rectangles = defaultdict(int)
        res = 0

        #same width to height ratio
        for weight, height in rectangles:

            key = weight / height

            res += rectangles[key]
            
            rectangles[key] += 1

        
        return res
        