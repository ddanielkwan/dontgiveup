# Given a string num that contains only digits and an integer target, 
# return all possibilities to insert the binary operators '+', '-', and/or '*' between the digits of num so 
# that the resultant expression evaluates to the target value.

# Note that operands in the returned expressions should not contain leading zeros.

# Note that a number can contain multiple digits.

 

# Example 1:

# Input: num = "123", target = 6
# Output: ["1*2*3","1+2+3"]
# Explanation: Both "1*2*3" and "1+2+3" evaluate to 6.
# Example 2:

# Input: num = "232", target = 8
# Output: ["2*3+2","2+3*2"]
# Explanation: Both "2*3+2" and "2+3*2" evaluate to 8.


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        
        #num -> is a string only digits
        #target - int

        #return list of possible places to insert "+" "-" "*" between num
        #so that the expression evaluates to target

        #123 target = 6 
        #backtracking

        # What are my choices? choose next substring number, and what to put before it
        # What state do I need to carry? currrent index, current expression, current value
        # What is the base case? if you used all digits and vvalue evalautes to target
        # How do I undo/backtrack?

        answers = []

        n = len(num)
        def dfs(index, expression, value, prev):
            #base case
            if index == n :
                if value == target:
                    answers.append(expression)
                return

            # Choose the next number, then try every operator
            for j in range(index, n): #e.g 1234, all possible numbers 2, 23, 234..
                #this jsut means if its more than 1 digit, it has not strt with 0
                #this loop goes through all index
                if j > index and num[index] == "0": #digit has to be at least 1 digit, remove leading zero "05" "0003"
                    break
                currStr = num[index:j+1]
                currNum = int(currStr)

                if index == 0:
                    #first case first number cannot ahve anything cant be "+1+2
                    #so just continue
                    dfs(j + 1, currStr, currNum, currNum)
                else:
                    #NOTE: THE PREV IS ALWAYS SIGNED SO NEGATIVE OR POSTIVE
                    #addition, just add value with current
                    dfs(j + 1,
                        expression + "+" + currStr,
                        value + currNum,
                        currNum)
                    #subtracting just do value - current
                    dfs(j + 1,
                        expression + "-" + currStr,
                        value - currNum,
                        -currNum)
                    #multiplication more complicant thats why we needed prev 
                    # handle multiplication precedence
                    # e.g 1 + 2 * 3
                    #if we added 1 + 2 already
                    #we now
                    #so we need to do 1 - +(2*3) 
                    dfs(j + 1, #index
                        expression + "*" + currStr, #expression normal as add and subtract
                        value - prev + (prev * currNum), #value remove previous term
# add multiplied version instead
                        prev * currNum) #prev
                #prev to handle multiplication

        dfs(0, "", 0, 0)
        return answers