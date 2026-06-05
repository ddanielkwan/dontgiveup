# Given an array of integers citations where citations[i] is the number of citations a researcher 
# received for their ith paper, return the researcher's h-index.

# According to the definition of h-index on Wikipedia: 
# The h-index is defined as the maximum value of h such that the given researcher has 
# published at least h papers that have each been cited at least h times.

 

# Example 1:

# Input: citations = [3,0,6,1,5]
# Output: 3
# Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
# Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
# Example 2:

# Input: citations = [1,3,1]
# Output: 1


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        #we want h papers
        #such that all h papers have at least h citations

        citations.sort(reverse=True)

        #intutition: if we sort in reverse order
        #then we check
        #does first one have at least 1 citation,
        #does second have at least two
        # does thrid have at least 3
        maxH = 0
        for h in range(len(citations)):
            if h+1 <= citations[h]:
                maxH = h+1
        # Find the largest h such that at least h papers have ≥ h citations.
        # if the 3rd paper has at least 3 citations,
# then the first two definitely do too
        return maxH
