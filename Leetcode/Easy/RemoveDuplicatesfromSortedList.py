
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        
        while cur!=None and cur.next != None:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
                
        return head
            
        
