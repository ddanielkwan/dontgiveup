# You are playing a game that contains multiple characters, and each of the characters has two main properties: attack and defense. You are given a 2D integer array properties where properties[i] = [attacki, defensei] represents the properties of the ith character in the game.

# A character is said to be weak if any other character has both attack and defense levels strictly greater than this character's attack and defense levels. More formally, a character i is said to be weak if there exists another character j where attackj > attacki and defensej > defensei.

# Return the number of weak characters.

 

# Example 1:

# Input: properties = [[5,5],[6,3],[3,6]]
# Output: 0
# Explanation: No character has strictly greater attack and defense than the other.
# Example 2:

# Input: properties = [[2,2],[3,3]]
# Output: 1
# Explanation: The first character is weak because the second character has a strictly greater attack and defense.


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        
        #weak if anybody else has attack and defense > than properties[i] attack and defense

        #this is so big brain and unituitive

        #sort by descending attack
        #sort second by ascendind defnse

        # properties = [[7,9], [5,3], [5,10], [5,7], [3,2]]

        #everything left of it we know has higher attack
        #we jsut keep track of max defnse

        properties.sort(key = lambda x:(-x[0], x[1]))

        max_def = 0
        count = 0
        for attack, defense in properties:
            if defense < max_def:
                count += 1
            else:
                max_def = defense
        
        return count