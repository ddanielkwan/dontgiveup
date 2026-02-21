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
        
        
        total = sum(skill) #total skills

        # There are n players and n/2 teams
        # if every team has the same total skill:
        # we solve for each team skill sum
        #   (team sum) × (number of teams) = total skill
        #   team_sum × (n / 2) = total
        #   team_sum = (2 × total) / n
        #
        # team_sum MUST be an integer, otherwise it's impossible
        # to divide players into equal-sum teams.
        if (2 * total) % len(skill):
            return -1 
        
        # count how many times each skill value appears
        # WE  "consume" players as we form teams
        count = Counter(skill)

        # we aim for this target for each team/pair
        target = (2 * total) // len(skill)  #number of players

        res = 0  # store total chemistry

        for s in skill:
 #similar to two sum
            # If this skill has already been fully used in previous pairs,
            # skip it — it has already been assigned to a team
            if not count[s]:
                continue
            
            # To form a valid team, we need another player whose skill
            # makes the pair sum to target
            diff = target - s

            # If there is no available player with the required skill,
            # then it's impossible to form valid teams
            if not count[diff]:
                return -1
            
            #valid then 
            # add their chemistry (product of skills)
            res += s * diff

            # remove that player diff and current player s 
            count[s] -= 1
            count[diff] -= 1
        

        return res
