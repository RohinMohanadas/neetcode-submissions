class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        init = nums[0]
        count = 0
        hashMap = defaultdict(int)
        for i in nums:
            hashMap[i] += 1

        countArray  = [[] for i in range(len(nums)+1)]

        for key,v in hashMap.items():
            countArray[v].append(key)

        res = []

        for i in reversed(countArray):
            for n in i:
                res.append(n)
                if len(res) == k:
                    return res
            

        