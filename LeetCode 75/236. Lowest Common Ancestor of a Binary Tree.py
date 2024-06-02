# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if root:
            if root == p or root == q: return root
            leftN = self.lowestCommonAncestor(root.left,p,q)
            rightN = self.lowestCommonAncestor(root.right,p,q)

            if leftN != None and rightN != None: return root
            if leftN != None: return leftN
            return rightN
        
