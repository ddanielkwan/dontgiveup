
class ListNode:
    def __init__(self, key , val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {} #key, node
        self.capacity = capacity
        #have two nodes one on left and right, each points to beginning of the list and end of the list respectively
        self.left = ListNode(0,0)
        self.right = ListNode(0,0)
        #intially only each other
        self.left.next = self.right
        self.right.prev = self.left


    def remove(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev
    
    def insert(self, node):
        #left is lru right is most recent
        #we should insert right
        prev = self.right.prev
        nxt = self.right

        prev.next = node
        node.prev = prev
        node.next = nxt
        nxt.prev = node

    def get(self, key: int) -> int:
        status = key in self.cache
        if status:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return self.cache[key].val
        return - 1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        node = ListNode(key, value)
        self.insert(node)
        self.cache[key] = node

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
 


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

