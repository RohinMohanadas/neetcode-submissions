class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSumHash = defaultdict(int)

        prefix = 0
        count = 0
        prefixSumHash[0] = 1

        for i in nums:
            prefix += i
            
            if (prefix - k) in prefixSumHash:
                count += prefixSumHash[prefix - k]
            
            prefixSumHash[prefix] +=1

        print(count)
        return count
            
        