# You are given a string s. You can convert s to a palindrome by adding characters in front of it.

# Return the shortest palindrome you can find by performing this transformation.

 

# Example 1:

# Input: s = "aacecaaa"
# Output: "aaacecaaa"
# Example 2:

# Input: s = "abcd"
# Output: "dcbabcd"

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # def palindrome(s):
        #     l = 0
        #     r = len(s) - 1
        #     while l < r :
        #         if s[l] != s[r]:
        #             return False
        #         l += 1
        #         r -= 1
        #     return True
        
        # #go from back to left, and find if the center is palindrome, that means we just need to add the remaining right side to left to make it palindrome
        # for r in range(len(s)-1,-1,-1):
        #     if palindrome(s[0:r+1]): 

        #         suffix = s[r+1:][::-1]
        #         return suffix + s
        


        # Intuition:
        # We want to find the LONGEST prefix of the string that is already a palindrome.
        # If we know that prefix [0..i] is palindromic, then everything AFTER i must be
        # reversed and added to the front to make the whole string a palindrome.

        # Example:
        #   s = "a a c a a b e"
        #        ^       ^
        # Reverse(s) = "e b a a c a a"
        #                  ^       ^
        # The overlapping region that matches tells us the longest palindromic prefix.

        # Key trick:
        # Instead of comparing strings (which costs O(n) each time),
        # we compare rolling HASH VALUES (integers) in O(1).

        # We compute:
        #   prefix hash  -> left to right
        #   suffix hash  -> right to left
        # If they are equal at index i, then s[0:i] is a palindrome.

        # We use base-26 hashing (similar to binary, but for letters a–z)
        # so that character order matters.
        # Example:
        #   "abc" → a*26^2 + b*26^1 + c*26^1

        #hashes
        prefix = 0
        suffix = 0
        base = 26

        power = 1
        last_index = -1


        for i, c in enumerate(s):
            # map character to number: 'a' -> 1, 'b' -> 2, ..., 'z' -> 26
            char = ord(c) - ord('a') + 1

            # build prefix hash: shift previous hash left (multiply by base) and add new character
            #just like now in base 10 we multiple by 10
            prefix = (prefix * base) + char

        #   it is math
        #     The first character comes → we place it at power 26⁰.
        #     The second character comes → we place it at power 26¹.
        #     The third character comes → we place it at power 26².
        #     The fourth character comes → we place it at power 26³.
        #     We ADD each character’s contribution to the total.
        #     We never shift or move earlier characters.

            suffix = suffix + char * power
            power = power * base

            if prefix == suffix:
                last_index = i


        suffix = s[last_index+ 1:]
        return suffix[::-1] + s 
    

