# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head: 
            return head
        length = 0 
        cur = head 

        while cur: 
            length += 1
            cur = cur.next 
        index = length - n 
        i = 0
        dummy = ListNode(0, head)
        tail = dummy
        # n == length fails always, since i =0 and index = 0 

        while i != index:
            tail = tail.next
            i+=1
        
        tmp = tail.next
        tail.next = tail.next.next 
        
        return dummy.next                




