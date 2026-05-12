# You are given an m x n grid where each cell contains one of the values 0, 1, or 2. You are also given an integer k.

# You start from the top-left corner (0, 0) and want to reach the bottom-right corner (m - 1, n - 1) by moving only right or down.

# Each cell contributes a specific score and incurs an associated cost, according to their cell values:

# 0: adds 0 to your score and costs 0.
# 1: adds 1 to your score and costs 1.
# 2: adds 2 to your score and costs 1. ​​​​​​​
# Return the maximum score achievable without exceeding a total cost of k, or -1 if no valid path exists.

# Note: If you reach the last cell but the total cost exceeds k, the path is invalid.

 

# Example 1:

# Input: grid = [[0, 1],[2, 0]], k = 1

# Output: 2

# Explanation:​​​​​​​

# The optimal path is:

# Cell	grid[i][j]	Score	Total
# Score	Cost	Total
# Cost
# (0, 0)	0	0	0	0	0
# (1, 0)	2	2	2	1	1
# (1, 1)	0	0	2	0	1
# Thus, the maximum possible score is 2.


class Solution:
    def maxPathScore(self, grid, k):

        m = len(grid)
        n = len(grid[0])

        # helper function:
        # determines how much COST a cell adds
        def get_cost(val):
            if val == 0:
                return 0
            return 1

        # NEG means:
        # "this state is impossible / unreachable"
        # we use -1 because score can never be negative
        NEG = -1

        # 3D DP
        #
        # dp[r][c][used]
        #
        # meaning:
        #
        # "maximum score possible when we arrive at
        # cell (r,c) having used exactly 'used' cost"
        #
        # dimensions:
        #
        # m rows
        # n cols
        # k+1 possible costs (0 to k)
        #
        # initialize everything to NEG (unreachable)
        dp = [[[NEG] * (k + 1) for _ in range(n)] for _ in range(m)]


        start_val = grid[0][0]
        start_cost = get_cost(start_val)

        # if even the starting cell already exceeds budget
        # then impossible immediately
        if start_cost > k:
            return -1

        # initialize starting state
        #
        # we are at (0,0)
        # we used start_cost
        # our score is start_val
        dp[0][0][start_cost] = start_val

        for r in range(m):
            for c in range(n):
                cell_val = grid[r][c]
                cell_cost = get_cost(cell_val)

                # skip start cell
                if r == 0 and c == 0:
                    continue

                # try every possible total cost amount
                #
                # IMPORTANT:
                #
                # if current cell itself costs 1,
                # then total used cost must be at least 1
                #
                # example:
                # cannot arrive here with used=0
                # if this cell costs 1
                for used in range(cell_cost, k + 1):

                    # best score for this state
                    #
                    # initialize impossible
                    best = NEG

                    # =========================
                    # OPTION 1: come from TOP
                    # =========================
                    #
                    # previous cell:
                    # (r-1, c)

                    # make sure top cell exists
                    if r > 0:

                        # before entering current cell,
                        # previous used cost would've been:
                        #
                        # used - cell_cost
                        #
                        # because current cell adds cell_cost
                        prev_used = used - cell_cost

                        # check if previous state was reachable
                        if dp[r - 1][c][prev_used] != NEG:

                            # score if we come from top:
                            #
                            # previous score
                            # + current cell value
                            candidate = (
                                dp[r - 1][c][prev_used]
                                + cell_val
                            )

                            # keep better answer
                            best = max(best, candidate)

                    # ==========================
                    # OPTION 2: come from LEFT
                    # ==========================
                    #
                    # previous cell:
                    # (r, c-1)

                    # make sure left cell exists
                    if c > 0:

                        # previous used cost
                        prev_used = used - cell_cost

                        # check reachable
                        if dp[r][c - 1][prev_used] != NEG:

                            # score if coming from left
                            candidate = (
                                dp[r][c - 1][prev_used]
                                + cell_val
                            )

                            # keep better answer
                            best = max(best, candidate)

                    # store final best answer
                    # for this state
                    dp[r][c][used] = best

        # at destination:
        # bottom-right corner
        #
        # we can finish using ANY cost <= k
        #
        # so take best among all costs
        ans = max(dp[m - 1][n - 1])

        # if still NEG,
        # then destination unreachable
        if ans == NEG:
            return -1

        return ans