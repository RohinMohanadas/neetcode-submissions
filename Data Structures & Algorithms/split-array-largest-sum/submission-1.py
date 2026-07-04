class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def cansplit(largest):
            subarrays = 0
            cumsum = 0
            for i in nums:
                cumsum+=i
                if cumsum > largest:
                    subarrays+=1
                    cumsum=i
            return (subarrays + 1)<=k

        l,r = max(nums),sum(nums)
        res = r
        while l<=r:
            mid = l+(r-l)//2
            if cansplit(mid):
                res = mid
                r = mid-1
            else:
                l = mid+1

        return res
            

                

