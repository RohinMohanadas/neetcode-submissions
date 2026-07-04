class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashMap = defaultdict(int)
        max = -1
        maxNum = float("-inf")
        for num in nums:
            hashMap[num] += 1
            print(hashMap)
            if max < hashMap[num]:
                print(max)
                max = hashMap[num]
                maxNum = num
        return maxNum


        