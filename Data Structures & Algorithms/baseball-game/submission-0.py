class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = 0
        stack = []
        for i in operations:
            if i=="+":
                stack.append(stack[-1]+stack[-2])
                
            elif i=="D":
                stack.append(2*stack[-1])
            elif i=="C":
                res-=stack[-1]
                stack.pop()
                continue
            else:
                stack.append(int(i))
            
            res+=stack[-1]
            print(stack, res)

        return res

        

        