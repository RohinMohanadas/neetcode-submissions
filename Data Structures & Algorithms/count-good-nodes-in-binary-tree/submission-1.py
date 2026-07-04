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
        
        def findNodes(root,maxSo):
            if not root:
                return 0
            if root.val >= maxSo:
                maxSo = max(maxSo, root.val)
                self.nodes+=1
            findNodes(root.left,maxSo)
            findNodes(root.right,maxSo)                
        
        findNodes(root,self.currmax)
        return self.nodes
        

        