class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        i = 0
        while l<=r:
            mid = (r+l)//2
            print(nums[mid],l,r,mid)
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                r = mid-1
            else:
                l = mid+1

            i+=1
            if i > 20: 
                break
        return -1
        