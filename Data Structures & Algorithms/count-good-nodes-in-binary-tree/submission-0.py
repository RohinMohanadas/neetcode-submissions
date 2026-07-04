# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.currmax = float("-inf")
        self.nodes = 0
    def goodNodes(self, root: TreeNode) -> int:
        self.currmax = root.val
        
        def findNodes(root,max):
            if not root:
                return 0
            if root.val >= max:
                self.nodes+=1
                findNodes(root.left,root.val)
                findNodes(root.right,root.val)
            else:
                findNodes(root.left,max)
                findNodes(root.right,max)                
        
        findNodes(root,self.currmax)
        return self.nodes
        

        