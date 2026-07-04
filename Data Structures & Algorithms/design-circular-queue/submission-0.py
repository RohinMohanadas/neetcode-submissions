class MyCircularQueue:

    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next       

    def __init__(self, k: int):
        self.front = self.ListNode()
        self.rear = self.front
        self.size = k
        self.sizerem = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            print("im full")
            return False
        elif self.isEmpty():
            tmp = self.ListNode(value,None)
            self.front = tmp
            self.rear = tmp
            self.sizerem -= 1
            return True
        else:
            tmp = self.ListNode(value,None)
            self.rear.next = tmp
            self.rear = tmp
            self.sizerem -= 1
            return True


    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.front.val = 0
            self.front = self.front.next
            self.sizerem += 1
            return True
        else:
            return False
        

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.front.val

    def Rear(self) -> int:
        print(self.sizerem, self.size, self.rear.val)
        return -1 if self.isEmpty() else self.rear.val
        

    def isEmpty(self) -> bool:
        return self.sizerem == self.size
        

    def isFull(self) -> bool:
        return self.sizerem == 0
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()