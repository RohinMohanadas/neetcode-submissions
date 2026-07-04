class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxarea = float("-inf")
        for i,v in enumerate(heights):
            if not stack:
                stack.append((i,v))
            else:
                idx = i
                while stack and stack[-1][1] > v:
                    maxarea = max((i-stack[-1][0])*stack[-1][1],maxarea)
                    idx,_ = stack.pop()
                stack.append((idx,v))
        
        while stack:
            maxarea = max(maxarea,(len(heights)-stack[-1][0])*stack[-1][1])
            stack.pop()
        return maxarea