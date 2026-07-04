class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        
        print(nums)
        nums = list(dict.fromkeys(nums))
        print(nums)
        l,r = 0, len(nums)-1
        while l<=r:
            mid = l+(r-l)//2

            print(l,mid,r)
            if target == nums[mid]:
                return True

            if nums[l] <= nums[mid]: # in left subarray
                print("left sub")
                if nums[l] < target and target <= nums[mid]:
                    r = mid 
                else:
                    l = mid + 1

            elif nums[l] > nums[mid]: # in the right subarray
                print("right sub")
                if nums[r] > target and target >= nums[mid]:
                    l = mid 
                else:
                    r = mid - 1
            else:
                l+=1
        return False


        