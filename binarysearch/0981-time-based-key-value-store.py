#     Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

# Implement the TimeMap class:

# TimeMap() Initializes the object of the data structure.
# void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
# String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".


from collections import defaultdict


class TimeMap:

    def __init__(self):

        self.store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
    
        res = ""
        if key not in self.store:
            return res

        l = 0
        r = len(self.store[key]) - 1
        row = self.store[key]
        while l <= r :

            m = l + (r-l)//2 


            if row[m][0] <= timestamp:
                res = row[m][1]
                l = m + 1
            else:
                r = m - 1


        return res
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

