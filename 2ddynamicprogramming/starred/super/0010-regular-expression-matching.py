# # Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.
# Return a boolean indicating whether the matching covers the entire input string (not partial).

 

# Example 1:

# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# Example 2:

# Input: s = "aa", p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        #memo it
        cache = {}
        def dfs(i, j):
            if j == n: #if we reached end of pattern
                return i == m #we must match s
            if (i,j) in cache:
                return cache[(i,j)]
            
            #first of all, check if i is out of bounds
            #if it is not, and characters are same or pj is . means we can match one cahracter
            match = i < m and (s[i] == p[j] or p[j] == ".") 

            #if pattern in bounds and the next element in pattern is *
            #that means the current character e.g a* we can do aaa or aa

            if (j+1) < n and p[j+1] == "*":

                #dfs(i, j + 2) is skip the pattern so a*bbb vs bbb
                #option 2 use match and dfs(i + 1, j) only wrks if curent cahracter matches
                #you can still keep j bcause *
                #return dont include matchall OR include matchall and checknext char to see if match            
                cache[(i, j)] = (dfs(i, j +2 ) or (match and dfs(i+1, j)))
                return cache[(i, j)]

            if match:
                #default cause both match, just increment 
                cache[(i, j)] = dfs(i+1,j+1)
                return cache[(i, j)]

            cache[(i, j)] = False
            return False
        return dfs(0,0)
