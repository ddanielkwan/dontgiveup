# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

# Example 1:

# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Example 2:

# Input: s = "Mr Ding"
# Output: "rM gniD"



class Solution:
    def reverseWords(self, s: str) -> str:
        
        def swap(word):
            res = list(word)
            l = 0
            r = len(word) - 1

            while l < r :
                res[l], res[r] = res[r], res[l]
                l += 1
                r -= 1

            return "".join(res)
        
        words = s.split(" ")
        res = []
        for word in words:
            res.append(swap(word))

        return " ".join(res)

