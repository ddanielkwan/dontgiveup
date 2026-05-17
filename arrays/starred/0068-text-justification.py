# Given an array of strings words and a width maxWidth, 
# format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

# You should pack your words in a greedy approach; that is, pack as many words as you can in each line. 
# Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

# Extra spaces between words should be distributed as evenly as possible. 
# If the number of spaces on a line does not divide evenly between words, 
# the empty slots on the left will be assigned more spaces than the slots on the right.

# For the last line of text, it should be left-justified, and no extra space is inserted between words.

# Note:

# A word is defined as a character sequence consisting of non-space characters only.
# Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
# The input array words contains at least one word.
 

# Example 1:

# Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
# Output:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]
# # 


class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        # You build the text line by line. For each line:
        # 1. Greedily pack as many words as fit.
        # 2. When the next word would overflow, you justify the current line by inserting spaces.
        # 3. The last line is special: it’s left-justified (single spaces, then trailing spaces).

        # were going to keep track of the cumulative length of each line WITHOUT THE SPSCAES
        # we add spaces when we determine that the calculation is over the maxwdidth
    
        lettersCount = 0 #Total number of letters already in the current line , space not counted
        lineWords = [] #["this", "is", "an"] #len(lineWords) - Number of spaces that will be required if we add another word
        res = []

        i = 0
        while i < len(words):
            #if the number of spaces we have to add and amount of letters we currently have, and the next word is greater than maxWidth
            if len(lineWords) + lettersCount + len(words[i]) > maxWidth:
                

                # Step 2. when next word would overflow, we justify the current line by inserting spaces

                # determine the extra spaces we currently have, without the next word, since next word will overflow
                # "this" "is" "an" -> 16 - 8 = 8 spaces
                extra_spaces = maxWidth - lettersCount

                # Distribute the extra spaces 
                # 8 spaces / max(1 mandatory space, 2) = 4 so between each word there must be 4 spaces
                spaces = extra_spaces // max(1, (len(lineWords) - 1)) #minimum 1 because we must have at least one space between words

                #e.g extra_spaces = 7, gaps = 3, problem requires, that extra space, must be distributed from left side to right
                #we have 1 extra space, so that goes to first word first
                remainder = extra_spaces % max(1, (len(lineWords) - 1))

                #case ["hello"] only one word needs space
                for j in range(max(1,len(lineWords)-1)): #we add space behind word so we dont need add space to last word
                    lineWords[j] += " " * spaces

                    if remainder: #remainder we go from left to right, so we just subtract 1
                        remainder -= 1
                        lineWords[j] += " "


                res.append("".join(lineWords))
                
                #reset
                lineWords = [] 
                lettersCount = 0


            lineWords.append(words[i])
            lettersCount += len(words[i])
            i += 1


        #need to handle the last line  
        # this case would only happen if the while loop ends and its not perfectly fitted so it has remaining words
        # Last line -> left-justified
        # 1. exactly one space between words
        # 2. remaining spaces go at the end
        # ""This is last____""
        lastLine = " ".join(lineWords)
        traillingSpaces = maxWidth - len(lastLine)
        res.append(lastLine + " " * traillingSpaces)
        return res


     

