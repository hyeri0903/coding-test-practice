# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        tmp = []
        while head != None:
            tmp.append(head.val)
            head = head.next
            
        if tmp == tmp[::-1]:
            return True
        
        return False
        
