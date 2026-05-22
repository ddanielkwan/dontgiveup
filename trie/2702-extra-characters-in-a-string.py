# You are given a 0-indexed string s and a dictionary of words dictionary. You have to break s into one or more non-overlapping substrings such that each substring is present in dictionary. There may be some extra characters in s which are not present in any of the substrings.

# Return the minimum number of extra characters left over if you break up s optimally.

 

# Example 1:

# Input: s = "leetscode", dictionary = ["leet","code","leetcode"]
# Output: 1
# Explanation: We can break s in two substrings: "leet" from index 0 to 3 and "code" from index 5 to 8. There is only 1 unused character (at index 4), so we return 1.

# Example 2:

# Input: s = "sayhelloworld", dictionary = ["hello","world"]
# Output: 3
# Explanation: We can break s in two substrings: "hello" from index 3 to 7 and "world" from index 8 to 12. The characters at indices 0, 1, 2 are not used in any substring and thus are considered as extra characters. Hence, we return 3.


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        #what the fuck
        #dynamic programming
        #have one pointer
        #tracking the word 
        #check wehther that subword is within dict
        #and create a branch, update teh res if the branch is min than result
        #memo
        #account for skip caes first

        #we must have two decisions, skip or not skip because
        #abcdefg > [abc, bcdefg] if we dont skip a we will get result 3
        dictionary = set(dictionary)
        cache = {}
        def dfs(i):
            if i == len(s):
                return 0
            if i in cache:
                return cache[i]
            
            #option 1 : Skip this character #go to next
            #e.g abcd try ab 
            res = 1 + dfs(i +1) #skip this char
            #
            #option 2 : is abc in dictionary
            for j in range(i, len(s)):
                if s[i:j+1] in dictionary: #it is in dictionary so go to next one
                    res = min(res,dfs(j+1))#start at next index of the word after
            
            cache[i] = res
            return res
        return dfs(0)