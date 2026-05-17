# Given two strings s and t, return true if they are equal when both are typed into empty text editors. 
# '#' means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.

 

# Example 1:

# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        #we can use a stack or two pointers
        #intuition: Backspaces only affect characters before them, so it’s natural to process the strings from right to left.
        sPointer = len(s) - 1
        tPointer = len(t) - 1

        def nextValid(word, index):
            #determine the next index for a character not backspace
            #everytime we see backspace, add to count
            #if its not a backspace and backspace > 0, ignore that character and subtract from backspace count
            #once we get to character and no more backspace, that is valid index
            backspace = 0
            while index >= 0:
                if word[index] == "#":
                    backspace += 1
                elif backspace > 0 :
                    backspace -= 1 #just means were skipping the cahracter andnot doing anything
                else: #we finsihed looking at backspaces
                    break
                
                index -= 1
            return index
        #we need to start backwrads because they are deleting 
        while sPointer >= 0 or tPointer >= 0: #must keep comparing until BOTH strings are fully processed, not stop when one finishes so use OR b
            # becaeuase we eont know if they are equal

        #find next vlid pointer that is not "deleted"
            sPointer = nextValid(s, sPointer)
            tPointer = nextValid(t, tPointer)


            charS = s[sPointer] if sPointer >= 0 else ""
            charT = t[tPointer] if tPointer >= 0 else ""
            #not equal false
            if charS != charT:
                return False

            sPointer -= 1
            tPointer -= 1


        
        return True

