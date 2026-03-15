# Given a string s and an integer k, 
# return the number of substrings in s of length k with no repeated characters.

# Example 1:

# Input: s = "havefunonneetcode", k = 5

# Output: 6
# Explanation:

# There are 6 substrings they are: 'havef','avefu','vefun','efuno','etcod','tcode'.

class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:

        # as for k > 26, there can be no substrings with only unique characters
        if k > 26:
            return 0
        answer = 0
        n = len(s)


        left = right = 0

    
        freq = [0] * 26


        def get_val(ch: str) -> int:
            return ord(ch) - ord("a")

        while right < n:


            freq[get_val(s[right])] += 1

            # If the current character appears more than once in the frequency array
            # keep contracting the window and removing characters from the
            # frequency array till the frequency of the current character becomes 1.
            while freq[get_val(s[right])] > 1:
                freq[get_val(s[left])] -= 1
                left += 1

            # Check if the length of the current unique substring is equal to k
            if right - left + 1 == k:
                answer += 1

                # Contract the window and remove the leftmost character from the
                # frequency array
                freq[get_val(s[left])] -= 1
                left += 1

            right += 1

        return answer