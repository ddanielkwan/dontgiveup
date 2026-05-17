# Write a function to find the longest common prefix string 
# amongst an array of strings.

# If there is no common prefix, return an empty string "".
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

#o(n^2) use simple loops
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        
        longest = ""

        #lets pick the first word in the array to compare
        #it doesn't matter which index to choose to compare as first word because
        #the longest is always limited by the shortest word in the array anyways

        firstWordToCompare = strs[0]

        for index in range(len(firstWordToCompare)):

            for word in strs:
                #if any of the characters don't match just return longest we have so far 
                if index >= len(word) or word[index] != firstWordToCompare[index]:
                    return longest
            
            longest += firstWordToCompare[index]
        
        return longest


