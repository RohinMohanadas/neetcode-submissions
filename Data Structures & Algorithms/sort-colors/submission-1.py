class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #hashMap = defaultdict(int)
        
        counts = [0]*3
        for i in nums:
            if i == 0:
                counts[0] +=1
            elif i == 1:
                counts[1] +=1
            else:
                counts[2] +=1
        
        ctr = 0
        for i in range(counts[0]):
            nums[ctr] = 0
            ctr +=1
        for i in range(counts[1]):
            nums[ctr] = 1
            ctr +=1
        for i in range(counts[2]):
            nums[ctr] = 2
            ctr +=1