class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = left+1
        maxprofit = 0
        while right < len(prices):
            if prices[left]>prices[right]:
                left+=1
            else:
                maxprofit = max(maxprofit, prices[right]-prices[left])
                right+=1
        print(maxprofit)
        return maxprofit
            
        