class Solution:

    def decodeString(self, s: str) -> str:
        stack = []
        for i in s:
            if i=="]":
                res=""
                counter = ""
                while stack[-1]!="[":
                    res = stack.pop()+res
                stack.pop()
                while stack and stack[-1].isdigit():
                    counter = stack.pop()+counter
                stack.append(int(counter)*res)
            else:
                stack.append(i)
        
        return("".join(stack))