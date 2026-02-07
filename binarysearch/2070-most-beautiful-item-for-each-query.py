# You are given a 2D integer array items where items[i] = [pricei, beautyi] denotes the price and beauty of an item respectively.

# You are also given a 0-indexed integer array queries. For each queries[j], you want to determine the maximum beauty of an item whose price is less than or equal to queries[j]. If no such item exists, then the answer to this query is 0.

# Return an array answer of the same length as queries where answer[j] is the answer to the jth query.

 

# Example 1:

# Input: items = [[1,2],[3,2],[2,4],[5,6],[3,5]], queries = [1,2,3,4,5,6]
# Output: [2,4,5,5,6,6]
# Explanation:
# - For queries[0]=1, [1,2] is the only item which has price <= 1. Hence, the answer for this query is 2.
# - For queries[1]=2, the items which can be considered are [1,2] and [2,4]. 
#   The maximum beauty among them is 4.
# - For queries[2]=3 and queries[3]=4, the items which can be considered are [1,2], [3,2], [2,4], and [3,5].
#   The maximum beauty among them is 5.
# - For queries[4]=5 and queries[5]=6, all items can be considered.
#   Hence, the answer for them is the maximum beauty of all items, i.e., 6.

#o(nlogn) + o(mlogm)
class Solution:
    def maximumBeauty(self, items: list[list[int]], queries: list[int]) -> list[int]:
        # Each item is represented as [price, beauty]
        # For each query, we want the maximum beauty among items
        # whose price is <= the query value

        # STEP 1: Sort items by price (ascending)
        # This allows us to binary search by price later
        items.sort()

        # STEP 2: Preprocess items to build a prefix maximum
        # After this step:
        # items[i][1] will represent the maximum beauty
        # among all items from index 0 to i (inclusive)
        # At every price point, we remember the best beauty we’ve ever seen up to that pric

        maxBeautySoFar = 0
        for i in range(len(items)):
            # Update the running maximum beauty seen so far
            maxBeautySoFar = max(maxBeautySoFar, items[i][1])

            # Overwrite the beauty at index i with the prefix maximum
            items[i][1] = maxBeautySoFar


        answer = []

        # STEP 3: Process each query independently
        # For each query, we binary search for the rightmost
        # item whose price is <= query
       
        for query in queries:

            l = 0
            r = len(items) - 1

            res = 0


            while l <= r:

                m = l + (r - l) // 2


                if items[m][0] <= query:
                    # This is a valid candidate
                    # Because of prefix max preprocessing,
                    # items[m][1] already contains the best beauty up to m
                    res = items[m][1]

                    # Try to find a higher-priced (but still affordable) item
                    l = m + 1
                else:
                    # Price too large, discard the right half
                    r = m - 1


            answer.append(res)


        return answer
