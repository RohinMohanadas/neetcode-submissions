class StockSpanner:

    def __init__(self):
        self.prices = []
        self.stack = []
        self.idx = 0
        
    def next(self, price: int) -> int:
        print(self.stack)
        self.prices.append(price)
        count = 0
        if self.stack:
            span = 1
            if self.stack[-1][0] > price:
                self.stack.append((price,1))
            else:
                while self.stack and self.stack[-1][0] <= price:
                    span+= self.stack[-1][1]
                    self.stack.pop()
                self.stack.append((price,span))
        else:
            self.stack.append((price,1))
            return 1

        return self.stack[-1][1]
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)