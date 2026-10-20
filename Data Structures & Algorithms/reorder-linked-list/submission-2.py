# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
        # now slow is at mid point

        # split 
        second = slow.next 
        slow.next = None 

        # reverse the second one: 
        prev = None 
        tmp = None 
        while second:
            tmp = second.next 
            second.next = prev
            prev = second  
            second = tmp

        # merge: prev now is the new head, the usual return of reverse linked lists
        first, second = head, prev

        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1 
            first, second = tmp1, tmp2
