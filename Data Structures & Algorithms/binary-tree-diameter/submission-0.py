# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.dia = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def dfs(curr):

            if not curr:
                return 0
            
            left = dfs(curr.left)
            right = dfs(curr.right)

            self.dia = max(self.dia, left+right)

            return max(left,right)+1
        
        dfs(root)
        return self.dia