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