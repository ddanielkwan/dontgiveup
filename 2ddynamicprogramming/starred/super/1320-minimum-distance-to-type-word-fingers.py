
# You have a keyboard layout as shown above in the X-Y plane, where each English uppercase letter is located at some coordinate.

# For example, the letter 'A' is located at coordinate (0, 0), the letter 'B' is located at coordinate (0, 1),
#  the letter 'P' is located at coordinate (2, 3) and the letter 'Z' is located at coordinate (4, 1).
# Given the string word, return the minimum total distance to type such string using only two fingers.

# The distance between coordinates (x1, y1) and (x2, y2) is |x1 - x2| + |y1 - y2|.

# Note that the initial positions of your two fingers are considered free so do not count towards your total distance,
#  also your two fingers do not have to start at the first letter or the first two letters.



class Solution:
    def minimumDistance(self, word: str) -> int:
        #dp 

#         First observation
# At any point in time, you have two fingers on the keyboard. You need to type the next letter — you choose which finger to move.

# Second observation
# After typing letter i, what do you actually need to know to make future decisions?

# Where is finger 1? → always at word[i], you just typed it
# Where is finger 2? → could be anywhere

# So the entire situation is captured by just two things:

# i → how far into the word you are
# other → where the finger that DIDN'T just type is sitting


        #what is state 
        #assume we have way to get (r,c) for letter
        #|x1 - x2| + |y1 - y2|
        def get_pos(c):
            i = ord(c) - ord('A') #returns 0 index of character
            #g is 6 so row 1 , col 1
            return (i // 6, i % 6)

        def dist(a, b):
            r1, c1 = get_pos(a)
            r2, c2 = get_pos(b)
            return abs(r1 - r2) + abs(c1 - c2)

        n = len(word)
        
        # dp[i][other] = min distance to type word[i:] 
        # where one finger is at word[i-1] and other finger is at letter 'other'
#       So a cell like dp[2][3] means:
# Rows = "which letter in the word am I about to type next?"
# Columns = "where is my other finger sitting?"
# "I'm about to type word[2], and my other finger is sitting on D — what's the cheapest way to finish from here?"
#
# We use 26 as a special state meaning:
# "the other finger has not been used yet"
        INF = float('inf')
        dp = [[INF] * 27 for _ in range(n + 1)]

        # base case: finished typing, cost is 0
        for other in range(27):
            dp[n][other] = 0

        # fill backwards
        for i in range(n - 1, 0, -1):
            for other in range(27):
                current = word[i - 1]
                nxt = word[i]

                # option 1: move current finger to nxt
                # In option 1, the current finger moved to type nxt. The other finger didn't move at all — it's still sitting exactly where it was.
# So the "other" finger's position is unchanged, meaning we pass the same other column to dp[i+1].
#               if other means the other finger
#           this means we use current finger not other finger 
                option1 = dist(current, nxt) + dp[i + 1][other]

                # option 2: move other finger to nxt
                # If other == 26, it means the finger hasn't been used yet,
                # so it can move to nxt for free
                if other == 26:
                    move_cost = 0
                else:
                    other_c = chr(other + ord('A'))
                    move_cost = dist(other_c, nxt)

                # Now current becomes the "other" finger (it's sitting idle)
                option2 = move_cost + dp[i + 1][ord(current) - ord('A')]

                dp[i][other] = min(option1, option2)

        # first letter is free
        # initially the other finger is unused
        return dp[1][26]
    

    #o n x 27
    #o n space



