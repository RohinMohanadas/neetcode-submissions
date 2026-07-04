class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r = 0,0
        sum = 0
        maxlen = float("inf")
        for r in range(len(nums)):

            sum+=nums[r]
            
            while sum >= target:
                maxlen = min(maxlen,r-l+1)
                print("maxlen",maxlen)
                sum-=nums[l]
                l+=1

        
        if maxlen==float("inf"):
            return 0
        else:    
            return maxlen

