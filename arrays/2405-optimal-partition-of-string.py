# Given a string s, partition the string into one or more substrings such that the characters in each substring are unique. That is, no letter appears in a single substring more than once.

# Return the minimum number of substrings in such a partition.

# Note that each character should belong to exactly one substring in a partition.

 

# Example 1:

# Input: s = "abacaba"
# Output: 4
# Explanation:
# Two possible partitions are ("a","ba","cab","a") and ("ab","a","ca","ba").
# It can be shown that 4 is the minimum number of substrings needed.




class Solution:
    #intuition : To minimize the number of substrings, each substring should be as long as possible greedy insight.
    #If you end a substring earlier than necessary, you only make future substrings shorter, which can never reduce the total count — it can only increase it.

    #split string if we see duplicate character
    def partitionString(self, s: str) -> int:
        
        res = 0

        seen = set()

        for character in s :
            if character in seen:
                seen.clear()
                res += 1
            seen.add(character)
        
        return res + 1