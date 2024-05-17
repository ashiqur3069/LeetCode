# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        if not head: return head
        if head and not head.next: return None
        slow, fast, prev = head, head, head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = slow.next
        return head


#####################################################
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        fast=head
        slow=head
        prev=None
        while fast and fast.next:
            fast=fast.next.next
            prev=slow
            slow=slow.next
         
        if prev:  
            prev.next = slow.next
        else:  
            head = head.next
        return head
        
        
