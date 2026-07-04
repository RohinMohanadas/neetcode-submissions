class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        for i,v in enumerate(nums):
            if i>0 and nums[i-1]==nums[i]:
                continue
            #targetCurr = target - nums[i]
            for j in range(i+1,len(nums)):
                if j>i+1 and nums[j-1]==nums[j]:
                    continue
                
                l,r = j+1, len(nums)-1
                
                while l<r:
                    sum = nums[i]+nums[j]+nums[l]+nums[r]
                    if sum < target:
                        l+=1
                    if sum > target:
                        r-=1
                    if sum == target:
                        result.append([nums[i],nums[j],nums[l],nums[r]])
                        l+=1
                        r-=1
                        while l < r and nums[l]==nums[l-1]:
                            l+=1
                        while l < r and nums[r]==nums[r+1]:
                            r-=1
        return result

        