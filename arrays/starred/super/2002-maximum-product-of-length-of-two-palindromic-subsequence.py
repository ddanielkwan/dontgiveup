# Given a string s, find two disjoint palindromic subsequences of s such that the product of their lengths is maximized. 
# The two subsequences are disjoint if they do not both pick a character at the same index.

# Return the maximum possible product of the lengths of the two palindromic subsequences.

# A subsequence is a string that can be derived from another string by deleting some or no characters without 
# changing the order of the remaining characters. A string is palindromic if it reads the same forward and backward.

# Input: s = "leetcodecom"
# Output: 9
# Explanation: An optimal solution is to choose "ete" for the 1st subsequence and "cdc" for the 2nd subsequence.
# The product of their lengths is: 3 * 3 = 9.


class Solution:
    def maxProduct(self, s: str) -> int:
        
        #The product len(s1) * len(s2) is maximized

        # Key insight: Every character has 3 choices
        #     At each index, a character can go to:
        #     1. Neither subsequence
        #     2. First subsequence (currents1)
        #     3. Second subsequence (currents2)
        #     That’s the core intuition behind the backtracking.

        def palindrome(s):
            l = 0
            r = len(s) - 1
            while l < r :
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        

        res = 0
        def backtrack(index,currents1, currents2):
            #O(3^n)
            nonlocal res

            #we only check palindrome at the end because non palindromic prefix can turn to palindromic later
            #brute force is to go through all possible options of strings
            if index == len(s):
                if palindrome(currents1) and palindrome(currents2):
                    res = max(res, len(currents1)*len(currents2))
                return
            
            
            backtrack(index+1, currents1, currents2) #ignore it
            backtrack(index+1, currents1 + s[index], currents2) #put it into first string
            backtrack(index+1, currents1, currents2+s[index]) #put it into second string

        backtrack(0,"","")

        return res

        # https://www.youtube.com/watch?v=aoHbYlO8vDg&t=181s
        # n = len(s)
        # palindromes = {} #bitmask to length
        
        # for mask in range(1, 1<<n):
        #     #bit shift means 00000000000 when shifted it means 00000000001 00000000011 ... so on it tries every combination
        #     subseq = ""
        #     for i in range(n):
        #         #going though every posiitoni n bitmask because htats size of string
        #         #we are going through every index of the bitmask
        #         #recall that the bitmask will represent our string
        #         #since we are going through every combination of bit mask liek 00000010101
        #         #we determine if that posotion at that bitmask is 1 or not, means that combination we include that subseq in the string
        #         if mask  & (1 << i): #and operator 1 and 0 = 0  but 1 and 1 = 1
        #             subseq += s[i]
        #             #convert mask to srting
        #     if subseq == subseq[::-1]: #is palindrome
        #         palindromes[mask] = len(subseq)
        # res = 0
        # #
        # for m1 in palindromes:
        #     for m2 in palindromes:
        #         if m1 & m2 == 0:#if they are disjoint
        #             res = max(res,palindromes[m1]*palindromes[m2])
        # return res


        # # for i in range(5):
        # #     print(1 << 2)
        # #     print(1 << 8)

