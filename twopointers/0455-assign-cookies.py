# Assume you are an awesome parent and want to give your children some cookies. 
# But, you should give each child at most one cookie.

# Each child i has a greed factor g[i], 
# which is the minimum size of a cookie that the child will be content with; 
# and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, 
# and the child i will be content. Your goal is to maximize the number of your content children 
# and output the maximum number.

 

# Example 1:

# Input: g = [1,2,3], s = [1,1]
# Output: 1
# Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
# And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
# You need to output 1.

class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        #intuition: not wasting resources, always give smallest one possible to the child to make happy
        #because big cookies are more flexible (they can satisfy more children), while small cookies are very limited.

        # A child with low greed can eat many cookies
        # A child with high greed can eat only large cookies

        #sort children by ascending greed, sort cookies by ascending size
        g.sort()
        s.sort()

        childrenPointer = 0

        cookieSizePointer = 0

        happyChildren = 0

        while childrenPointer < len(g) and cookieSizePointer < len(s):
            
            #here, we only increase children pointer once we satisfy them, the cookie pointer will always be increasing
            #because in both cases: cookie doesnt fit, or cookie consumed, it needs to move anyways
            if s[cookieSizePointer] >= g[childrenPointer]:
                happyChildren += 1
                childrenPointer += 1
            
            cookieSizePointer += 1
        
        return happyChildren
                




        
