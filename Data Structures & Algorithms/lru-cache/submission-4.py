class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.nxt = None

class LRUCache:

    def __init__(self, capacity: int):
        self.maxsize = capacity
        self.cache = {}
        self.front = ListNode(0,0)
        self.tail = ListNode(0,0)
        self.front.nxt, self.tail.prev = self.tail, self.front

    def get(self, key: int) -> int:
        print("get",self.cache)
        if key in self.cache:
            self.cache[key].nxt.prev = self.cache[key].prev #remove
            self.cache[key].prev.nxt = self.cache[key].nxt

            self.cache[key].prev = self.tail.prev 
            self.cache[key].nxt = self.tail
            self.tail.prev.nxt = self.cache[key] # move to right
            self.tail.prev = self.cache[key]
            

            return self.cache[key].val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        print("size",self.maxsize)

        if key in self.cache:
            # self.cache[key].val = value #update val
            
            self.cache[key].prev.nxt = self.cache[key].nxt # remove
            self.cache[key].nxt.prev = self.cache[key].prev

        self.cache[key] = ListNode(key,value)


        self.cache[key].prev = self.tail.prev 
        self.cache[key].nxt = self.tail
        self.tail.prev.nxt = self.cache[key] # move to right
        self.tail.prev = self.cache[key]

        if len(self.cache) > self.maxsize:
            print("no space")
            lru = self.front.nxt
            print(lru.key, lru.val)
            lru.prev.nxt = lru.nxt
            lru.nxt.prev = lru.prev

            del self.cache[lru.key]
            


