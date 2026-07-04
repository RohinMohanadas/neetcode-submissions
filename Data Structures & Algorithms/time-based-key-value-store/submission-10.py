class TimeMap:

    def __init__(self):
        self.kvmap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.kvmap:
            self.kvmap[key].append((value,timestamp))
        else:
            self.kvmap[key] = [(value,timestamp)]

    def get(self, key: str, timestamp: int) -> str:

        if key in self.kvmap :
            if self.kvmap[key][0][1] > timestamp:
                return ""
            if self.kvmap[key][-1][1]<=timestamp:
                return(self.kvmap[key][-1][0]) 

            l,r = 0, len(self.kvmap[key])-1

            res = r
            searchlist = self.kvmap[key]
            print(searchlist)
            ctr = 0
            while l<=r:
                mid = l+(r-l)//2
                print(l,mid,r)
                print(searchlist[mid][1],timestamp)
                if searchlist[mid][1] > timestamp:
                    r = mid -1
                elif searchlist[mid][1] < timestamp:
                    l = mid +1
                else:
                    res = mid
                    return(self.kvmap[key][mid][0])
                    

                ctr+=1
                print(ctr)
                if ctr == 30:
                    break

            res = min(res,l)
            return(self.kvmap[key][res-1][0])
        else:
            return ""
        
