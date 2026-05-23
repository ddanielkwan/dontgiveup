# You are painting a fence of n posts with k different colors. You must paint the posts following these rules:

# Every post must be painted exactly one color.
# There cannot be three or more consecutive posts with the same color.
# Given the two integers n and k, return the number of ways you can paint the fence.

 

# Example 1:


# Input: n = 3, k = 2
# Output: 6
# Explanation: All the possibilities are shown.
# Note that painting all the posts red or all the posts green is invalid because there cannot be three posts in a row with the same color.


# class Solution:
#     def numWays(self, n: int, k: int) -> int:
#         #n posts
#         #k different colors

#         #can this be a dynamci programming question?
#         #n posts
#         #k different colors

#         #what is the state here?
#         # - what post we are on
#         # - what color we painted previously (same or differnt)
#         cache = {}
#         def dfs(postNumber, consecutiveCount, prevColor):
#             #what is the base case
#             # if consecutiveCount >= 3:
#             #     return 0
#             if postNumber >= n :
#                 return 1
#             if (postNumber,consecutiveCount,prevColor) in cache:
#                 return cache[(postNumber,consecutiveCount,prevColor)]
#             cache[(postNumber,consecutiveCount,prevColor)] = 0
#             for color in range(k):
#                 if color == prevColor and consecutiveCount < 2:
#                     cache[(postNumber,consecutiveCount,prevColor)] += dfs(postNumber + 1, consecutiveCount + 1, color)
#                 elif color != prevColor:
#                     cache[(postNumber,consecutiveCount,prevColor)] += dfs(postNumber + 1, 1, color) #should not reset to 0

#             return cache[(postNumber,consecutiveCount,prevColor)]

#         return dfs(0, 0, None)


class Solution:
    def numWays(self, n: int, k: int) -> int:
        cache = {}

        def dfs(post, sameStreak):
            if post == n:
                return 1
            if (post, sameStreak) in cache:
                return cache[(post, sameStreak)]

            # Pick a different color from previous: k-1 choices
            #becase if there are k paints, if you dont choose same
            #its k - 1, big brain
            total = (k - 1) * dfs(post + 1, 1)

            # Pick the same color as previous: only 1 choice, only if streak < 2
            if sameStreak < 2:
                total += dfs(post + 1, sameStreak + 1)

            cache[(post, sameStreak)] = total
            return total

        # First post: k choices, all "different" from a fictional previous
        return k * dfs(1, 1)