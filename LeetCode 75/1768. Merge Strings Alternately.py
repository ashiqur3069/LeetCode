class Solution(object):
    def mergeAlternately(self, word1, word2):
        result = ""
        i , j = 0, 0
        while i < len(word1) and j < len(word2):
            result += word1[i]
            result += word2[j]
            i += 1
            j += 1
        result += word1[i:]
        result += word2[j:]
        return result


###############################################
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
        
        
