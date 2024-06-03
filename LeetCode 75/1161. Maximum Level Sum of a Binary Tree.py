# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        q = deque()
        q.append(root)
        maxSum = root.val
        level = 1
        res = 1
    
        while q:
            qlen = len(q)
            levelSum = 0
            for i in range(qlen):
                node = q.popleft()
                levelSum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if levelSum > maxSum:
                maxSum = levelSum
                res = level
            level +=1
        return res

                
            



        
