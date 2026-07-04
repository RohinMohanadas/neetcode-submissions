class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        array = [0]*(len(nums)+1)

        for i in nums:
            if array[i]!=0:
                return i
            else:
                array[i]+=1
        