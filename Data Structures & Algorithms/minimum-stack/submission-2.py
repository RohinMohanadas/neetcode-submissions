import heapq

class MinStack:

    def __init__(self):
        self.minval = float("inf")
        self.mystack = []
        
    def push(self, val: int) -> None:
        self.mystack.append(val)
        self.minval = min(self.minval,val)
        #heapq.heappush(self.myheap,val)
        
    def pop(self) -> None:
        if self.mystack and self.mystack[-1] == self.minval:
            self.mystack.pop()
            self.minval = float("inf")
            for i in self.mystack:
                self.minval = min(self.minval,i)
        else:
            self.mystack.pop()
        
        
    def top(self) -> int:
        return self.mystack[-1]
        
    def getMin(self) -> int:
        return self.minval if self.mystack else None
        
