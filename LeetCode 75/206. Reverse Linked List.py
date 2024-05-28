# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        current = head
        prev = None
        while current != None:
            next_val = current.next
            current.next = prev
            prev = current
            current = next_val
        return prev
