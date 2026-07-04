class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        for i,v in enumerate(nums):
            if v in hashmap:
                if i - hashmap[v] <= k:
                    return True
                else:
                    hashmap[v]=i
            else:
                hashmap[v] = i
        return False