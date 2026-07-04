class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        stack = []
        for i,v in enumerate(temperatures):
            while stack and stack[-1][0] < v:
                _,idx = stack.pop()
                result[idx] = i - idx
            stack.append((v,i))
        return result        

            


        