# There are n people standing in a queue, and they numbered from 0 to n - 1 in left to right order. 
# You are given an array heights of distinct integers where heights[i] represents the height of the ith person.

# A person can see another person to their right in the queue if everybody in between is shorter than both of them.
#  More formally, the ith person can see the jth person if i < j and 
# min(heights[i], heights[j]) > max(heights[i+1], heights[i+2], ..., heights[j-1]).

# Return an array answer of length n where answer[i] is the number of people the ith person can see to their right in the queue.

 

# Example 1:



# Input: heights = [10,6,8,5,11,9]
# Output: [3,1,2,1,1,0]
# Explanation:
# Person 0 can see person 1, 2, and 4.
# Person 1 can see person 2.
# Person 2 can see person 3 and 4.
# Person 3 can see person 4.
# Person 4 can see person 5.
# Person 5 can see no one since nobody is to the right of them.


# class Solution:
#     def canSeePersonsCount(self, heights: List[int]) -> List[int]:
#         #brute force
#         #for each person
#         #track what is maximum height seen so far to their right

#         ans = [0] * len(heights)

#         for i in range(len(heights)):
#             maxseen = 0
#             cnt = 0

#             for j in range(i+1, len(heights)):
#                 if min(heights[i], heights[j]) > maxseen:
#                     cnt += 1
#                 maxseen = max(maxseen, heights[j])
#             ans[i] = cnt
#         return ans


class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        #intution ach person only cares about the first taller/equal person to their righ
        res = [0] * n
        stack = []
        # Each person looks to the right and can see people until someone taller/equal blocks the view
        # The stack stores indices of people whose answers we haven't fully finished yet
        #decraesking stack
        for i, h in enumerate(heights):
            #if current person is talelr, then shorter people in the stack can see this person
            # h is current
            #if everybody in between is shorter, then you cna see person on right
            #that why we use decreasing stack
            #e.g 7,2,1 and now 4, imagine if 2 can see 4 because 1 is less thna 4 
            while stack and heights[stack[-1]] < h:
                res[stack.pop()] += 1
            if stack: #after removing all short people, the remaining top is first tallest person or equal on left can also see current
                res[stack[-1]] += 1
            stack.append(i)

        return res

