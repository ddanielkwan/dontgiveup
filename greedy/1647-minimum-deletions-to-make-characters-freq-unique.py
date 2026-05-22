# A string s is called good if there are no two different characters in s that have the same frequency.

# Given a string s, return the minimum number of characters you need to delete to make s good.

# The frequency of a character in a string is the number of times it appears in the string. 
# For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.

 

# Example 1:

# Input: s = "aab"
# Output: 0
# Explanation: s is already good.
# Example 2:

# Input: s = "aaabbbcc"
# Output: 2
# Explanation: You can delete two 'b's resulting in the good string "aaabcc".
# Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".


class Solution:
    def minDeletions(self, s: str) -> int:

        #we are getting the counts of freq for all charracters
        #we will keep track ofa "seen frequnecies" set so that if we sawthat freuency before, then we cant use that one
        #we will have to greedily keep decreasing the next count until we havent seen a freq
        #add taht freq to the set 
        counter = Counter(s)

        freq = counter.values()

        seen_frequencies = set()

        deletions = 0

        for count in freq:
            while count > 0 and count in seen_frequencies:
                count -= 1
                deletions += 1
            seen_frequencies.add(count)
        return deletions

