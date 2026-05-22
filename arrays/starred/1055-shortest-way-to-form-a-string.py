# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) 
# of the characters without disturbing the relative positions of the remaining characters.
#  (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

# Given two strings source and target, return the minimum number of subsequences of source such
#  that their concatenation equals target. If the task is impossible, return -1.

 

# Example 1:

# Input: source = "abc", target = "abcbc"
# Output: 2
# Explanation: The target "abcbc" can be formed by "abc" and "bc", which are subsequences of source "abc".

class Solution:
    def shortestWay(self, source: str, target: str) -> int:

            # o(t^2 * s) because
            #each time is scanning issubequence S -> 2S -> 3S -> 4S
        def is_subsequence(target, concatstring):
            i = 0
            j = 0

            while i < len(target) and j < len(concatstring):
                if target[i] == concatstring[j]:
                    i += 1
                j += 1
            return i == len(target)
           

        #brute force, keep adding sources together until it has all of target
        source_chars = set(source)
        #but first we need to ensure that the source we are given is possible to create target
        #so there shouldnt be any character not in target 
        #if we keep adding source it wont matter because we never get that one letter in target
        for char in target:
            if char not in source_chars:
                return -1

        #now keep adding source until it is equals target 
        concatenated_source = source
        count = 1
        while not is_subsequence(target, concatenated_source):
            concatenated_source += source
            count += 1


        return count
    

#o(s*t)
class Solution:
    def shortestWay(self, source: str, target: str) -> int:


        source_chars = set(source)
        for char in target:
            if char not in source_chars:
                return -1

        # Length of source to loop back to start of source using mod
        m = len(source)

        source_iterator = 0

        # Number of times source is traversed. It will be incremented when
        # while finding the occurrence of a character in target, source_iterator
        # reaches the start of source again.
        count = 0


        for char in target:

            # If while finding, iterator reaches start of source again,
            # increment count
            if source_iterator == 0:
                count += 1

            # Find the first occurrence of char in source
            while source[source_iterator] != char:


                source_iterator = (source_iterator + 1) % m
                if source_iterator == 0:
                    count += 1

            # Loop will break when char is found in source. Thus, increment.
            # Don't increment count until it is not clear that target has
            # remaining characters.
            source_iterator = (source_iterator + 1) % m


        return count

