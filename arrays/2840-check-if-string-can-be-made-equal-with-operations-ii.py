# You are given two strings s1 and s2, both of length n, 
# consisting of lowercase English letters.

# You can apply the following operation on any of the two strings any number of times:

# Choose any two indices i and j such that i < j and the difference j - i is even,
#  then swap the two characters at those indices in the string.
# Return true if you can make the strings s1 and s2 equal, and false otherwise.

 

# Example 1:

# Input: s1 = "abcdba", s2 = "cabdab"
# Output: true
# Explanation: We can apply the following operations on s1:
# - Choose the indices i = 0, j = 2. The resulting string is s1 = "cbadba".
# - Choose the indices i = 2, j = 4. The resulting string is s1 = "cbbdaa".
# # - Choose the indices i = 1, j = 5. The resulting string is s1 = "cabdab" = s2.

class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        # You can only swap characters with the SAME parity index.

        # even indices can only swap with even indices
# odd indices can only swap with odd indices
# Do both strings have same EVEN-index characters?
# Do both strings have same odd-index characters?
        return Counter(s1[::2]) == Counter(s2[::2]) and Counter(
            s1[1::2]
        ) == Counter(s2[1::2])

