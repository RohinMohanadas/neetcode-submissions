from collections import deque

class MyStack:

    def __init__(self):
        self.queueone = deque()
        self.queuetwo = deque()

    def push(self, x: int) -> None:
        self.queueone.append(x)
        self.queuetwo.appendleft(self.queueone.popleft())
        print(self.queuetwo)

    def pop(self) -> int:
        res = self.queuetwo.popleft()
        print(self.queuetwo)
        return res
        

    def top(self) -> int:
        return self.queuetwo[0]
        
    def empty(self) -> bool:
        return False if self.queuetwo else True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()