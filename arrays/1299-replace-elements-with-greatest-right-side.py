class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        
        largestRight = -1
        #go from backwards and check whether the current element is greater than previous largest right element
        for i in range(len(arr)-1, -1, -1):
            temp = arr[i]

            arr[i] = largestRight
            
            #only update if larger 
            if largestRight < temp:
                largestRight = temp
      
        return arr