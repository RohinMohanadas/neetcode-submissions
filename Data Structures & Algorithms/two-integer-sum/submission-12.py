class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hMap = defaultdict(List)
        for j,i in enumerate(nums):
            if i in hMap:
                hMap[i].append(j)
            else:
                hMap[i] = [j]
        print(hMap)

        for k,v in hMap.items():
            if (target-k == k):
                if len(hMap[k])>1:
                    return hMap[k][0:2]
                else:
                    continue

            if (target-k) in hMap:
                return [hMap[k][0],hMap[target-k][0]]
