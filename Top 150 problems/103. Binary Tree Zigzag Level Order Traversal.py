# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        res = []
        q = deque()
        q.append(root)
        while q:
            lvl = []
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    lvl.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if lvl:
                lvl = reversed(lvl) if len(res) % 2 else lvl
                res.append(lvl)
        return res

        
