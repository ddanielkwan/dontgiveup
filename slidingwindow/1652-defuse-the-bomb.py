# You have a bomb to defuse, and your time is running out! Your informer will provide you with a circular array code of length of n and a key k.

# To decrypt the code, you must replace every number. All the numbers are replaced simultaneously.

# If k > 0, replace the ith number with the sum of the next k numbers.
# If k < 0, replace the ith number with the sum of the previous k numbers.
# If k == 0, replace the ith number with 0.
# As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].

# Given the circular array code and an integer key k, return the decrypted code to defuse the bomb!

 

# Example 1:

# Input: code = [5,7,1,4], k = 3
# Output: [12,10,16,13]
# Explanation: Each number is replaced by the sum of the next 3 numbers. The decrypted code is [7+1+4, 1+4+5, 4+5+7, 5+7+1]. Notice that the numbers wrap around.

class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:

        n = len(code)
        l = 0

        res = [0] * n 

        curr = 0

        for r in range(n + abs(k)): #because circular when last element need to possible k next
            curr += code[r%n]

            if r - l + 1 > abs(k): #window too large
                curr -= code[l%n]
                l = (l+1)%n
            
            if r - l + 1 == abs(k): #window just right
                if k > 0:
                    res[(l-1)%n] = curr #so the left side element is "i" here, so this is the sum of what we calculated
                elif k < 0 :
                    res[(r+1)%n] = curr #right side will be sum before it 
        
        return res

