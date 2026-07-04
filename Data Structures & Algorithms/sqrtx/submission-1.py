class Solution:
    def mySqrt(self, x: int) -> int:
        l,r = 0,x//2
        if x == 0 or x == 1:
            return x
        while l<=r:
            mid = l+(r-l)//2
            comp = mid*mid
            if comp > x:
                r = mid-1
            elif comp < x:
                l = mid+1
            else: 
                return mid
        return r