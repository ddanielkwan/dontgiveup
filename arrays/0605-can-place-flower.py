# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.


#ADJUST THE ARRAY
class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        #0 is empty
        #1 is not empty


        if n == 0 :
            return True
        #the place before first index and place after last index should be 0 and available

        #we can go through each spot and check left and right and update accordingly

        flowerbed = [0] + flowerbed + [0]
        #[0, 1, 2, 3, 0]
        #previous length = 3
        #new length = 5 , not end inclusive
        for index in range(1, len(flowerbed)-1):
            if flowerbed[index-1] == 0 and flowerbed[index+1] == 0 and flowerbed[index] == 0:
                flowerbed[index] = 1
                n -= 1
                if n == 0 :
                    return True
                
        return False
    


