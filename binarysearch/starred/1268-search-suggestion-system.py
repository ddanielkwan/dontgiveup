# You are given an array of strings products and a string searchWord.

# Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

# Return a list of lists of the suggested products after each character of searchWord is typed.

 

# Example 1:

# Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
# Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]
# Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"].
# After typing m and mo all products match and we show user ["mobile","moneypot","monitor"].
# After typing mou, mous and mouse the system suggests ["mouse","mousepad"].


class Solution:
    def suggestedProducts(self, products: list[str], searchWord: str) -> list[list[str]]:
        #find most common for all index
        products.sort()
        #want to sort alphabetical and do binarysearch
        #similar words are close togethjer
        #mouse , mousepad
        allCommonWords = []

        l = 0
        r = len(products) - 1

        #go character by character
        #for these list of words, find all words that have matching prefix so we can leave left pointer/rightpointer etc..
        #every item in range is valid
        for i in range(len(searchWord)):
            character = searchWord[i]

            #if the word at left pointer is shorter than index, skip
            #if the character of word[l] at index i is not equal to character, skip
            while l <= r and (len(products[l]) <= i or products[l][i] != character):
                l += 1
            while l <= r and (len(products[r]) <= i or products[r][i] != character):
                r -= 1
            
            #find common at all index
            allCommonWords.append([])
            remain = r - l + 1
            for j in range(min(3, remain)):
                allCommonWords[-1].append(products[l+j])
            
        return allCommonWords
            

            

            

