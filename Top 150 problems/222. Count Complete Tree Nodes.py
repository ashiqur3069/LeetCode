# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        def leftHeight(node):
            return 0 if not node else 1 + leftHeight(node.left)

        def rightHeight(node):
            return 0 if not node else 1 + rightHeight(node.right)

        def count(node):
            if not node:
                return 0

            left, right = leftHeight(node), rightHeight(node)

            if left == right:
                return 2 ** (left) - 1
            return 1 + count(node.left) + count(node.right)

        return count(root)
