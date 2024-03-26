# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        res = []
        q = deque()
        q.append(root)
        while q:
            rightview = None
            qlen = len(q)
            for i in range(qlen):
                node = q.popleft()
                if node:
                    rightview = node
                    q.append(node.left)
                    q.append(node.right)
            if rightview:
                res.append(rightview.val)
        return res
