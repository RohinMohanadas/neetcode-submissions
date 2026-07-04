class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        countZero = 0
        for i in nums:
            if i == 0:
                prod *= 1
                countZero += 1
            else:
                prod *= i
        
        print(prod)
        for i in range(len(nums)):
            if nums[i] == 0:
                if countZero == 1:
                    nums[i] = int(prod/1)
                else:
                    nums[i] = 0
                continue
            else:
                if countZero != 0:
                    nums[i] = 0
                else:
                    nums[i] = int(prod/nums[i])
        
        return nums
        