# The beauty of a string is the difference in frequencies between the most frequent and least frequent characters.

# For example, the beauty of "abaacc" is 3 - 1 = 2.
# Given a string s, return the sum of beauty of all of its substrings.

 

# Example 1:

# Input: s = "aabcb"
# Output: 5
# Explanation: The substrings with non-zero beauty are ["aab","aabc","aabcb","abcb","bcb"], each with beauty equal to 1.
# Example 2:

# Input: s = "aabcbaa"
# Output: 17

class Solution:
    def beautySum(self, s: str) -> int:
        #how mny substrings in abcd, must look thtrough all
        # a
        # ab
        # abc
        # abcd
        # b
        # bc
        # bcd
        # c
        # cd
        # d

        #algorithm

        #we will have to go through all substrings anyways
        #abcd
        #a, ab , abc, abcd
        #b, bc, bcd
        #c, cd
        #d

        # there will be two for loops, this wont be a window , instead we can keep track of tracker array since 26 elements
        #add freqnecy each time, and perofrm max and min of each substring, this is constant time

        

        ans = 0 
        for i in range(len(s)):
            freq = [0] * 26
            for j in range(i, len(s)): #these two for loops makes all substrigns
                #instead of calcualting frequency each time
                #justadd 1 to the new character
                freq[ord(s[j]) - ord('a')] += 1
                #the substring only grows
                non_zero = [x for x in freq if x]

                ans += max(non_zero) - min(non_zero) #<- #scanning 26 only
        return ans

        #o(26n^2)

