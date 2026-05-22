# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

 

# Example 1:

# Input: num1 = "2", num2 = "3"
# Output: "6"
# Example 2:

# Input: num1 = "123", num2 = "456"
# Output: "56088"
 

# Constraints:

# 1 <= num1.length, num2.length <= 200
# num1 and num2 consist of digits only.
# Both num1 and num2 do not contain any leading zero, except the number 0 itself.
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # If either number is 0, answer is immediately 0
        if "0" in [num1, num2]:
            return "0"

        # Maximum digits possible:
        # len(num1) + len(num2)
        # Example:
        # 999 * 999 = 998001 (6 digits)
        res = [0] * (len(num1) + len(num2))

        # Reverse so index 0 becomes ones place
        # "123" -> "321"
        # "45"  -> "54"
        num1, num2 = num1[::-1], num2[::-1]

        # Example:
        # num1 = "321"
        # num2 = "54"
        #
        # Real multiplication:
        #
        #      123
        #   x   45
        #   ------
        #      615   <- 123 * 5
        # +   4920   <- 123 * 40
        #   ------
        #     5535
        #remember this is already reversed
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):

                # multiply current digits
                digit = int(num1[i1]) * int(num2[i2])

                # place into correct position
                #
                # Example:
                # i1=0 (3), i2=0 (5)
                # 3*5 affects ones place -> res[0]
                #
                # i1=0 (3), i2=1 (4)
                # 3*4 affects tens place -> res[1]
                #
                # i1=1 (2), i2=1 (4)
                # 2*4 affects hundreds place -> res[2]
                #
                # so position is i1+i2
                res[i1 + i2] += digit

                # handle carry
                #
                # Example:
                # res[1] = 13
                #
                # keep 3 in current slot
                # carry 1 to next slot
                res[i1 + i2 + 1] += res[i1 + i2] // 10

                # keep only single digit
                res[i1 + i2] = res[i1 + i2] % 10

        # Reverse back to normal order
        # Example:
        # [5,3,5,5,0] -> [0,5,5,3,5]
        res = res[::-1]

        # Remove leading zeros
        # Example:
        # [0,5,5,3,5] -> [5,5,3,5]
        ind = 0
        while ind < len(res) and res[ind] == 0:
            ind += 1

        # Convert digits back into string
        res = map(str, res[ind:])

        return "".join(res)