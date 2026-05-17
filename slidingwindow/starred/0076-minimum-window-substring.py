# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

 

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.


from collections import defaultdict


#brute. force

class Solution: #o(n^2 * m)
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT = {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        res, resLen = [-1, -1], float("infinity")
        for i in range(len(s)):
            countS = {}
            for j in range(i, len(s)):
                countS[s[j]] = 1 + countS.get(s[j], 0)

                flag = True
                for c in countT:
                    if countT[c] > countS.get(c, 0):
                        flag = False
                        break

                if flag and (j - i + 1) < resLen:
                    resLen = j - i + 1
                    res = [i, j]

        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""
    
class Solution: #o(n+m)
    def minWindow(self, s: str, t: str) -> str:
        
        if len(t) > len(s):
            return "" #t cannot be greater than s

        
        #step 1 . get the counts of t 

        trackerT = defaultdict(int)
        for char in t:
            trackerT[char] += 1
        
        have = 0
        need = len(trackerT)

        l = 0

        res = [-1, -1]

        resLen = float('inf')
        window = defaultdict(int)

        for r in range(len(s)):
            window[s[r]] += 1

            if s[r] in trackerT and trackerT[s[r]] == window[s[r]]:
                have += 1
            
            while have == need:
                if r - l + 1 < resLen:
                    res = [l, r ]
                    resLen = r - l + 1
                
                charLeft = s[l]
                window[charLeft] -= 1

                if charLeft in trackerT and trackerT[charLeft] > window[charLeft]:
                    have -= 1
                l += 1
        l, r = res 

        return s[l: r + 1]

