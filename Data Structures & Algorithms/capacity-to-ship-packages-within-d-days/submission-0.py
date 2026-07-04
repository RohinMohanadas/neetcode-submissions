class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        maxwt = sum(weights)
        l,r = max(weights),maxwt
        #leastdays = maxwt
        print(maxwt, max(weights))

        while l<=r:
            mid = l+(r-l)//2

            remaining = mid
            dayctr = 0

            lp, rp = 0,0

            for i in weights:
                remaining -= i
                if remaining < 0:
                    dayctr+=1
                    remaining = mid - i 

            dayctr+= 1
            print(dayctr,"for ",mid)
            if dayctr <= days:
                maxwt = min(maxwt,mid)
                r = mid - 1
            else:
                l = mid +1

        return maxwt