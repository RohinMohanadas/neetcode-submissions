class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        countZero = 0
        prod = 1
        for i in nums:
            if i == 0:
                countZero += 1
                prod *= 1
            else:
                prod *= i

        if countZero > 1:
            return [0]*len(nums)
        else:
            for idx, val in enumerate(nums):
                if val == 0:
                    nums[idx] = prod
                else:
                    if countZero == 1:
                        nums[idx] = 0
                    else:
                        nums[idx] = prod//val
        
        return nums
        