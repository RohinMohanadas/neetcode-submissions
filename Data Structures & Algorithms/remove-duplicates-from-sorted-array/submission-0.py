class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        newidx = [-1]*len(nums)

        left = 0
        right = 0
        unique = 1
        
        while right < len(nums):
            if nums[left]==nums[right]:
                print(nums[left], nums[right])
                right+=1
            else:
                nums[unique]=nums[right]
                unique+=1
                left = right
                print("next uniqye",nums[right])
            
        print(nums)
        return unique