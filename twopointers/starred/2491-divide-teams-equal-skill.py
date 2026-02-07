# You are given a positive integer array skill of even length n where skill[i] denotes the skill of the ith player. Divide the players into n / 2 teams of size 2 such that the total skill of each team is equal.

# The chemistry of a team is equal to the product of the skills of the players on that team.

# Return the sum of the chemistry of all the teams, or return -1 if there is no way to divide the players into teams such that the total skill of each team is equal.

 

# Example 1:

# Input: skill = [3,2,5,1,3,4]
# Output: 22
# Explanation: 
# Divide the players into the following teams: (1, 5), (2, 4), (3, 3), where each team has a total skill of 6.
# The sum of the chemistry of all the teams is: 1 * 5 + 2 * 4 + 3 * 3 = 5 + 8 + 9 = 22.

from collections import Counter


class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        
        # Sum of all players' skills
        total = sum(skill)

        # There are n players and n/2 teams.
        # If every team has the same total skill:
        #
        #   (team sum) × (number of teams) = total skill
        #   team_sum × (n / 2) = total
        #   team_sum = (2 × total) / n
        #
        # team_sum MUST be an integer, otherwise it's impossible
        # to divide players into equal-sum teams.
        if (2 * total) % len(skill):
            return -1 
        
        # Count how many times each skill value appears
        # This lets us "consume" players as we form teams
        count = Counter(skill)

        # Target sum that every pair of players must equal
        target = (2 * total) // len(skill)

        res = 0  # will store the total chemistry

        # Iterate through the original skill list
        # (not the Counter keys) so every player is considered
        for s in skill:

            # If this skill has already been fully used in previous pairs,
            # skip it — it has already been assigned to a team.
            if not count[s]:
                continue
            
            # To form a valid team, we need another player whose skill
            # makes the pair sum to `target`
            diff = target - s

            # If there is no available player with the required skill,
            # then it's impossible to form valid teams
            if not count[diff]:
                return -1
            
            # Valid pair found:
            # add their chemistry (product of skills)
            res += s * diff

            # Consume one player of each skill so they are not reused
            count[s] -= 1
            count[diff] -= 1
        
        # If all players were successfully paired, return total chemistry
        return res
