class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r = 0, len(matrix)*len(matrix[0])-1
        while l<=r:
            mid = l+(r-l)//2
            print("l,r",l,r)
            row,col = mid//len(matrix[0]) , mid%len(matrix[0])
            print("mid",mid,"row",row,"col",col)
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False