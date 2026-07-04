class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        result = []
        i = 0

        for i in range(len(nums)):
            if nums[i]>0:
                break
                


            if i>0 and nums[i]==nums[i-1]:
                continue

            left = i+1
            right = len(nums)-1

            while left<right:
                sum3 = nums[i] + nums[left] + nums[right]
                

                if sum3 == 0:
                    
                    result.append([nums[i],nums[left],nums[right]])
                    #find the next unique num
                    left+=1
                    right-=1
                    
                    while nums[left]==nums[left-1] and left < right:
                        left+=1
                    
                elif sum3 < 0:
                    left+=1
                else:
                    right-=1
        return result        
                    

            
            
