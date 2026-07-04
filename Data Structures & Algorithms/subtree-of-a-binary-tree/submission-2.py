# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def __init__(self):
        self.res = False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def subtreematch(root, subtree):
            if not root and not subtree:
                return True
            
            if (root and subtree) and (root.val == subtree.val):
                return subtreematch(root.left,subtree.left) and subtreematch(root.right, subtree.right)
            else:
                return False

        if not root:
            return True
        
        if root.val == subRoot.val:
            self.res = self.res or subtreematch(root,subRoot)
        
        self.isSubtree(root.left,subRoot)
        self.isSubtree(root.right,subRoot)

        return self.res
        