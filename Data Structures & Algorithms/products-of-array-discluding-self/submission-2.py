class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0]*len(nums)
        suffix = [0]*len(nums)
        prod = 1
        for idx,val in enumerate(nums):
            prefix[idx] = prod
            prod = prod*val
        prod = 1
        for i in range(len(nums)-1,-1,-1):
            suffix[i] = prod
            prod = prod*nums[i]

        #print(prefix)
        #print(suffix)

        retarr = []
        for i in range(len(prefix)):
            retarr.append(prefix[i]*suffix[i])

        return retarr