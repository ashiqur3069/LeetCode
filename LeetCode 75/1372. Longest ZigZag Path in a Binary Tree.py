# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestZigZag(self, root):
        self.max_path = 0
        def helper(root,left,right):
            if root:
                self.max_path = max(self.max_path,left,right)
                helper(root.left,right+1,0)
                helper(root.right,0,left+1)
        helper(root,0,0)
        return self.max_path    


