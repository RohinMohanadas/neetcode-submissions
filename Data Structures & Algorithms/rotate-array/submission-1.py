class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        array = [0]*len(nums)
        for i,v in enumerate(nums):

            array[(i + k) % (len(nums))] = nums[i]
        
        nums[:] = array
            
        

            

