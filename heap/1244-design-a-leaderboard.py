# Design a Leaderboard class, which has 3 functions:

# addScore(playerId, score): Update the leaderboard by adding score to the given player's score.
# If there is no player with such id in the leaderboard, add him to the leaderboard with the given score.
# top(K): Return the score sum of the top K players.
# reset(playerId): Reset the score of the player with the given id to 0 (in other words erase it from the leaderboard). 
# It is guaranteed that the player was added to the leaderboard before calling this function.
# Initially, the leaderboard is empty.

 


from sortedcontainers import SortedList

class Leaderboard:
    def __init__(self):
        self.scores = {}
        self.sorted_scores = SortedList()

    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.scores:
            self.sorted_scores.remove(self.scores[playerId])  # O(log n)
        self.scores[playerId] = self.scores.get(playerId, 0) + score
        self.sorted_scores.add(self.scores[playerId])         # O(log n)

    def top(self, K: int) -> int:
        return sum(self.sorted_scores[-K:])                   # O(K)
# sorted_scores[-3:] = [5, 7, 9]  ← the top 3
    def reset(self, playerId: int) -> None:
        self.sorted_scores.remove(self.scores[playerId])      # O(log n)
        self.scores[playerId] = 0
        self.sorted_scores.add(0)                             # O(log n)

        
import heapq
class Leaderboard:

    def __init__(self):
        self.scores = {}

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.scores:
            self.scores[playerId] = 0
        self.scores[playerId] += score

    def top(self, K: int) -> int:

        heap = []  
        # O(1)

        for val in self.scores.values():  
            # loops n times

            heapq.heappush(heap, val)  
            # O(log K)
            # NOT log n because heap size is kept <= K+1

            if len(heap) > K:  
                # O(1)
                heapq.heappop(heap)  
                # O(log K)

        res = 0  
        # O(1)

        while heap:  
            # runs K times at most
            res += heapq.heappop(heap)  
            # each pop is O(log K)

        return res  
        # O(1)



    def reset(self, playerId: int) -> None:
        self.scores[playerId] = 0

