import heapq

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        minheap = []
        for i in nums:
            heapq.heappush(minheap,i)
        
        #empty list
        if not nums:
            return 0

        prev = heapq.heappop(minheap)
        maxlength = 1
        currentlen = 1
        while len(minheap):
            curr = heapq.heappop(minheap)
            if curr == prev:
                continue
            elif curr == (prev+1):
                currentlen += 1
                prev = curr
                if currentlen > maxlength:
                    maxlength = currentlen
            else:
                prev = curr
                currentlen = 1
        
        return maxlength
