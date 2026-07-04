class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = []
        for i in range(len(position)):
            combined.append((position[i],speed[i],(target-position[i])/speed[i]))
        
        combined.sort()
        stack=[]

        for i in combined[::-1]:
            if stack:
                if i[2]> stack[-1][2]:
                    stack.append(i)
            else:
                stack.append(i)
        return len(stack)
