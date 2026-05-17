# Given a string s, sort it in decreasing order based on the frequency of the characters. 
# The frequency of a character is the number of times it appears in the string.

# Return the sorted string. If there are multiple answers, return any of them.

 

# Example 1:

# Input: s = "tree"
# Output: "eert"
# Explanation: 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.


from collections import Counter, defaultdict

#USE ARRAY FOR BUCKET SORT
class Solution:
    def frequencySort(self, s: str) -> str:

        #use bucket sort, and then loop to append from the largest count(index)
        counter = Counter(s)
        result = ""

        buckets = defaultdict(list)

        for key, value in counter.items():
            buckets[value].append(key)

        
        for i in range(len(s),0, - 1):
            if i in buckets:
                for item in buckets[i]:
                    result += item * i

        return result



