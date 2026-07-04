class Solution:
    def qsrt (self, nums, left, right):
        # base
        if left >= right:  
            print([nums[left],nums[right]])
            return
        
        mid = (right + left)//2
        self.qsrt(nums, left, mid)
        self.qsrt(nums, mid+1, right)

        first = nums[left:mid+1]
        second = nums[mid+1:right+1]

        print(first)
        print(second)
        ctr = left
        # if len(first) > len(second):
        #    for i,_ in enumerate(second):
        #        if(second[i]<first[i]):
        #            nums[ctr] = second[i]
        #        else:
        #            nums[ctr] = first[i]
        #        ctr += 1
        #    for i in first[len(second)-1:]:
        #        nums[ctr] = i
        #        ctr+=1
        # else:
        #    for i,_ in enumerate(first):
        #        if(second[i]<first[i]):
        #            nums[ctr] = second[i]
        #        else:
        #            nums[ctr] = first[i]
        #        ctr += 1
        #    for i in second[len(first)-1:]:
        #        nums[ctr] = i
        #        ctr+=1
        i, j, k = left, 0, 0
        while j < len(first) and k< len(second):
            if first[j] <= second[k]:
                nums[i] = first[j]
                j += 1
            else:
                nums[i] = second[k]
                k += 1
            i += 1

        while j < len(first):
            nums[i] = first[j]
            j += 1
            i += 1

        while k < len(second):
            nums[i] = second[k]
            k += 1
            i += 1

    def sortArray(self, nums: List[int]) -> List[int]:
        self.qsrt(nums, 0, len(nums)-1)
        return nums

    
        