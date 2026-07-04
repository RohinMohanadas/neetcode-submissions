class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefix = [0]*len(nums)
        prefixval = 0

        for i,v in enumerate(nums):
            prefix[i]=v+prefixval
            prefixval = prefix[i]
        
        print(prefix)
        minlength = float("inf")

        if prefix[-1] < target:
            return 0
        for l in range(len(nums)):
            for r in range(l,len(nums)):
                if l == 0:
                    if prefix[r]>=target:
                        minlength = min(minlength,r+1)
                        print("right",r)
                        break
                else:
                    if prefix[r]-prefix[l-1] >= target:
                        minlength = min(minlength, r-l+1)
                        print("left",l, "right", r)
                        break
        
        return minlength

