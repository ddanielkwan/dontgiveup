# There are n dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

# After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

# When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

# For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

# You are given a string dominoes representing the initial state where:

# dominoes[i] = 'L', if the ith domino has been pushed to the left,
# dominoes[i] = 'R', if the ith domino has been pushed to the right, and
# dominoes[i] = '.', if the ith domino has not been pushed.
# # Return a string representing the final state.

from collections import deque


#similar to BFS, each iteration handles level
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        
        q = deque()
        dominoes = list(dominoes)

        for i, direction in enumerate(dominoes):
            if direction != ".":
                q.append((i, direction))

        while q :
            index, direction = q.popleft()
            #we do not care about index - 2 because, we added to queue from left to right, so the right will get processed first
            #this will leave all Ls to be valid
            if direction == "L" and index - 1 >= 0 and dominoes[index-1] == ".":
                dominoes[index-1] = "L"
                q.append((index-1, "L"))

            elif direction == "R" and index + 1 < len(dominoes) and dominoes[index+1] == ".":
                if index + 2 < len(dominoes) and dominoes[index+2] == "L":
                    q.popleft() #if index + 2 is also a left, it means it willbe next to process so we must pop and equalize it 
                else:
                    dominoes[index+1] = "R"
                    q.append((index+1, "R"))
        return "".join(dominoes)

