class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.queue = []

    def push(self, x: int) -> None:
        while self.queue:
            self.stack1.append(self.queue.pop())
        self.stack1.append(x)
        print("push",self.stack1)
        
    def pop(self) -> int:
        
        while self.stack1:
            self.queue.append(self.stack1.pop())
        print("pop",self.queue)
        return self.queue.pop()
        
    def peek(self) -> int:
        while self.stack1:
            self.queue.append(self.stack1.pop())
        print("peek",self.queue)
        return self.queue[-1] if not self.empty() else None 
        
    def empty(self) -> bool:
        print("empty",self.queue)
        return False if (len(self.queue)!=0 or len(self.stack1)!=0) else True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()