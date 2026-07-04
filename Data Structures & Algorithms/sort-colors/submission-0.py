class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hashMap = defaultdict(int)

        for i in nums:
            hashMap[i] += 1
        
        ctr = 0
        for i in range(hashMap[0]):
            nums[ctr] = 0
            ctr +=1
        for i in range(hashMap[1]):
            nums[ctr] = 1
            ctr +=1
        for i in range(hashMap[2]):
            nums[ctr] = 2
            ctr +=1