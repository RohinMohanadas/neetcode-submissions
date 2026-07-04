class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        index = [
            [0,0,2,2],
            [0,3,2,5],
            [0,6,2,8],
            [3,0,5,2],
            [3,3,5,5],
            [3,6,5,8],
            [6,0,8,2],
            [6,3,8,5],
            [6,6,8,8],
            ]


        # rows
        for i in range(9):
            if not self.isValidSubmatrix(board, i, 0, i, 8):
                return False
        print("row ok")
        # columns
        for j in range(9):
            if not self.isValidSubmatrix(board, 0, j ,8, j):
                return False
        print("column ok")
        # submatrixes
        for i,j,k,l in index:
            if not self.isValidSubmatrix(board, i, j ,k, l):
                return False
        print("submatrix ok")
        return True

    
    def isValidSubmatrix(self, board, row1, col1, row2, col2) -> bool:
        countArray = [0 for _ in range(10)]
        for i in range(row1, row2+1):
            for j in range(col1, col2+1):
                if board[i][j] == ".":
                    continue
                else:
                    print(board[i][j])
                    if countArray[int(board[i][j])] == 0:
                        countArray[int(board[i][j])] += 1
                    else: 
                        return False
        print("countArray", countArray)
        return True

        