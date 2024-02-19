# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        if not head or not head.next:
            return head
        left = head
        right = self.getmid(head)
        temp = right.next
        right.next = None
        right = temp

        left = self.sortList(left)
        right = self.sortList(right)
        return self.marge(left,right)
    def getmid(self,head):
        slow, fast = head,head.next
        while fast and fast.next:
            slow =slow.next
            fast =fast.next.next
        return slow
    def marge(self,lst1,lst2):
        tail = dummy = ListNode()
        while lst1 and lst2:
            if lst1.val < lst2.val:
                tail.next = lst1
                lst1 = lst1.next
            else:
                tail.next = lst2
                lst2 = lst2.next
            tail = tail.next
        if lst1:
            tail.next = lst1
        if lst2:
            tail.next = lst2
        return dummy.next












        
            
        
