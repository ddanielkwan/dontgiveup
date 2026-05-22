# You are given a 0-indexed string s that you must perform k replacement operations on.
#  The replacement operations are given as three 0-indexed parallel arrays, indices, sources, and targets, all of length k.

# To complete the ith replacement operation:

# Check if the substring sources[i] occurs at index indices[i] in the original string s.
# If it does not occur, do nothing.
# Otherwise if it does occur, replace that substring with targets[i].
# For example, if s = "abcd", indices[i] = 0, sources[i] = "ab", and targets[i] = "eee", then the result of this replacement will be "eeecd".

# All replacement operations must occur simultaneously, meaning the replacement operations should not affect the indexing of each other.
#  The testcases will be generated such that the replacements will not overlap.

# For example, a testcase with s = "abc", indices = [0, 1], and sources = ["ab","bc"] will not be generated because the "ab" and 
# "bc" replacements overlap.
# Return the resulting string after performing all replacement operations on s.

# A substring is a contiguous sequence of characters in a string.

 

# Example 1:


# Input: s = "abcd", indices = [0, 2], sources = ["a", "cd"], targets = ["eee", "ffff"]
# Output: "eeebffff"
# Explanation:
# "a" occurs at index 0 in s, so we replace it with "eee".
# # "cd" occurs at index 2 in s, so we replace it with "ffff".


class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        
        # go thru indices / sources and check whether it matches in s
        # if it does, then mark it somehow
        toReplace = {} #key is of index s string, where to start replacing : value is index of source (what to replace with)
        for i in range(len(sources)):
            s_idx = indices[i]
            if s[s_idx:s_idx+len(sources[i])] == sources[i]:
                toReplace[s_idx] = i

        res = []
        i = 0
        #we push the words away and that is intentional because we remove and replace
        # go thru each char of s in a while loop
        while i < len(s):
            # if the index is marked, add the target to the res string and increment index by len(sources[i]) elements
            if i in toReplace:
                res.append(targets[toReplace[i]])
                i += len(sources[toReplace[i]])
            else:
                res.append(s[i])
                i += 1

        # return joined string
        return ''.join(res)

