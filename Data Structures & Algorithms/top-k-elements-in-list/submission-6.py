class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hMap = defaultdict(int)
        for i in nums:
            hMap[i] += 1
        
        import heapq
        heaparr = []
        for key,v in hMap.items():
            heapq.heappush(heaparr, (-v,key))
            #heaparr.append((-v,k))
        
        #print(heaparr)

        ret = []
        if k == 1:
            return [heaparr[0][1]]
        for i in range(k):
            ret.append(heapq.heappop(heaparr)[1])

        return ret

        