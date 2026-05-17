# Given the availability time slots arrays slots1 and slots2 of two people and a meeting duration duration, return the earliest time slot that works for both of them and is of duration duration.

# If there is no common time slot that satisfies the requirements, return an empty array.

# The format of a time slot is an array of two elements [start, end] representing an inclusive time range from start to end.

# It is guaranteed that no two availability slots of the same person intersect with each other. That is, for any two time slots [start1, end1] and [start2, end2] of the same person, either start1 > end2 or start2 > end1.

 

# Example 1:

# Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8
# Output: [60,68]

class Solution:
    def minAvailableDuration(
        self,
        slots1,
        slots2,
        duration
    ):
        
        slots1.sort()
        slots2.sort()

        i = j = 0

        while i < len(slots1) and j < len(slots2):

            s1, e1 = slots1[i]
            s2, e2 = slots2[j]

            # overlap
            start = max(s1, s2)
            end = min(e1, e2)

            # enough overlap
            if end - start >= duration:
                return [start, start + duration]

            # move interval that ends earlier
            if e1 < e2:
                i += 1
            else:
                j += 1

        return []

