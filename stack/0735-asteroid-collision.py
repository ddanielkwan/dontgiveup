# We are given an array asteroids of integers representing asteroids in a row. 
# The indices of the asteroid in the array represent their relative position in space.

# For each asteroid, the absolute value represents its size,
#  and the sign represents its direction (positive meaning right, negative meaning left). 
# Each asteroid moves at the same speed.

# Find out the state of the asteroids after all collisions. 
# If two asteroids meet, the smaller one will explode. 
# If both are the same size, both will explode. 
# Two asteroids moving in the same direction will never meet.

 

# Example 1:

# Input: asteroids = [5,10,-5]
# Output: [5,10]
# Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.


class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        
        #smaller one gets destroyed
        #intuition: two asteroids meet result immediately 

        #we dont need to subtract, dont get confused
        #find state of final asteroids
        stack = []

        for ass in asteroids:
            addToAssCollection = True #we can only add if final state of asteroid

            while stack and stack[-1] > 0 and ass < 0: #going towards same direction collide, 
                # we need thisloop to keep going e.g [1,2,-3] -> [1,-3] -> [-3]
                if abs(stack[-1]) > abs(ass):
                    #small one(current ass) gets destroyed, so we do not add 
                    addToAssCollection = False
                    break
                
                elif abs(stack[-1]) < abs(ass): #else the current is larger than prev so we remove prev
                    stack.pop()
                
                else:
                    #both lose if same
                    addToAssCollection = False
                    stack.pop()
                    break

            if addToAssCollection:
                stack.append(ass)
            
        return stack

