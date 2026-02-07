# You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.

# You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.

# Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.

 

# Example 1:

# Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
# Output: [4,0,3]
# Explanation:
# - 0th spell: 5 * [1,2,3,4,5] = [5,10,15,20,25]. 4 pairs are successful.
# - 1st spell: 1 * [1,2,3,4,5] = [1,2,3,4,5]. 0 pairs are successful.
# - 2nd spell: 3 * [1,2,3,4,5] = [3,6,9,12,15]. 3 pairs are successful.
# Thus, [4,0,3] is returned.


class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        
        potions.sort()
        potionsLength = len(potions)


        pairs = []

        for spell in spells:

            l = 0
            r = len(potions) - 1

            while l <= r :

                m = l + (r-l)//2

                if potions[m] * spell >= success:

                    r = m - 1
                else:
                    l = m + 1
            #l ends up pointing at the first successful potion index, itll keep moving, if not then itll be potionlength
            pairs.append(potionsLength - l)

        
        return pairs


