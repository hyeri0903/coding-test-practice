# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        tmp = []
        answerList = None
        
        while head != None:
            tmp.append(head.val)
            head = head.next
            
        rev = tmp[::-1]
        
        for i in range(len(rev)):
            if i == 0:
                answerList = ListNode(rev[i])
            else:
                newNode = ListNode(rev[i])
                curNode = answerList
                while curNode.next != None:
                    curNode = curNode.next
                curNode.next = newNode
                
        return answerList
                
        
        
