class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxlen = float("-inf")
        hset = set()
        for i in nums:
            hset.add(i)
        
        for i in nums:
            if i-1 in hset:
                continue
            else:
                newlist = [i]
                ctr = i
                while (ctr+1) in hset:
                    newlist.append(i+1)
                    ctr+=1
                maxlen = max(maxlen,len(newlist))

        return maxlen
        