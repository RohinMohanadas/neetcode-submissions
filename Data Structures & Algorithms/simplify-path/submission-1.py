class Solution:
    def simplifyPath(self, path: str) -> str:
        print(path.split("/"))
        stack=[]
        for i in path.split("/"):
            if stack:
                if i == "" or i==".":
                    continue
                elif i == "..":
                    if len(stack) == 1:
                        continue
                    else:
                        stack.pop()
                else:
                    if stack[-1]!="/":
                        stack.append("/")
                    stack.append(i)
            else:
                stack.append("/")
            if len(stack)>1 and stack[-1]=="/":
                stack.pop()
        return "".join(stack)