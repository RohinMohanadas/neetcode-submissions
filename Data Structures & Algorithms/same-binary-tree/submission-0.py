# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.same = True
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def checkSame(p,q):
            if not p and not q:
                return True
            if (not q and p) or (not p and q):
                return False
                
            if p.val == q.val:
                self.same = checkSame(p.left,q.left) and checkSame(p.right,q.right)
            else:
                self.same = False

            return self.same
        
        return checkSame(p,q)