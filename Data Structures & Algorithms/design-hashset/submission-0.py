class MyHashSet:

    def __init__(self):
        self.data = []
        self.nums = len(self.data)
        

    def add(self, key: int) -> None:
        if self.data.count(key) == 0:
            self.data.append(key)
        

    def remove(self, key: int) -> None:
        if key in self.data:
            self.data.remove(key)
        

    def contains(self, key: int) -> bool:
        if key in self.data:
            return True
        else:
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)