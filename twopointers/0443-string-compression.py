# Given an array of characters chars, compress it using the following algorithm:

# Begin with an empty string s. For each group of consecutive repeating characters in chars:

# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, 
# but instead, be stored in the input character array chars. 
# Note that group lengths that are 10 or longer will be split into multiple characters in chars.

# After you are done modifying the input array, return the new length of the array.

# You must write an algorithm that uses only constant extra space.

# Note: The characters in the array beyond the returned length do not matter and should be ignored.

 

# Example 1:

# Input: chars = ["a","a","b","b","c","c","c"]
# Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
# Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".


class Solution:
    def compress(self, chars: list[str]) -> int:
        
        # Because you have two different jobs happening at the same time:
        # Reading the original data
        # Writing the transformed (compressed) data
        
        insertPointer = 0
        count = 1

        for i in range(1, len(chars)):
            # if same as previous keep counting
            if chars[i] == chars[i - 1]:
                count += 1
            
            # character changed -> write previous group
            else:
                chars[insertPointer] = chars[i - 1] #the previous group char
                insertPointer += 1

                # write count only if > 1
                if count > 1:
                    for digit in str(count): #count can be more than 1 digit .e.g 10 or 11 or 123
                        chars[insertPointer] = digit
                        insertPointer += 1

                count = 1  # reset for new character

        # handle the last group, the last group never triggers a change, so it never gets written
        chars[insertPointer] = chars[-1] #last group
        insertPointer += 1

        if count > 1:
            for digit in str(count):
                chars[insertPointer] = digit
                insertPointer += 1

        return insertPointer

