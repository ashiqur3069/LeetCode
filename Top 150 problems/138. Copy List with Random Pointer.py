"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return
        
        cur = head
        while cur:
            temp = cur.next
            cur.next = Node(cur.val)
            cur.next.next = temp
            cur = cur.next.next
            
        
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        
        second = cur = head.next
        while cur.next:
            head.next = cur.next
            cur.next = head.next.next
            cur = cur.next
            head = head.next
        head.next = None
        return second
