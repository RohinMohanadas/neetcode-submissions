class Solution:
    def bsearch(self, sub: List[int],left: int, right: int, n: int) -> int:
        mid = (left+right) // 2
        if left > right:
            return -1
        if sub[mid]<n:
            left = mid+1
        elif sub[mid]>n:
            right = mid - 1
        else:
            return mid       
        return self.bsearch(sub, left, right, n)

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        found = False
        while left < right:
            val = self.bsearch(numbers, left, right, target-numbers[left])
            if val > -1:
                return [left+1,val+1]
            else:
                left += 1





        