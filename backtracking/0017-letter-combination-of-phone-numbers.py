
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        numToLetters = {
            "2": "abc",
            "3" : "def",
            "4" :"ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" :"pqrs",
            "8" : "tuv",
            "9":"wxyz"
        }

        results = []
        
        if not digits:
            return results
        
        def dfs(index, path):
            if index == len(digits):
                results.append(path[:])
                return
            for char in numToLetters[digits[index]]:
                dfs(index+1, path + char)
        
        dfs(0, "")
        return results
    


    # Time Complexity: O(4ⁿ · n)

