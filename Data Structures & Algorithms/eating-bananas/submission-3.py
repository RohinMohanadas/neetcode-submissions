import math

class Solution:
    #def hoursneeded(self, piles, )
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxval = max(piles)

        l,r = 1, maxval
        res = r
        print(maxval)
        while l<=r:
            mid = (r+l)//2
            print("mid",mid)
            print("l,r",l,r)
            hours = 0
            for i in piles:
                hours+=math.ceil(i/mid)
            print("hours", hours )
            if hours <= h:
                res = min(res,mid)
                r = mid - 1
            elif hours > h:
                l = mid + 1
        
        return res

