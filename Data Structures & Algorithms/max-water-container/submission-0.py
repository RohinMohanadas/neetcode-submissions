class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxvol = -float("inf")

        left = 0
        right = len(heights)-1

        while left<right:
            currentvol = (right-left)*min(heights[left],heights[right])
            if maxvol < currentvol:
                print("true")
                maxvol = currentvol

            if heights[left]<heights[right]:
                print("left")
                left+=1
            else:
                print("rught")
                right-=1

        return maxvol