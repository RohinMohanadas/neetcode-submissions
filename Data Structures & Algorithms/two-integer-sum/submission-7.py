class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashSet = {nums[i]:[]+i for i in nums}
        hashSet = {}
        for i,v in enumerate(nums):
            hashSet.setdefault(v,[]).append(i)
        
        print(hashSet)
        for i,v in enumerate(nums):
            remnant = target - v
            # edge case
            if remnant == v:
                if len(hashSet[remnant]) == 2:
                    arr = hashSet[remnant]
                    arr.sort()
                    return arr
                else:
                    continue
            if remnant in hashSet:
                if len(hashSet[remnant]) == 1:
                    print("why am i here")
                    arr = [hashSet[v][0],hashSet[remnant][0]]
                    arr.sort()
                    return arr
