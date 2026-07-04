class Solution:
    def trap(self, height: List[int]) -> int:
        maxleft = [0]*len(height)
        maxright = [0]*len(height)
        leftmax = 0
        rightmax = 0
        for i in range(len(height)):
            maxleft[i] = max(leftmax,height[i])
            leftmax = maxleft[i]
            maxright[len(height)-i-1] = max(rightmax,height[len(height)-i-1])
            rightmax = maxright[len(height)-i-1]

        print (maxleft)
        print (maxright)
        water = 0
        for i in range(len(height)): 
            water += max(min(maxleft[i],maxright[i])-height[i],0)
        return water
        