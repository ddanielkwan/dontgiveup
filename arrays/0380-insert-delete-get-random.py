# Implement the RandomizedSet class:

# RandomizedSet() Initializes the RandomizedSet object.
# bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
# bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
# int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element
#  exists when this method is called). Each element must have the same probability of being returned.
# You must implement the functions of the class such that each function works in average O(1) time complexity.


import random


class RandomizedSet:
    #let us store the val in an array and also store the index in the hashmap val:index
    #when we remove we can replace the last element of the array to the removed spot
    #1. get the index of the value we want to remove
    #2. get the last element of the array, this will be the value we will use to replace the removed value
    #3. replace the value at indexremoval to the last element
    #4. pop from array since last element
    #5. update reference of that element to removal index
    #6. delete value from hashmap
    def __init__(self):
        self.array = []  #stores val
        self.hashmap = {} #stores val: index
        

    def insert(self, val: int) -> bool:
        status = val in self.hashmap

        if not status:
            self.array.append(val) #append first to array
            self.hashmap[val] = len(self.array) - 1 #add index to hashmap
            return True
        
        return False
        

    def remove(self, val: int) -> bool:
        if val in self.hashmap: #if val is in hashmap, lets get removal index
            removalIndex = self.hashmap[val]
            replaceWithElement = self.array[-1]

            self.array[removalIndex] = replaceWithElement
            self.array.pop() #o(1)
            
            self.hashmap[replaceWithElement] = removalIndex

            del self.hashmap[val]
            return True
        
        return False
        

    def getRandom(self) -> int:
        return random.choice(self.array)
        

