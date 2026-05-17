# On an 2 x 3 board, there are five tiles labeled from 1 to 5, and an empty square represented by 0. A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

# The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

# Given the puzzle board board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1.

 

# Example 1:


# Input: board = [[1,2,3],[4,0,5]]
# Output: 1
# Explanation: Swap the 0 and the 5 in one move.

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # What is the “state”?
        #   the entire board configuration.
        # What transitions are possible from a state?
        #   Swap 0 with one of its 4-directionally adjacent tiles.
        # Is this shortest path / minimum operations?
        #   Yes — minimum number of moves.
        # Are edges weighted equally?
        #   Yes — every swap costs exactly 1 move.
        # Do I need visited states?
        #   Yes — otherwise you revisit the same board configurations infinitely.
      
      #bfs we make so that the nodes, is the puzzle state what does thi smean
      #e.g [1,2,3][4,0,5] -> next nodeposisble cna be [1,0,3][4,2,5]

        adj = { #where they can move
            0: [1,3],
            1: [0,2,4],
            2: [1,5],
            3: [0,4],
            4: [1,3,5],
            5: [4,2]
        }

        # string repreentation of the board in 1d
        b = "".join([str(c) for row in board for c in row])

        q = deque([(b.index("0"),b, 0)]) #index current at, so the 0  iwant to move, currentstateofboard, lengthofcurrentpath
        visit = set([b])
        while q :
            i, b, length = q.popleft()
            if b == "123450":
                return length
            #strings immutable to do swap so use array
            b_arr = list(b)
            for j in adj[i]:
                new_b_arr = b_arr.copy()
                new_b_arr[i],new_b_arr[j] =   new_b_arr[j],new_b_arr[i]
                #take this and conerrt o string
                new_b = "".join(new_b_arr)

                if new_b not in visit:
                    q.append((new_b.index("0"), new_b, length+1))
                    visit.add(new_b)
            
        return -1

            


