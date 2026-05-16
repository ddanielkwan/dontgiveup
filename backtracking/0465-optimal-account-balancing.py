# You are given an array of transactions transactions where transactions[i] = [fromi, toi, amounti] indicates that the person with ID = fromi gave amounti $ to the person with ID = toi.

# Return the minimum number of transactions required to settle the debt.

 

# Example 1:

# Input: transactions = [[0,1,10],[2,0,5]]
# Output: 2
# Explanation:
# Person #0 gave person #1 $10.
# Person #2 gave person #0 $5.
# Two transactions are needed. One way to settle the debt is person #1 pays person #0 and #2 $5 each.


class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        #from to amount
        # The key insight is:
        # We do NOT care about the original transactions.
        # We only care about each person’s FINAL balance.

        #backtracking
        #step 1 calculate net values
        balance = defaultdict(int)

        for f, t, amt in transactions:
            balance[f] -= amt
            balance[t] += amt

        #we dont care about index, just do values
        debt = [x for x in balance.values() if x != 0]

        def dfs(start):

            # skip settled people
            while start < len(debt) and debt[start] == 0:
                start += 1

            if start == len(debt):
                return 0

            ans = float('inf')

            for i in range(start + 1, len(debt)):

                # opposite signs only
                #it doesnt amtter who gets added
                if debt[start] * debt[i] < 0:

                    # settle start with i
                    debt[i] += debt[start]

                    ans = min(ans, 1 + dfs(start + 1))

                    # backtrack
                    debt[i] -= debt[start]

            return ans

        return dfs(0) #dfs(0) represents the minimum number of transactions to settle all the debts.
        # dfs(1) represents the minimum number of transactions to settle the debts of all people except the firs