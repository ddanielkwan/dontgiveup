# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

 

# Example 1:

# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:

# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".

#sliding window and use hashmap to track total chars of each substring
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:

        #what we can do is similar to a sliding window
        #1. get the goal/anagram pattern that P is
        #2. keep a updating pattern of that window in S
        #3. check if they are equal
        
        trackerP = [0] * 26

        #get the pattern for P
        for char in p:
            key = ord(char) - ord('a')
            trackerP[key] += 1
        
        leftPointer = 0
        trackerS = [0] * 26
        res = []

        #update pattern for S as we go along
        for rightPointer in range(len(s)):
            trackerS[ord(s[rightPointer]) - ord('a')] += 1

            #once the window is too large we want to shrink from left side
            while rightPointer - leftPointer + 1 > len(p):
                trackerS[ord(s[leftPointer])- ord('a')] -= 1
                leftPointer += 1
            
            if trackerS == trackerP:
                res.append(leftPointer)
                
        return res