class Solution:
    def operate(self, a: int, b: int, op: str) -> int:
        print(a,b,op)
        if op == "+":
            return a+b
        elif op == "-":
            return a-b
        elif op == "*":
            return a*b
        else:
            #print(a//b)
            return int(a/b)

    def evalRPN(self, tokens: List[str]) -> int:
        evalstack = []
        for i in tokens:
            if i in ["+","-","*","/"]:
                b = evalstack.pop()
                a = evalstack.pop()
                evalstack.append(self.operate(int(a),int(b),i))
            else:
                evalstack.append(int(i))
        
        return evalstack.pop()
        