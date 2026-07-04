# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        dummy = TreeNode(0,root,root)
        storeRoot = root
        if not root:
            return TreeNode(val)
            
        def insert(root,parent,val):
            if not root:
                if parent.val > val:
                    parent.left = TreeNode(val)
                else:
                    parent.right = TreeNode(val)
                return None
            
            if root.val > val:
                insert(root.left,root, val)
            else:
                insert(root.right,root, val)
        
        insert(storeRoot,dummy,val)

        return dummy.left