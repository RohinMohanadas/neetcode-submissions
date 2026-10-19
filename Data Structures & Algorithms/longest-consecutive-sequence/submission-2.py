class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        hmap = {}
        maxlen = float("-inf")
        for i in sorted(nums):
            if i-1 in hmap:
                hmap[i] = hmap[i-1]+1
            else:
                hmap[i] = 1
            maxlen = max(maxlen,hmap[i])
        
        return maxlen
        