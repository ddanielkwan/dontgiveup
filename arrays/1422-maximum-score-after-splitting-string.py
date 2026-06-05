# Given a string s of zeros and ones, 
# return the maximum score after splitting the 
# string into two non-empty substrings (i.e. left substring and right substring).

# The score after splitting a string is the number 
# of zeros in the left substring plus the number of ones in the right substring.

 

# Example 1:

# Input: s = "0 11101"
# Output: 5 
# Explanation: 
# All possible ways of splitting s into two non-empty substrings are:
# left = "0" and right = "11101", score = 1 + 4 = 5 
# left = "01" and right = "1101", score = 1 + 3 = 4 
# left = "011" and right = "101", score = 1 + 2 = 3 
# left = "0111" and right = "01", score = 1 + 1 = 2 
# left = "01110" and right = "1", score = 2 + 1 = 3


class Solution:
    def maxScore(self, s: str) -> int:
        #intution , can we get total number of 1s and at every index we calculate the score
        #we first update the ones and zeroes accordingly, since we are splitting at every index, if we see 0 ones +=1 else ones -=1
        ones = s.count("1")

        zeroes = 0

        result = 0

        for i in range(len(s)-1): #cannot count last index  011101| 
            if s[i] == "0":
                zeroes += 1
            else : #"0 11101" we are substracting ones because its like splitting, this is similar to pivot index
                ones -= 1
            result = max(ones + zeroes, result)
        return result


