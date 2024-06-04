# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        if root:
            if root.val < key:
                root.right = self.deleteNode(root.right,key)
            elif root.val > key:
                root.left = self.deleteNode(root.left,key)
            else:
                if not root.right:
                    return root.left
                elif not root.left:
                    return root.right
                else:
                    cur = root.right
                    while cur.left:
                        cur = cur.left
                    root.val = cur.val
                    root.right = self.deleteNode(root.right,root.val)
            return root
                    
        
