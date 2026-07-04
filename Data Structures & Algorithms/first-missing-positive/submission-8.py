class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        if nums[0]>1:
            return 1
        first = True
        for i in range(len(nums)):
            if nums[i] >= 0:
                   
                if first and nums[i]>0 and nums[i]!=1:
                    return 1
                if i+1 == len(nums):
                    return nums[i]+1
                if nums[i+1] == nums[i]+1 or nums[i+1] == nums[i]:
                    first = False
                    continue
                else:
                    return (1 if ((nums[i]+1) == 0) else nums[i]+1)
                
                
            else:
                continue
        return 1