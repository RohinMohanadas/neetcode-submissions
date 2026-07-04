# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = True
        def checkBal(root) -> int:
            if not root:
                return 0
            left = checkBal(root.left)
            right = checkBal(root.right)
            if abs(left -right)>1:
                self.res = False 
            return(max(left,right)+1)
        
        checkBal(root)
        return self.res