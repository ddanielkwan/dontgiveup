# You are given two string arrays username and website and an integer array timestamp. 
# All the given arrays are of the same length and the tuple [username[i], website[i], timestamp[i]] indicates that the user username[i] 
# visited the website website[i] at time timestamp[i].

# A pattern is a list of three websites (not necessarily distinct).

# For example, ["home", "away", "love"], ["leetcode", "love", "leetcode"], and ["luffy", "luffy", "luffy"] are all patterns.
# The score of a pattern is the number of users that visited all the websites in the pattern in the same order they appeared in the pattern.

# For example, if the pattern is ["home", "away", "love"], the score is the number of users x such that x visited "home" then visited "away" and visited "love" after that.
# Similarly, if the pattern is ["leetcode", "love", "leetcode"], the score is the number of users x such that x visited "leetcode" then visited "love" and visited "leetcode" one more time after that.
# Also, if the pattern is ["luffy", "luffy", "luffy"], the score is the number of users x such that x visited "luffy" three different times at different timestamps.
# Return the pattern with the largest score. If there is more than one pattern with the same largest score, return the lexicographically smallest such pattern.

# Note that the websites in a pattern do not need to be visited contiguously, they only need to be visited in the order they appeared in the pattern.

 

# Example 1:

# Input: username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"], timestamp = [1,2,3,4,5,6,7,8,9,10], website = ["home","about","career","home","cart","maps","home","home","about","career"]
# Output: ["home","about","career"]
# Explanation: The tuples in this example are:
# ["joe","home",1],["joe","about",2],["joe","career",3],["james","home",4],["james","cart",5],["james","maps",6],["james","home",7],["mary","home",8],["mary","about",9], and ["mary","career",10].
# The pattern ("home", "about", "career") has score 2 (joe and mary).
# The pattern ("home", "cart", "maps") has score 1 (james).
# The pattern ("home", "cart", "home") has score 1 (james).
# The pattern ("home", "maps", "home") has score 1 (james).
# The pattern ("cart", "maps", "home") has score 1 (james).
# The pattern ("home", "home", "home") has score 0 (no user visited home 3 times).

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        #username
        #website

        #timestamp

        #same length 
        #step 1, sort by timestamp
        groupedData = []
        for i in range(len(username)):
            groupedData.append([timestamp[i], username[i], website[i]])
        
        groupedData.sort()

        hashmap = defaultdict(list)
        #step 2. group by user and order of what website they visited
        for time, user, site in groupedData:
            hashmap[user].append(site)
        

        count = defaultdict(int)
        #step 3, brute force and get all combinations of 3 sites
        #3 loops here and add them all to patterns and increment the count seen for that pattern
        for user in hashmap:
            patterns = set()
            curr = hashmap[user]

            for i in range(len(curr)):
                for j in range(i+1, len(curr)):
                    for k in range(j + 1, len(curr)):
                        patterns.add((curr[i], curr[j], curr[k]))
            for p in patterns:
                count[p] += 1
        max_count = 0

        res = tuple()
        #step 4, get the max pattern and smallest lexi pattern
        for pattern in count:
            if count[pattern] > max_count or (count[pattern] == max_count and pattern < res):
                max_count = count[pattern]
                res = pattern
        return list(res)