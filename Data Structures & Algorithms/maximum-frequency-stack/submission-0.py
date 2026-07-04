class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int)
        self.stack = []
        
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        self.freq[val]+=1

    def pop(self) -> int:
         
        maxfreq = max(self.freq.values())
        for i,v in enumerate(self.stack[::-1]):
            if self.freq[v] == maxfreq:
                self.freq[v]-=1
                return self.stack.pop(len(self.stack)-i-1)
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()