# Given a string s and a dictionary of strings wordDict,
#  return true if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

# Example 1:

# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# Example 2:

# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.
# Example 3:

# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false



class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Can I find a dictionary word that ENDS at this position, where everything BEFORE it was also valid?"

        # dp = {}
        # words = set(wordDict)
        # def dfs(i):
        #     if i == len(s):
        #         return True
        #     if i in dp:
        #         return dp[i]
            
        #     for end in range(i+1, len(s)+1):
        #         if s[i:end] in words and dfs(end):
        #             dp[i] = True
        #             return True
        #     dp[i] = False
        #     return False
        # return dfs(0)
        dp = {len(s):True}
        for i in range(len(s)-1,-1,-1):
            dp[i] = False
            for word in wordDict:
                if i + len(word) <= len(s) and s[i:i+len(word)] == word:
                    dp[i] = dp[i+len(word)]
                    #because this word is now valid, so its just depending on whetehr we have soemthing later
                if dp[i]:
                    break
        return dp[0]

