# You start with an initial power of power, an initial score of 0, 
# and a bag of tokens given as an integer array tokens, where each tokens[i] denotes the value of tokeni.

# Your goal is to maximize the total score by strategically playing these tokens. 
# In one move, you can play an unplayed token in one of the two ways (but not both for the same token):

# Face-up: If your current power is at least tokens[i], you may play tokeni, losing tokens[i] power and gaining 1 score.
# Face-down: If your current score is at least 1, you may play tokeni, gaining tokens[i] power and losing 1 score.
# Return the maximum possible score you can achieve after playing any number of tokens.

 

# Example 1:

# Input: tokens = [100], power = 50

# Output: 0

# Explanation: Since your score is 0 initially, you cannot play the token face-down. You also cannot play it face-up since your power (50) is less than tokens[0] (100).

# Example 2:

# Input: tokens = [200,100], power = 150

# Output: 1

# Explanation: Play token1 (100) face-up, reducing your power to 50 and increasing your score to 1.

# There is no need to play token0, since you cannot play it face-up to add to your score. The maximum score achievable is 1.


class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        # The intuition is very similar to "spend cheap things to gain points, sell expensive things to regain power"
        # Greedy idea:
        # - Use the cheapest tokens (smallest values) face-up to gain score
        # - If stuck, use the most expensive token face-down to regain power
        # - Goal is to maximize score, not power

        # Sort tokens so we can access cheapest and most expensive easily
        tokens.sort()

        score = 0       
        maxScore = 0    

        l = 0              # pointer to smallest unused token (cheapest)
        r = len(tokens) - 1  # pointer to largest unused token (most power gain)

        # Continue while there are still tokens to consider
        while l <= r:
            # Case 1: We can afford to play the cheapest token face-up
            # This is always the best move because it costs the least power
            # and increases our score.
            if tokens[l] <= power:
                power -= tokens[l]   # spend power
                l += 1               # mark token as used
                score += 1           # gain score
                maxScore = max(maxScore, score)

            # Case 2: We cannot afford a face-up play, but we have score to spend
            # Trade 1 score for power by playing the most expensive token face-down.
            # This gives us the maximum power boost for minimal score loss.
            elif score > 0:
                power += tokens[r]   # gain power
                score -= 1           # lose score
                r -= 1               # mark token as used

            # Case 3: No valid moves left (no power, no score)
            # We are stuck and must stop.
            else:
                break

        return maxScore

