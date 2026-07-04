"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def contents_same(grid,row1,col1,row2,col2):
            init = grid[row1][col1]
            for i in range(row1,row2):
                for j in range(col1, col2):
                    if init!=grid[i][j]:
                        return -1
            return init

        def recurs(grid, row1,col1,row2,col2) -> 'Node':
            gridval = contents_same(grid,row1,col1,row2,col2)
            if gridval!=-1:
                return Node(gridval,True,None,None,None,None)
            else:
                topLeft = recurs(grid,row1,col1,math.ceil((row1+row2)/2), math.ceil((col1+col2)/2))
                topRight = recurs(grid,row1,math.ceil((col1+col2)/2),math.ceil((row1+row2)/2), col2)
                bottomLeft = recurs(grid,math.ceil((row1+row2)/2),col1,row2, math.ceil((col1+col2)/2))
                bottomRight = recurs(grid,math.ceil((row1+row2)/2),math.ceil((col1+col2)/2),row2,col2)

                return Node(1,False,topLeft,topRight,bottomLeft,bottomRight)

        return recurs(grid,0,0,len(grid),len(grid))
