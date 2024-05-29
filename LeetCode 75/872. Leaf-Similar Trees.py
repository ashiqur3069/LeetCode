# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        def dfs(root, leaf):
            if root:
                if not root.left and not root.right:
                    return leaf.append(root.val)
                dfs(root.left, leaf)
                dfs(root.right, leaf)


        leaf1, leaf2 = [], []
        dfs(root1, leaf1)
        dfs(root2, leaf2)
        return leaf1 == leaf2
        
