class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        limit = len(nums) // 3
        hashMap = defaultdict(int)
        uniques = set()
        for i in nums:
            hashMap[i] += 1
            if hashMap[i] > limit:
                uniques.add(i)
        
        return list(uniques)