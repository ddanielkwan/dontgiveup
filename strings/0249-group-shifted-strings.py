# Perform the following shift operations on a string:

# Right shift: Replace every letter with the successive letter of the English alphabet, where 'z' is replaced by 'a'. For example, "abc" can be right-shifted to "bcd" or "xyz" can be right-shifted to "yza".
# Left shift: Replace every letter with the preceding letter of the English alphabet, where 'a' is replaced by 'z'. For example, "bcd" can be left-shifted to "abc" or "yza" can be left-shifted to "xyz".
# We can keep shifting the string in both directions to form an endless shifting sequence.

# For example, shift "abc" to form the sequence: ... <-> "abc" <-> "bcd" <-> ... <-> "xyz" <-> "yza" <-> .... <-> "zab" <-> "abc" <-> ...
# You are given an array of strings strings, group together all strings[i] that belong to the same shifting sequence. You may return the answer in any order.

 

# Example 1:

# Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]

# Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]

# Example 2:

# Input: strings = ["a"]

# Output: [["a"]]

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        # right shift - replace every letter with sucessive letter of english alpha
        #ciruclar z -> a e.g abc -> bcd e.g xyz -> yza

        #left shiftbefore #
        #can we use a hashamp to keep track of a "key" this key can be
        #a pattern that all common strings can reach

        #e.g hashmap[abc] = [abc, bcd]

        #how to find common key ?
        #can one key be the difference between each letter?
        #e.g abc -> becomes key 011

        hashmap = defaultdict(list)
        def getKey(string):

            if len(string) == 1:
                return "single"

            key = []

            for i in range(1, len(string)):

                diff = (ord(string[i]) - ord(string[i - 1])) % 26

                key.append(str(diff))

            return ",".join(key)


        for s in strings:
            key = getKey(s)
            hashmap[key].append(s)
        print(hashmap.items())
        return list(hashmap.values())


